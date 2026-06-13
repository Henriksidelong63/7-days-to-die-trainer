using System;
using System.Threading;
using Trainer.Core;

namespace Trainer
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("7 Days to Die Trainer v1.0");
            Console.WriteLine("--------------------------");
            Console.WriteLine("Commands: god, ammo, speed, exit");

            using var memory = new GameMemory();
            memory.AttachToProcess("7DaysToDie");

            string? input;
            while ((input = Console.ReadLine()?.ToLower()) != "exit")
            {
                switch (input)
                {
                    case "god":
                        memory.WriteBytes(0x00400000 + 0x1234, new byte[] { 0x90, 0x90 });
                        Console.WriteLine("God mode activated.");
                        break;
                    case "ammo":
                        memory.WriteInt(0x00400000 + 0x5678, 999);
                        Console.WriteLine("Ammo set to 999.");
                        break;
                    case "speed":
                        memory.WriteFloat(0x00400000 + 0x9ABC, 2.5f);
                        Console.WriteLine("Movement speed increased.");
                        break;
                    default:
                        Console.WriteLine("Unknown command.");
                        break;
                }
            }
        }
    }
}