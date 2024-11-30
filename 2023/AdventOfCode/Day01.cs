using System.Text.RegularExpressions;

namespace AdventOfCode;

public class Day01 : BaseDay
{
    private readonly string[] _input;

    public Day01()
    {
        _input = [.. File.ReadAllText(InputFilePath).Split('\n')];
    }

    public int CalculateSum()
    {
        var calibrations = _input.Select(x => $"{GetFirstNumber(x)}{GetFirstNumber(new string(x.Reverse().ToArray()))}").ToArray();
        return calibrations.Sum(int.Parse);
    }

    private static string GetFirstNumber(string line)
    {
        return Regex.Match(line, @"\d").ToString();
    }

    public int CalculateSumPart2()
    {
        var calibrations = _input.Select(x => $"{GetFirstNumber(InsertDigitWhereAsString(x))}{GetFirstNumber(new string(InsertDigitWhereAsString(x).Reverse().ToArray()))}").ToArray();
        return calibrations.Sum(int.Parse);
    }

    private static string InsertDigitWhereAsString(string line)
    {
        return line.Replace("one", "one1one")
            .Replace("two", "two2two")
            .Replace("three", "three3three")
            .Replace("four", "four4four")
            .Replace("five", "five5five")
            .Replace("six", "six6six")
            .Replace("seven", "seven7seven")
            .Replace("eight", "eight8eight")
            .Replace("nine", "nine9nine");
    }

    public override ValueTask<string> Solve_1() => new(CalculateSum().ToString());

    public override ValueTask<string> Solve_2() => new(CalculateSumPart2().ToString());
}
