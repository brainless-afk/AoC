namespace AdventOfCode;

public class Day01 : BaseDay
{
    private readonly string[] _lines;

    public Day01()
    {
        _lines = [.. File.ReadAllText(InputFilePath).Split(Environment.NewLine)];
    }

    private (List<int>, List<int>) ParseInputToLists()
    {
        var leftIds = new List<int>();
        var rightIds = new List<int>();

        foreach (var line in _lines)
        {
            string[] numbers = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);

            leftIds.Add(int.Parse(numbers[0]));
            rightIds.Add(int.Parse(numbers[1]));
        }

        leftIds.Sort();
        rightIds.Sort();

        return (leftIds, rightIds);
    }

    private int CalculateTotalDistanceOfIds()
    {
        var (leftIds, rightIds) = ParseInputToLists();

        int totalDistance = 0;
        for (int i = 0; i < leftIds.Count; i++)
        {
            int distance = Math.Abs(leftIds[i] - rightIds[i]);
            totalDistance += distance;
        }

        return totalDistance;
    }

    private int CalculateSimularityOfIds()
    {
        var (leftIds, rightIds) = ParseInputToLists();

        var rightIdCounts = rightIds.CountBy(id => id).ToDictionary();

        return leftIds.Sum(leftId => leftId * rightIdCounts.GetValueOrDefault(leftId));
    }

    public override ValueTask<string> Solve_1() => new(CalculateTotalDistanceOfIds().ToString());

    public override ValueTask<string> Solve_2() => new(CalculateSimularityOfIds().ToString());
}
