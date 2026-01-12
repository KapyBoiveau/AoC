
namespace _2025.Days
{
    public partial class Day05
    {
        public static void Solution()
        {
            var database = File.ReadAllText("input.txt")
                .Split("\r\n\r\n");

            var ranges = database[0]
                .Split("\r\n")
                .Select(s => s.Split('-'))
                .Select(p => (start: long.Parse(p[0]), end:long.Parse(p[1])))
                .OrderBy(p => p.start) // utile pour les intersections
                .ToArray();

            var ids = database[1]
                .Split("\r\n")
                .Select(long.Parse);

            ManageIntersections(ref ranges);

            int freshIDs = ids.Count(id => ranges.Any(r => id >= r.start && id <= r.end));
            long allFreshIDs = ranges.Sum(r => r.end - r.start + 1);
            
            foreach(var (start, end) in ranges)
            {
                Console.WriteLine($"{end} - {start} = {end-start+1}");
            }
            Console.WriteLine($"Total : {allFreshIDs}");
        }

        private static void ManageIntersections(ref (long start, long end)[] ranges)
        {
            for (int i = 1; i < ranges.Length; i++)
            {
                if (ranges[i].start <= ranges[i-1].end)
                    ranges[i].start = ranges[i-1].end + 1;
            }
        }
    }
}