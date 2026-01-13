
namespace _2025.Days
{
    public partial class Day06
    {
        public static void Solution()
        {
            var lines = File.ReadAllLines("input.txt");

            var numbers = lines[..^1]
                .Select(line => line.Split(' ',StringSplitOptions.RemoveEmptyEntries)
                    .Select(long.Parse)
                    .ToArray())
                .ToArray();

            var operators = lines[^1]
                .Split(' ',StringSplitOptions.RemoveEmptyEntries);

            long total = operators.Select((op, i) => numbers
                    .Select(row => row[i])
                    .Aggregate((a, b) => op == "+" ? a + b : a * b))
                .Sum();
            
            Console.WriteLine($"Total : {total}");
        }
    }
}