using System;
using System.Runtime.InteropServices;

namespace Trainer.Core
{
    public static class MemoryHelper
    {
        [DllImport("kernel32.dll")]
        private static extern bool VirtualProtectEx(
            IntPtr hProcess, IntPtr lpAddress,
            uint dwSize, uint flNewProtect,
            out uint lpflOldProtect);

        public static bool UnprotectMemory(IntPtr processHandle, IntPtr address, uint size)
        {
            return VirtualProtectEx(processHandle, address, size, 0x40, out _);
        }
    }
}