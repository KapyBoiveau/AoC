
namespace _2025.Days
{
    public partial class Day04
    {
        public static void Solution()
        {
            int total = 0;
            List<(int,int)> subtotal;
            char[][] grid = File.ReadAllLines("input.txt")
                                .Select(ligne => ligne.ToCharArray())
                                .ToArray();
            do
            {
                subtotal = [];
                for (int y = 0; y < grid.Length; y++)
                {
                    for (int x = 0; x < grid[y].Length; x++)
                    {
                        if (grid[y][x] == '@')
                        {
                            var pos = CheckNeighbours(grid, y, x);
                            if (pos != (-1, -1))
                                subtotal.Add(pos);
                        }                            
                    }
                }
                total += subtotal.Count;
                foreach(var (y,x) in subtotal)
                    grid[y][x] = '.';
                
            } while (subtotal.Count > 0);
            Console.WriteLine($"Total : {total}");
        }

        private static (int, int) CheckNeighbours(char[][] grid, int y, int x)
        {
            int nbRolls = 0;
            for (int dy = -1; dy <= 1; dy++)
            {
                for (int dx = -1; dx <= 1; dx++)
                {
                    if (dx == 0 && dy == 0) continue;
                    if (x+dx < 0 || x+dx >= grid[0].Length || y+dy < 0 || y+dy >= grid.Length) continue;
                    if (grid[y+dy][x+dx] == '@')        
                        nbRolls += 1;
                }
            }
            return nbRolls < 4 ? (y, x) : (-1, -1);
        }
    }
}