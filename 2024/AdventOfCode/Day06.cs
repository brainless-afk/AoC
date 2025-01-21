namespace AdventOfCode;

public class Day06 : BaseDay
{
    private const char obstacle = '#';
    private const char positionMarker = 'X';
    private const char startingPosition = '^';

    private readonly char[][] _lines;

    enum Direction
    {
        North = 0,
        East = 1,
        South = 2,
        West = 3
    }

    public Day06()
    {
        _lines = [.. File.ReadAllText(InputFilePath).Split(Environment.NewLine).Select(l => l.ToCharArray()).ToArray()];
    }

    private int Part1()
    {
        (int xPosition, int yPosition) = FindStartingPosition(_lines);
        MarkPosition(xPosition, yPosition);
        int distinctPositions = 1;
        Direction direction = Direction.North;

        (int nextX, int nextY) = GetNextPosition(xPosition, yPosition, direction);
        while (nextY < _lines.Length && nextX < _lines[0].Length)
        {

            while (_lines[nextY][nextX].Equals(obstacle))
            {
                direction = GetNextDirection(direction);
                (nextX, nextY) = GetNextPosition(xPosition, yPosition, direction);
            }

            xPosition = nextX;
            yPosition = nextY;

            if (_lines[nextY][nextX] != positionMarker) // Ignore if already visited
            {
                MarkPosition(xPosition, yPosition);
                distinctPositions++;
            }

            (nextX, nextY) = GetNextPosition(xPosition, yPosition, direction);

        }

        //PrintMap();
        return distinctPositions;
    }

    private void MarkPosition(int x, int y)
    {
        _lines[y][x] = positionMarker;
    }

    private static (int, int) GetNextPosition(int xPosition, int yPosition, Direction direction)
    {
        return direction switch
        {
            Direction.North => (xPosition, yPosition - 1),// Move up
            Direction.East => (xPosition + 1, yPosition),// Move right
            Direction.South => (xPosition, yPosition + 1),// Move down
            Direction.West => (xPosition - 1, yPosition),// Move left
            _ => throw new ArgumentOutOfRangeException(nameof(direction), "Invalid direction"),
        };
    }

    private static Direction GetNextDirection(Direction direction)
    {
        // Increment and cycle through enum values
        return (Direction)(((int)direction + 1) % Enum.GetValues<Direction>().Length);
    }

    private void PrintMap()
    {
        foreach (var line in _lines)
        {
            Console.WriteLine(line);
        }
    }

    private static (int, int) FindStartingPosition(char[][] charArray)
    {

        for (int y = 0; y < charArray.Length; y++)
        {
            for (int x = 0; x < charArray[y].Length; x++)
            {
                if (charArray[y][x].Equals(startingPosition))
                {
                    return (x, y);
                }
            }
        }

        throw new Exception($"Character '{startingPosition}' not found.");
    }

    public override ValueTask<string> Solve_1() => new(Part1().ToString());

    public override ValueTask<string> Solve_2() => new("Part1().ToString()");
}