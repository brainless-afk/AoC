with open('input') as file:
    gravity_assist_program = file.read()
    gravity_assist_program = [int(s) for s in gravity_assist_program.split(',')]


def calculate_value(gravity_array, noun, verb):
    gravity_array[1] = noun
    gravity_array[2] = verb
    pos_zero = 0
    opcode = gravity_array[pos_zero]

    while opcode != 99:
        if opcode == 1:
            gravity_array[gravity_array[pos_zero + 3]] = gravity_array[gravity_array[pos_zero + 1]] + \
                                                         gravity_array[gravity_array[pos_zero + 2]]
        elif opcode == 2:
            gravity_array[gravity_array[pos_zero + 3]] = gravity_array[gravity_array[pos_zero + 1]] * \
                                                         gravity_array[gravity_array[pos_zero + 2]]
        else:
            print("Hello, Intcode?")
            print("Intcode machine broke")
            print("Understandable, have a nice day")
            return "Error"
        pos_zero += 4
        opcode = gravity_array[pos_zero]

    return gravity_array[0]


# Part 1
result = calculate_value(gravity_assist_program[:], 12, 2)
print("Value at position 0: ", result)


# Part 2
def part2(gravity_array):
    desired_output = 19690720

    for n in range(100):
        for v in range(100):
            array = gravity_array[:]
            if calculate_value(array, n, v) == desired_output:
                print("Noun: ", n)
                print("Verb; ", v)
                print("100 * noun + verb = ", 100 * n + v)
                return


part2(gravity_assist_program)
