namespace AdventOfCode;

public class Day05 : BaseDay
{
    private readonly string _input;

    public Day05()
    {
        _input = File.ReadAllText(InputFilePath);
    }

    #region Part 1

    private int PrintQueueCheck()
    {
        var (pageOrderingRules, pagesToProduce) = ParseInput();
        int count = 0;

        foreach (var page in pagesToProduce)
        {
            bool isOrdererCorrectly = true;
            for (int i = page.Count - 1; i > 0 && isOrdererCorrectly; i--)
            {
                if (pageOrderingRules.TryGetValue(page[i], out List<string> forbidden))
                {
                    var forbiddenSet = new HashSet<string>(forbidden);

                    for (int j = i - 1; j >= 0; j--)
                    {
                        if (forbiddenSet.Contains(page[j]))
                        {
                            isOrdererCorrectly = false;
                            break;
                        }
                    }
                }
            }

            if (isOrdererCorrectly)
            {
                int middleIndex = page.Count / 2;
                count += int.Parse(page[middleIndex]);
            }
        }

        return count;
    }

    #endregion Part 1

    #region Part 2

    private int FixIncorrectOrders()
    {
        var (pageOrderingRules, pagesToProduce) = ParseInput();
        var forbiddenCache = pageOrderingRules.ToDictionary(
            kvp => kvp.Key,
            kvp => new HashSet<string>(kvp.Value)
        );

        int count = 0;

        foreach (var page in pagesToProduce)
        {
            bool isOrdererCorrectly = true;
            for (int i = page.Count - 1; i > 0; i--)
            {
                if (forbiddenCache.TryGetValue(page[i], out var forbiddenSet))
                {
                    bool itemWasMoved = false;

                    for (int j = 0; j < i; j++)
                    {
                        if (forbiddenSet.Contains(page[j]))
                        {
                            MoveItem(page, i, j);
                            isOrdererCorrectly = false;
                            itemWasMoved = true;
                            break;
                        }
                    }

                    if (itemWasMoved) i++;
                }
            }

            if (!isOrdererCorrectly)
            {
                int middleIndex = page.Count / 2;
                count += int.Parse(page[middleIndex]);
            }
        }

        return count;
    }

    #endregion Part 2

    private (Dictionary<string, List<string>>, List<List<string>>) ParseInput()
    {
        var (pageOrderingRules, pagesToProduce) = _input.Split(Environment.NewLine + Environment.NewLine) switch { var a => (a[0], a[1]) };

        var pageOrderingDict = pageOrderingRules.Split(Environment.NewLine).Select(x => x.Split('|')).GroupBy(x => x[0], x => x[1]).ToDictionary(y => y.Key, y => y.ToList());
        var pagesToProduceList = pagesToProduce.Split(Environment.NewLine).Select(x => x.Split(',').ToList()).ToList();

        return (pageOrderingDict, pagesToProduceList);
    }

    private static void MoveItem(List<string> list, int oldIndex, int newIndex)
    {
        string item = list[oldIndex];
        list.RemoveAt(oldIndex);
        list.Insert(newIndex, item);
    }

    public override ValueTask<string> Solve_1() => new(PrintQueueCheck().ToString());

    public override ValueTask<string> Solve_2() => new(FixIncorrectOrders().ToString());
}