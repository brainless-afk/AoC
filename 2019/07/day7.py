import itertools

with open('input') as file:
    array = list(map(int, file.read().split(',')))


def modus_operandi(position, mode):
    if int(mode) == 0:
        return array[array[position]]
    return array[position]


def calc_intcode(in_phase, in_signal):
    pos_zero = 0
    pad_zeroes = f"{array[pos_zero]:05d}"
    opcode = int(pad_zeroes[-2:])
    mode3, mode2, mode1 = pad_zeroes[:-2]
    phase = True
    out = 0

    while opcode != 99:
        if opcode == 1:
            array[array[pos_zero + 3]] = modus_operandi(pos_zero + 1, mode1) + \
                                         modus_operandi(pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 2:
            array[array[pos_zero + 3]] = modus_operandi(pos_zero + 1, mode1) * \
                                         modus_operandi(pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 3:
            array[array[pos_zero + 1]] = in_phase if phase else in_signal
            phase = False
            pos_zero += 2
        elif opcode == 4:
            out = modus_operandi(pos_zero + 1, mode1)
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
                array[array[pos_zero + 3]] = 1
            else:
                array[array[pos_zero + 3]] = 0
            pos_zero += 4
        elif opcode == 8:
            if modus_operandi(pos_zero + 1, mode1) == modus_operandi(pos_zero + 2, mode2):
                array[array[pos_zero + 3]] = 1
            else:
                array[array[pos_zero + 3]] = 0
            pos_zero += 4
        else:
            print("Opcode: ", opcode, " Position: ", pos_zero)
            return "Error"
        pad_zeroes = f"{array[pos_zero]:05d}"
        opcode = int(pad_zeroes[-2:])
        mode3, mode2, mode1 = pad_zeroes[:-2]

    return out


phase_settings = list(itertools.permutations((range(0, 5))))
best = 0
sequence = []
for setting in phase_settings:
    setting = list(setting)
    s = setting
    start_input = 0
    for amp in range(5):
        start_input = calc_intcode(setting[amp], start_input)
        sequence = s
    if start_input > best:
        best = start_input

print("Highest signal: ", best)
print("Sequence: ", sequence)
