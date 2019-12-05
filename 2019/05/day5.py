with open('input') as file:
    gravity_assist_program = file.read()
    gravity_assist_program = [int(s) for s in gravity_assist_program.split(',')]


def modus_operandi(position, mode):
    if int(mode) == 0:
        return gravity_array[gravity_array[position]]
    return gravity_array[position]


def calculate_value():
    pos_zero = 0
    pad_zeroes = f"{gravity_array[pos_zero]:05d}"
    opcode = int(pad_zeroes[-2:])
    mode3, mode2, mode1 = pad_zeroes[:-2]

    while opcode != 99:
        if opcode == 1:
            gravity_array[gravity_array[pos_zero + 3]] = modus_operandi(pos_zero + 1, mode1) + \
                                                         modus_operandi(pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 2:
            gravity_array[gravity_array[pos_zero + 3]] = modus_operandi(pos_zero + 1, mode1) * \
                                                         modus_operandi(pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 3:
            gravity_array[gravity_array[pos_zero + 1]] = int(input("Input: "))
            pos_zero += 2
        elif opcode == 4:
            print("Output: ", modus_operandi(pos_zero + 1, mode1))
            pos_zero += 2
        elif opcode == 5:
            if not modus_operandi(pos_zero + 1, mode1) == 0:
                pos_zero = modus_operandi(pos_zero + 2, mode2)
            else:
                pos_zero += 3
        elif opcode == 6:
            if modus_operandi(pos_zero + 1, mode1) == 0:
                pos_zero = modus_operandi(pos_zero + 2, mode2)
            else:
                pos_zero += 3
        elif opcode == 7:
            if modus_operandi(pos_zero + 1, mode1) < modus_operandi(pos_zero + 2, mode2):
                gravity_array[gravity_array[pos_zero + 3]] = 1
            else:
                gravity_array[gravity_array[pos_zero + 3]] = 0
            pos_zero += 4
        elif opcode == 8:
            if modus_operandi(pos_zero + 1, mode1) == modus_operandi(pos_zero + 2, mode2):
                gravity_array[gravity_array[pos_zero + 3]] = 1
            else:
                gravity_array[gravity_array[pos_zero + 3]] = 0
            pos_zero += 4
        else:
            print("Error in Thermal Environment Supervision Terminal!")
            print("Opcode: ", opcode, " Position: ", pos_zero)
            return
        pad_zeroes = f"{gravity_array[pos_zero]:05d}"
        opcode = int(pad_zeroes[-2:])
        mode3, mode2, mode1 = pad_zeroes[:-2]

    return "Success"


gravity_array = gravity_assist_program[:]
result = calculate_value()
print("Final Output: ", result)
