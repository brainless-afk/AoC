namespace AdventOfCode;

public class Day02 : BaseDay
{
    private readonly string[] _lines;

    public Day02()
    {
        _lines = [.. File.ReadAllText(InputFilePath).Split('\n')];
    }

    private static int GetIdIfGamePossible(string game)
    {
        string id = game.Split(':')[0].Split(' ')[1];
        string[] subsets = game.Substring(game.IndexOf(':') + 1).Split(';');

        foreach (string subset in subsets)
        {
            var colorCounts = ParseSubSet(subset);

            if (colorCounts["red"] > 12 || colorCounts["green"] > 13 || colorCounts["blue"] > 14)
            {
                return 0;
            }
        }

        return int.Parse(id);
    }

    private static Dictionary<string, int> ParseSubSet(string subset)
    {
        string[] coloredCubes = subset.Split(",", StringSplitOptions.TrimEntries);

        var colorCounts = new Dictionary<string, int>() { { "red", 0 }, { "green", 0 }, { "blue", 0 } };
        foreach (string c in coloredCubes)
        {
            string[] parts = c.Split(' ');

            colorCounts[parts[1]] = int.Parse(parts[0]);
        }

        return colorCounts;
    }

    private int Part1()
    {
        return _lines.Select(GetIdIfGamePossible).Sum();
    }

    private static int GetMinColorSum(string game)
    {
        string[] subsets = game.Substring(game.IndexOf(':') + 1).Split(';');

        var dicts = subsets.Select(ParseSubSet).ToList();

        int red = dicts.Select(colorDict => colorDict["red"] | 0).Max();
        int green = dicts.Select(colorDict => colorDict["green"] | 0).Max();
        int blue = dicts.Select(colorDict => colorDict["blue"] | 0).Max();

        return red * green * blue;
    }

    private int Part2()
    {
        return _lines.Select(GetMinColorSum).Sum();
    }

    public override ValueTask<string> Solve_1() => new(Part1().ToString());

    public override ValueTask<string> Solve_2() => new(Part2().ToString());
}
