import collections

input_min = 158126
input_max = 624574


def check_password(number):
    digits = list(map(int, str(number)))
    same_digit = False

    # Part 2
    element_counter = collections.Counter(digits)

    for one, two in zip(digits, digits[1:]):
        if one == two:
            if element_counter.get(one) == 2:
                same_digit = True
        if one > two:
            return False
    return same_digit


pwd_count = sum(1 if check_password(number) else 0 for number in range(input_min, input_max + 1))
print("Number of potential passwords: ", pwd_count)
