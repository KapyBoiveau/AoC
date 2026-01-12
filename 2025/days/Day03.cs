
namespace _2025.Days
{
    public partial class Day03
    {
        public static void Solution()
        {
            var banks = File.ReadAllLines("input.txt");
            long total = banks.Sum(bank => TurnOnBatteries(bank, 12)); // 12 pour p2, 2 pour p1
            Console.WriteLine($"Total : {total}");
        }

        private static long TurnOnBatteries(string bank, int nbBatteries)
        {
            long total = 0;
            int offset = 0;
            for (int i = nbBatteries; i > 0; i--)
            {
                var (chiffre, index) = GetMaxBattery(bank[offset..(bank.Length-i+1)]);
                total += chiffre * (long)Math.Pow(10, i-1);
                offset += index + 1;
            }
            return total;
        }

        private static (int chiffre, int index) GetMaxBattery(string s)
        {
            return s.Select((carac, index) => (chiffre: carac - '0', index))
                    .MaxBy(x => x.chiffre);
        }
    }
}