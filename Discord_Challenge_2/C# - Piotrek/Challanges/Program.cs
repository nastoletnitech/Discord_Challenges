using System;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using DataLibrary;

namespace Challanges
{
    internal static class Program
    {
        private static async Task Main()
        {
            ApiCaller.InitializeClient();
            var rawNames = await ApiCaller.GetNames();
            var names = rawNames.Split(", ");
            Console.WriteLine("Wpisz imię i nazwisko(a): ");
            var fullName = Console.ReadLine() ?? "";
            var name = fullName.Split(' ')[0];
            Console.WriteLine(names.Contains(name)
                ? $"Twoje imię jest dzisiejszym imieniem! Dzisiejsze szczęśliwe imiona, to: {rawNames}"
                : $"Twoje imię nie jest dzisiejszym imieniem :( Dzisiejsze szczęśliwe imiona, to: {rawNames}");
            var regex = new Regex(Regex.Escape(name));
            var surnames = regex.Replace(fullName, "", 1).Replace(" ", "");
            var nickname = User.GetNickname(name, surnames);
            var random = new Random();
            var x = random.Next(1, 10);
            Console.WriteLine($"Witaj {nickname}, podaj wynik pierwiastka z {x}: ");
            CheckSqrt(x);
        }

        private static void Calculator()
        {
            Console.WriteLine("Wpisz, jakie działanie chcesz wynokać:" +
                              $"{Environment.NewLine} 1: Dodawanie" +
                              $"{Environment.NewLine} 2: Odejmowanie" +
                              $"{Environment.NewLine} 3: Mnożenie" +
                              $"{Environment.NewLine} 4: Dzielenie" +
                              $"{Environment.NewLine} 5: Potęga" +
                              $"{Environment.NewLine} 6: Pierwiastek" +
                              $"{Environment.NewLine} Aby wyjść, napisz 'e'");

            var ch = Console.ReadLine();

            try
            {
                var choice = int.Parse(ch ?? "1");
                Console.WriteLine("Wpisz liczbę 1: ");
                var x = double.Parse(Console.ReadLine() ?? "0");
                Console.WriteLine("Wpisz liczbę 2: ");
                var y = double.Parse(Console.ReadLine() ?? "0");
                var result = choice switch
                {
                    1 => DataLibrary.Calculator.Add(x, y),
                    2 => DataLibrary.Calculator.Subtract(x, y),
                    3 => DataLibrary.Calculator.Multiple(x, y),
                    4 => DataLibrary.Calculator.Divide(x, y == 0 ? 1 : y),
                    5 => DataLibrary.Calculator.Power(x, y),
                    6 => DataLibrary.Calculator.Root(x, y),
                    _ => 0
                };
                Console.WriteLine($"Wynik, to {result}. {Environment.NewLine} Aby wyjść, wpisz 'e'. {Environment.NewLine} Aby policzyć coś nowego, wpisz cokolwiek innego!");
                var newChoice = Console.ReadLine();
                if(newChoice == "e") return;
                Calculator();
            }
            catch
            {
                if(ch == "e") return;
                Console.WriteLine("Wpisz poprawną wartość!");
                Calculator();
            }
            
        }

        private static void CheckSqrt(int x)
        {
            var answer = Console.ReadLine() ?? "0";
            
            try
            {
                answer = answer.Replace('.', ',');
                Console.WriteLine(answer);
                var givenNumber = Convert.ToDecimal(answer);
                
                var correct = Convert.ToDecimal(Math.Sqrt(x));
                correct = decimal.Round(correct, 2);

                if (decimal.Equals(givenNumber, correct))
                {
                    Calculator();
                }
                else
                {
                    Console.WriteLine("Źle!");
                    CheckSqrt(x);
                }
            }
            catch
            {
                Console.WriteLine("Wpisz poprawną wartość!");
                CheckSqrt(x);
            }
        }
    }
}
