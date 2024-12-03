using System.Text.RegularExpressions;

namespace AdventOfCode;

public class Day03 : BaseDay
{
    private readonly string _input;

    public Day03()
    {
        _input = File.ReadAllText(InputFilePath);
    }

    private MatchCollection FindMultiplications()
    {
        string pattern = @"mul\((\d{1,3}),(\d{1,3})\)";
        return Regex.Matches(_input, pattern);
    }

    private int FixCorruptedMemory()
    {
        var validMultiplications = FindMultiplications();
        return validMultiplications.Select(match => int.Parse(match.Groups[1].Value) * int.Parse(match.Groups[2].Value)).Sum();
    }

    private List<Match> FindEnabledMultiplications()
    {
        string pattern = @"mul\((\d{1,3}),(\d{1,3})\)";

        return _input.Split("do()")
            .Select(x => x.Split("don't()")[0])
            .SelectMany(x => Regex.Matches(x, pattern)).ToList();
    }

    private int FixConditionalCorruptedMemory()
    {
        var validOperations = FindEnabledMultiplications();
        return validOperations.Select(match => int.Parse(match.Groups[1].Value) * int.Parse(match.Groups[2].Value)).Sum();
    }

    public override ValueTask<string> Solve_1() => new(FixCorruptedMemory().ToString());

    public override ValueTask<string> Solve_2() => new(FixConditionalCorruptedMemory().ToString());
}
