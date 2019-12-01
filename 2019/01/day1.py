def calculate_fuel(mass):
    return (int(mass) // 3) - 2


with open('input') as fp:
    required_fuel = 0
    total_fuel = 0

    for line in fp:
        module_fuel = calculate_fuel(line)
        required_fuel += module_fuel
        while module_fuel > 0:
            total_fuel += module_fuel
            module_fuel = calculate_fuel(module_fuel)

    print("Part 1: Required fuel: ", required_fuel)
    print("Part 2: Total fuel: ", total_fuel)
