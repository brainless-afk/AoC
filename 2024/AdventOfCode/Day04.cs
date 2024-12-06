namespace AdventOfCode;

public class Day04 : BaseDay
{
    private readonly string[] _lines;

    public Day04()
    {
        _lines = [.. File.ReadAllText(InputFilePath).Split(Environment.NewLine)];
    }

    #region Part 1

    private int XmasWordSearch()
    {
        var diagonalTextsLeftToRight = GetTextFromDiagonalsLeftToRight(_lines);
        var diagonalTextsRightToLeft = GetTextFromDiagonalsLeftToRight(_lines.Select(line => string.Concat(line.Reverse().ToArray())).ToArray());
        var verticalTexts = GetTextsFromVertical(_lines);

        var allPossibleTexts = _lines
            .Concat(diagonalTextsLeftToRight)
            .Concat(diagonalTextsRightToLeft)
            .Concat(verticalTexts);

        var wordCount = 0;
        foreach (var line in allPossibleTexts)
        {
            wordCount += CountWordInString(line, "XMAS");
            wordCount += CountWordInString(line, "SAMX");
        }

        return wordCount;
    }

    private static List<string> GetTextFromDiagonalsLeftToRight(string[] lines)
    {
        List<string> texts = [];

        // Get all diagonal texts from first line
        foreach (var (columnIndex, letter) in lines[0].Index())
        {
            List<char> text = [letter];
            int rowIndex = 1;

            for (var i = columnIndex + 1; i < lines.Length; i++)
            {
                text.Add(lines[rowIndex][i]);
                rowIndex++;
            }

            texts.Add(string.Concat(text));
        }

        // Get diagonal text from first index of each row
        foreach (var (index, line) in lines.Skip(1).Index())
        {
            List<char> text = [];

            for (var i = 0; i < line.Length; i++)
            {
                // +1 because skipping the first line
                var rowIndex = index + i + 1;
                if (rowIndex >= lines.Length) break;

                text.Add(lines[rowIndex][i]);
            }

            texts.Add(string.Concat(text));
        }

        return texts;
    }

    private static List<string> GetTextsFromVertical(string[] lines)
    {
        List<string> texts = [];

        foreach (var (columnIndex, _) in lines[0].Index())
        {
            List<char> text = [];

            for (var i = 0; i < lines.Length; i++)
            {
                text.Add(lines[i][columnIndex]);
            }

            texts.Add(string.Concat(text));
        }

        return texts;
    }

    private static int CountWordInString(string line, string wordToSearch)
    {
        if (string.IsNullOrEmpty(line) || string.IsNullOrEmpty(wordToSearch))
            return 0;

        int count = 0;
        int index = 0;

        while ((index = line.IndexOf(wordToSearch, index, StringComparison.OrdinalIgnoreCase)) != -1)
        {
            count++;
            index += wordToSearch.Length;
        }

        return count;

        // Regex is very slow
        //return Regex.Matches(line, wordToSearch, RegexOptions.IgnoreCase).Count;
    }

    #endregion

    #region Part 2
    private int CrossMasWordSearch()
    {
        int count = 0;

        foreach (var (rowIndex, line) in _lines.Index())
        {
            // Cant have a cross at the edge
            if (rowIndex != 0 && rowIndex != _lines.Length - 1)
            {
                int columnIndex = 0;

                while ((columnIndex = line.IndexOf('A', columnIndex)) != -1)
                {
                    // Cant have a cross at the edge
                    if (columnIndex != 0 && columnIndex != line.Length - 1 && HasMSNeighbors(rowIndex, columnIndex))
                    {
                        count++;
                    }

                    columnIndex++;
                }
            }
        }

        return count;
    }

    private bool HasMSNeighbors(int rowIndex, int columnIndex)
    {
        char[] crossTopLeftBottomRight = [_lines[rowIndex - 1][columnIndex - 1], _lines[rowIndex + 1][columnIndex + 1]];
        char[] crossTopRightBottomLeft = [_lines[rowIndex - 1][columnIndex + 1], _lines[rowIndex + 1][columnIndex - 1]];
        char[] desiredResult = ['M', 'S'];

        return crossTopLeftBottomRight.Order().SequenceEqual(desiredResult) && crossTopRightBottomLeft.Order().SequenceEqual(desiredResult);
    }

    #endregion

    public override ValueTask<string> Solve_1() => new(XmasWordSearch().ToString());

    public override ValueTask<string> Solve_2() => new(CrossMasWordSearch().ToString());
}
