namespace AdventOfCode;

public class Day02 : BaseDay
{
    private readonly string[] _lines;

    public Day02()
    {
        _lines = [.. File.ReadAllText(InputFilePath).Split(Environment.NewLine)];
    }

    private int CalculateNumberOfSafeReports()
    {
        int[][] reports = _lines.Select(line => line.Split(' ').Select(int.Parse).ToArray()).ToArray();

        return reports.Where(report => IsIncreasing(report) || IsDecreasing(report)).Count();
    }

    private static bool IsIncreasing(int[] array)
    {
        return array.Zip(array.Skip(1), (a, b) => (a < b) && ((b - a) <= 3)).All(x => x);
    }

    private static bool IsDecreasing(int[] array)
    {
        return array.Zip(array.Skip(1), (a, b) => (a > b) && ((a - b) <= 3)).All(x => x);
    }

    private int CalculateNumberOfSafeReportsWithProblemDampener()
    {
        int[][] reports = _lines.Select(line => line.Split(' ').Select(int.Parse).ToArray()).ToArray();

        var unsafeReports = reports.Where(report => !IsIncreasing(report) || !IsDecreasing(report)).ToArray();
        var safeReportsCount = reports.Length - unsafeReports.Length;

        foreach (var report in unsafeReports)
        {
            for (var i = 0; i < report.Length; i++)
            {
                var adjustedReport = report.Where((_, index) => index != i).ToArray();
                if (IsIncreasing(adjustedReport) || IsDecreasing(adjustedReport))
                {
                    safeReportsCount++;
                    break;
                }
            }
        }

        return safeReportsCount;
    }

    public override ValueTask<string> Solve_1() => new(CalculateNumberOfSafeReports().ToString());

    public override ValueTask<string> Solve_2() => new(CalculateNumberOfSafeReportsWithProblemDampener().ToString());
}
