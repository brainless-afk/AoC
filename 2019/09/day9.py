with open('input') as file:
    arr_in = list(map(int, file.read().split(',')))
    #arr_in = list(map(int, "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99".split(',')))
    #arr_in = list(map(int, "1102,34915192,34915192,7,4,7,99,0".split(',')))
    #arr_in = list(map(int, "104,1125899906842624,99".split(',')))

def get_mode(arr, position, mode):
    if int(mode) == 0:
        return arr[arr[position]]
    elif int(mode) == 1:
        return arr[position]
    return arr[arr[position] + relative_base]


def set_mode(arr, position, mode):
    m = int(mode)
    if m == 0 or m == 1:
        return arr[position]
    return arr[position] + relative_base


def calc_intcode(array, in_phase, in_signal, phase=True, pos_zero=0):
    global relative_base
    pad_zeroes = f"{array[pos_zero]:05d}"
    opcode = int(pad_zeroes[-2:])
    mode3, mode2, mode1 = pad_zeroes[:-2]
    out = 0
    fin = False

    while opcode != 99:
        if opcode == 1:
            array[set_mode(array, pos_zero + 3, mode3)] = get_mode(array, pos_zero + 1, mode1) + \
                                         get_mode(array, pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 2:
            array[set_mode(array, pos_zero + 3, mode3)] = get_mode(array, pos_zero + 1, mode1) * \
                                         get_mode(array, pos_zero + 2, mode2)
            pos_zero += 4
        elif opcode == 3:
            if phase:
                array[set_mode(array, pos_zero + 1, mode1)] = in_phase
            else:
                array[set_mode(array, pos_zero + 1, mode1)] = in_signal
            phase = False
            pos_zero += 2
        elif opcode == 4:
            out = get_mode(array, pos_zero + 1, mode1)
            pos_zero += 2
            return array[:], out, pos_zero, phase, fin
        elif opcode == 5:
            if not get_mode(array, pos_zero + 1, mode1) == 0:
                pos_zero = get_mode(array, pos_zero + 2, mode2)
            else:
                pos_zero += 3
        elif opcode == 6:
            if get_mode(array, pos_zero + 1, mode1) == 0:
                pos_zero = get_mode(array, pos_zero + 2, mode2)
            else:
                pos_zero += 3
        elif opcode == 7:
            if get_mode(array, pos_zero + 1, mode1) < get_mode(array, pos_zero + 2, mode2):
                array[set_mode(array, pos_zero + 3, mode3)] = 1
            else:
                array[set_mode(array, pos_zero + 3, mode3)] = 0
            pos_zero += 4
        elif opcode == 8:
            if get_mode(array, pos_zero + 1, mode1) == get_mode(array, pos_zero + 2, mode2):
                array[set_mode(array, pos_zero + 3, mode3)] = 1
            else:
                array[set_mode(array, pos_zero + 3, mode3)] = 0
            pos_zero += 4
        elif opcode == 9:
            relative_base += get_mode(array, pos_zero + 1, mode1)
            pos_zero += 2
        else:
            raise Exception("opcode error")

        pad_zeroes = f"{array[pos_zero]:05d}"
        opcode = int(pad_zeroes[-2:])
        mode3, mode2, mode1 = pad_zeroes[:-2]

    fin = True
    return array, out, pos_zero, phase, fin


relative_base = 0

for x in range(100000):
    arr_in.append(0)

last_output = []
arr_ = arr_in[:]
out_ = 0
pos_ = 0
phase_in = 2
fin_ = False
phase_ = True
while not fin_:
    arr_, out_, pos_, phase_, fin_ = calc_intcode(arr_, phase_in, out_, phase_, pos_)
    print(out_)
print(last_output)
