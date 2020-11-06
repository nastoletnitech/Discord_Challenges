using System.Collections.Generic;
using System.Linq;

namespace DataLibrary
{
    public static class User
    {
        public static string GetNickname(string name, string surnames)
        {
            name = FromUtf8(name);
            return (name.Length > 1 ? name.Remove(1).ToUpper() : name.ToUpper()) + (surnames.Length > 1 ? FormatSurnames(surnames.ToLower()) : surnames.ToUpper());
        }

        private static string FormatSurnames(string surnames)
        {
            surnames = FromUtf8(surnames);
            var firstLetter = surnames[0].ToString().ToUpper();
            return firstLetter + (surnames.Length > 1 ? surnames.Remove(0, 1) : firstLetter);
        }

        private static string FromUtf8(string text)
        {
            var polishLetters = new List<char> {'ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż'};
            var normalLetters = new List<char> {'a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z'};
            return polishLetters.Aggregate(text, (current, polishLetter)
                => current.Replace(polishLetter.ToString(),
                    normalLetters[polishLetters.IndexOf(polishLetter)].ToString()
                    )
                );
        }
    }
}