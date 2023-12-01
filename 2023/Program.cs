// https://github.com/eduherminio/AdventOfCode.Template
// By default, only your last problem will be solved when running the project. You can change that by behavior by modifying Program.cs.
// Invoking different methods:

//     Solver.SolveAll(); → solves all the days.
//     Solver.SolveLast(); → solves only the last day.
//     Solver.Solve<Day_XX>(); → solves only day XX.
//     Solver.Solve(new uint[] { XX, YY }); → solves only days XX and YY.
//     Solver.Solve(new [] { typeof(Day_XX), typeof(Day_YY) }); → same as above.

if (args.Length == 0)
{
    await Solver.SolveLast(opt => opt.ClearConsole = false);
}
else if (args.Length == 1 && args[0].Contains("all", StringComparison.CurrentCultureIgnoreCase))
{
    await Solver.SolveAll(opt =>
    {
        opt.ShowConstructorElapsedTime = true;
        opt.ShowTotalElapsedTimePerDay = true;
    });
}
else
{
    var indexes = args.Select(arg => uint.TryParse(arg, out var index) ? index : uint.MaxValue);

    await Solver.Solve(indexes.Where(i => i < uint.MaxValue));
}
