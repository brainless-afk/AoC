import itertools

with open('input') as file:
    arr_in = list(map(int, file.read().split(',')))


def modus_operandi(arr, position, mode):
    if int(mode) == 0:
        return arr[arr[position]]
    return arr[position]


def calc_intcode(array, in_phase, in_signal, phase=True, pos_zero=0):
    pad_zeroes = f"{array[pos_zero]:05d}"
    opcode = int(pad_zeroes[-2:])
    mode3, mode2, mode1 = pad_zeroes[:-2]
    out = 0
    fin = False

    while opcode != 99:
        if opcode == 1:
            array[array[pos_zero + 3]] = modus_operandi(array, pos_zero + 1, mode1) + \
                                         modus_operandi(array, pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 2:
            array[array[pos_zero + 3]] = modus_operandi(array, pos_zero + 1, mode1) * \
                                         modus_operandi(array, pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 3:
            if phase:
                array[array[pos_zero + 1]] = in_phase
                phase = False
            else:
                array[array[pos_zero + 1]] = in_signal
            pos_zero += 2
        elif opcode == 4:
            out = modus_operandi(array, pos_zero + 1, mode1)
            pos_zero += 2
            return array[:], out, pos_zero, phase, fin
        elif opcode == 5:
            if not modus_operandi(array, pos_zero + 1, mode1) == 0:
                pos_zero = modus_operandi(array, pos_zero + 2, mode2)
            else:
                pos_zero += 3
        elif opcode == 6:
            if modus_operandi(array, pos_zero + 1, mode1) == 0:
                pos_zero = modus_operandi(array, pos_zero + 2, mode2)
            else:
                pos_zero += 3
        elif opcode == 7:
            if modus_operandi(array, pos_zero + 1, mode1) < modus_operandi(array, pos_zero + 2, mode2):
                array[array[pos_zero + 3]] = 1
            else:
                array[array[pos_zero + 3]] = 0
            pos_zero += 4
        elif opcode == 8:
            if modus_operandi(array, pos_zero + 1, mode1) == modus_operandi(array, pos_zero + 2, mode2):
                array[array[pos_zero + 3]] = 1
            else:
                array[array[pos_zero + 3]] = 0
            pos_zero += 4
        else:
            raise Exception("opcode error")

        pad_zeroes = f"{array[pos_zero]:05d}"
        opcode = int(pad_zeroes[-2:])
        mode3, mode2, mode1 = pad_zeroes[:-2]

    fin = True
    return array, out, pos_zero, phase, fin


phase_settings = list(itertools.permutations((range(5, 10))))
best = 0
sequence = []

for setting in phase_settings:
    setting = list(setting)
    s = setting
    amps_count = len(setting)
    start_input = 0
    last_output = [0] * amps_count
    finished = False
    pos_list = [0] * amps_count
    phase_list = [True] * amps_count
    arr = [arr_in[:]] * amps_count

    while not finished:
        for amp in range(amps_count):
            arr[amp], start_input, pos_list[amp], phase_list[amp], finished = calc_intcode(arr[amp], setting[amp],
                                                                                             start_input,
                                                                                             phase_list[amp],
                                                                                             pos_list[amp])
            if finished:
                if last_output[amp] > best:
                    best = last_output[amp]
                    sequence = s
            last_output[amp] = start_input

print("Highest signal: ", best)
print("Sequence: ", sequence)
