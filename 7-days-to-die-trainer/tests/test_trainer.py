import unittest
from unittest.mock import patch, MagicMock
from trainer import SevenDaysTrainer

class TestSevenDaysTrainer(unittest.TestCase):
    @patch('trainer.ctypes')
    def test_find_process_success(self, mock_ctypes):
        trainer = SevenDaysTrainer()
        mock_ctypes.windll.kernel32.Process32First.return_value = True
        mock_ctypes.windll.kernel32.Process32Next.return_value = False

        with patch.object(trainer, 'process_name', 'test.exe'):
            process_entry = MagicMock()
            process_entry.szExeFile = b'test.exe'
            process_entry.th32ProcessID = 1234
            mock_ctypes.create_string_buffer.return_value = process_entry

            result = trainer.find_process()
            self.assertTrue(result)
            self.assertEqual(trainer.process_id, 1234)

    @patch('trainer.ctypes')
    def test_find_process_failure(self, mock_ctypes):
        trainer = SevenDaysTrainer()
        mock_ctypes.windll.kernel32.Process32First.return_value = False

        result = trainer.find_process()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()