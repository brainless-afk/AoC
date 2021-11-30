from itertools import combinations

with open('input.txt') as f:
    lines = list(map(int, f.readlines()))


def part1(lines):
    comb = combinations(lines, 2) 
    for i in list(comb):  
        if (i[0] + i[1] == 2020):
            return i[0] * i[1]

def part2(lines):
    comb = combinations(lines, 3) 
    for i in list(comb):  
        if (i[0] + i[1] + i[2] == 2020):
            return i[0] * i[1] * i[2]


print(part1(lines))
print(part2(lines))