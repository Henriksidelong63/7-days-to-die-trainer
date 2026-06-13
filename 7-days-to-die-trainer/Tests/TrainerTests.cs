using System;
using Xunit;
using Trainer.Core;

namespace Trainer.Tests
{
    public class TrainerTests
    {
        [Fact]
        public void MemoryHelper_UnprotectMemory_ReturnsFalse_WhenProcessNull()
        {
            var result = MemoryHelper.UnprotectMemory(IntPtr.Zero, (IntPtr)0x1000, 4);
            Assert.False(result);
        }

        [Fact]
        public void GameMemory_AttachToProcess_Throws_WhenProcessNotFound()
        {
            var memory = new GameMemory();
            Assert.Throws<InvalidOperationException>(() => memory.AttachToProcess("NonExistentProcess"));
        }
    }
}