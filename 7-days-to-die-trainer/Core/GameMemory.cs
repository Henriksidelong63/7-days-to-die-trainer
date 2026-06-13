using System;
using System.Diagnostics;
using Memory;

namespace Trainer.Core
{
    public class GameMemory : IDisposable
    {
        private Mem? _mem;
        private bool _disposed;

        public void AttachToProcess(string processName)
        {
            _mem = new Mem();
            var process = Process.GetProcessesByName(processName);
            if (process.Length == 0)
                throw new InvalidOperationException($"Process '{processName}' not found.");

            _mem.OpenProcess(process[0].Id);
        }

        public void WriteBytes(IntPtr address, byte[] data)
        {
            EnsureAttached();
            _mem!.WriteBytes(address, data);
        }

        public void WriteInt(IntPtr address, int value)
        {
            EnsureAttached();
            _mem!.WriteMemory(address, "int", value.ToString());
        }

        public void WriteFloat(IntPtr address, float value)
        {
            EnsureAttached();
            _mem!.WriteMemory(address, "float", value.ToString());
        }

        private void EnsureAttached()
        {
            if (_mem == null)
                throw new InvalidOperationException("Not attached to process.");
        }

        public void Dispose()
        {
            if (!_disposed)
            {
                _mem?.CloseProcess();
                _mem?.Dispose();
                _disposed = true;
            }
        }
    }
}