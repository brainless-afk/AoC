import itertools

with open('input') as file:
    file = file.read().splitlines()
    asteroids = [(x, y) for y, l in enumerate(file) for x, symbol in enumerate(list(l)) if symbol == '#']


def get_line(a, b):
    try:
        m = (b[1] - a[1]) / (b[0] - a[0])
        t = a[1] / (m * a[0])
        return m, t
    except ZeroDivisionError:
        return None


def is_on_line(a, m, t):
    if a[1] == m * a[0] + t:
        return True
    return False


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
