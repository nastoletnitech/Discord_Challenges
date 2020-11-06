using System;

namespace Discord_Challenge1
{
	class Program
	{
		static void Main(string[] args)
		{
			void restart()
			{
				System.Diagnostics.Process.Start(System.AppDomain.CurrentDomain.FriendlyName);
				Environment.Exit(0);
			}
			Console.Write("Wpisz Imię: ");
			string Name;
			Name = Console.ReadLine();
			if(Name.Length > 13 || Name.Length < 3)
			{
				Console.WriteLine("Niepoprawne Imię.");
				restart();
			}
			else
			{
				if (Name.EndsWith("a") || Name.EndsWith("A"))
				{
					if (Name == "Kuba" || Name == "kuba" || Name == "KubA" || Name == "kubA")
					{
						Console.WriteLine("Podane imie jest męskie");
					}
					else
					{
						Console.WriteLine("Podane imie jest żeńskie.");
					}
					restart();
				}
				else
				{
					Console.WriteLine("Podane imie jest męskie");
					restart();
				}
			}
		}
	}
}
