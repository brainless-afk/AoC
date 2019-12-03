file = open('input')
path_wire1, path_wire2 = file.read().split()
path_wire1, path_wire2 = [cmd.split(',') for cmd in [path_wire1, path_wire2]]
file.close()


def get_direction(d):
    if d == "L":
        return -1, 0
    if d == "R":
        return 1, 0
    if d == "U":
        return 0, 1
    else:
        return 0, -1


def manhattan(x_, y_):
    return abs(x_) + abs(y_)


def get_steps(key_):
    return grid1.get(key_) + grid2.get(key_)


def map_grid(path_wire):
    grid = {}
    x = 0
    y = 0
    steps = 0
    for cmd in path_wire:
        direction, distance = cmd[:1], int(cmd[1:])
        dx, dy = get_direction(direction)
        for number in range(distance):
            x += dx
            y += dy
            steps += 1
            if (x, y) not in grid:
                grid[(x, y)] = steps
    return grid


grid1 = map_grid(path_wire1)
grid2 = map_grid(path_wire2)

intersections = set(grid1.keys()).intersection(grid2.keys())
print(intersections)

closest_intersection = 9999999
fewest_steps = 9999999
for cross in intersections:
    manhattan_distance = manhattan(cross[0], cross[1])
    if manhattan_distance < closest_intersection and manhattan_distance != 0:
        closest_intersection = manhattan_distance
    steps_taken = get_steps(cross)
    if steps_taken < fewest_steps and steps_taken != 0:
        fewest_steps = steps_taken

print("Closest intersection: ", closest_intersection)
print("Fewest steps: ", fewest_steps)
