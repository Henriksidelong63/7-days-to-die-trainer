import ctypes
import time
from typing import Optional

class SevenDaysTrainer:
    def __init__(self, process_name: str = "7DaysToDie.exe"):
        self.process_name = process_name
        self.process_id: Optional[int] = None
        self.module_base: Optional[int] = None
        self.handle: Optional[int] = None

    def find_process(self) -> bool:
        """Find the game process and get its handle."""
        PROCESS_ALL_ACCESS = 0x1F0FFF
        process_entry = ctypes.create_string_buffer(1024)
        process_snapshot = ctypes.windll.kernel32.CreateToolhelp32Snapshot(0x2, 0)

        if process_snapshot == -1:
            return False

        process_entry.dwSize = ctypes.sizeof(process_entry)
        if not ctypes.windll.kernel32.Process32First(process_snapshot, ctypes.byref(process_entry)):
            ctypes.windll.kernel32.CloseHandle(process_snapshot)
            return False

        while True:
            if process_entry.szExeFile.decode() == self.process_name:
                self.process_id = process_entry.th32ProcessID
                self.handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, self.process_id)
                ctypes.windll.kernel32.CloseHandle(process_snapshot)
                return True

            if not ctypes.windll.kernel32.Process32Next(process_snapshot, ctypes.byref(process_entry)):
                break

        ctypes.windll.kernel32.CloseHandle(process_snapshot)
        return False

    def write_memory(self, address: int, value: int, size: int = 4) -> bool:
        """Write value to memory address."""
        if not self.handle:
            return False

        bytes_written = ctypes.c_size_t()
        return ctypes.windll.kernel32.WriteProcessMemory(
            self.handle, address, ctypes.byref(ctypes.c_int(value)), size, ctypes.byref(bytes_written)
        )

    def set_health(self, value: int = 1000) -> bool:
        """Set player health to specified value."""
        if not self.find_process():
            return False

        # Hardcoded health address (would need to be updated per game version)
        health_address = 0x145A3B8C
        return self.write_memory(health_address, value)

    def set_stamina(self, value: int = 100) -> bool:
        """Set player stamina to specified value."""
        if not self.find_process():
            return False

        # Hardcoded stamina address
        stamina_address = 0x145A3B90
        return self.write_memory(stamina_address, value)

    def close(self):
        """Close process handle."""
        if self.handle:
            ctypes.windll.kernel32.CloseHandle(self.handle)
            self.handle = None