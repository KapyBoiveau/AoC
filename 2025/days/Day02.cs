
using System.Text.RegularExpressions;

namespace _2025.Days
{
    public partial class Day02
    {
        public static void Solution()
        {
            string input = File.ReadAllText("input.txt");
            var ranges = MyRegex().Matches(input)
                .Select(m => (m.Groups[1].Value, m.Groups[2].Value))
                .ToList();

            long total = 0;
            foreach (var (start, end) in ranges)
            {
                total += CalculateRangeSum(start, end);
            }
            Console.WriteLine($"Total : {total}");
        }

        private static long CalculateRangeSum(string start, string end)
        {
            AdjustToEvenLength(ref start, ref end);

            int halfStartLength = start.Length / 2;
            int halfEndLength = end.Length / 2;

            long leftStart = long.Parse(start[..halfStartLength]);
            long rightStart = long.Parse(start[halfStartLength..]);
            long leftEnd = long.Parse(end[..halfEndLength]);
            long rightEnd = long.Parse(end[halfEndLength..]);

            List<long> results = [];

            for (long n = leftStart; n <= leftEnd; n++)
            {
                int shift = (int)Math.Log10(n) - (int)Math.Log10(leftStart); // shift utile si End a plus de chiffres que Start
                results.Add(n * (long)Math.Pow(10, halfStartLength + shift) + n); // on double le nombre sans string
            }

            if (rightStart > leftStart && results.Count > 0) results.RemoveAt(0); // le premier est invalide
            if (rightEnd < leftEnd && results.Count > 0) results.RemoveAt(results.Count - 1); // le dernier est invalide
            
            return results.Sum();
        }

        private static void AdjustToEvenLength(ref string start, ref string end)
        {
            if (start.Length % 2 == 1)
            {
                start = ((long)Math.Pow(10, start.Length)).ToString();
            }
            if (end.Length % 2 == 1)
            {
                end = ((long)Math.Pow(10, end.Length - 1) - 1).ToString();
            }
        }

        [GeneratedRegex(@"(\d+)-(\d+)")]
        private static partial Regex MyRegex();
    }
}