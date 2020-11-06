using System;

namespace Challanges
{
    internal static class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("Wpisz imię: ");
            var name = Console.ReadLine() ?? "";
            var nameLength = name.Length;
            var lastLetterA = name.EndsWith('a') || name.EndsWith('A');
            if (nameLength < 3 || nameLength > 13)
            {
                Console.WriteLine("Nie jest to poprawne imię!");
                return;
            }
            const string kuba = "Kuba";
            if (string.Equals(name, kuba, StringComparison.CurrentCultureIgnoreCase) && lastLetterA)
            {
                Console.WriteLine("Męskie imię!");
                return;
            }
            if (!lastLetterA)
            {
                Console.WriteLine("Męskie imię!");
                return;
            }
            Console.WriteLine("Żeńskie imię!");
        }
    }
}