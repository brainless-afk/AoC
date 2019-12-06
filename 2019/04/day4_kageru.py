import collections

input_min = 158126
input_max = 624574


def check_password(number):
    digits = list(map(int, str(number)))
    if digits != sorted(digits):
        return False

    element_counter = collections.Counter(digits)
    for one, two in zip(digits, digits[1:]):
        if one == two and element_counter.get(one) == 2:
            return True
    return False


pwd_count = len(list(filter(check_password, range(input_min, input_max + 1))))
print("Number of potential passwords: ", pwd_count)
