from _collections import defaultdict

orbits = defaultdict(list)
with open('input') as file:
    for line in file:
        left, right = line[:-1].split(')')
        orbits[left].append(right)

count_orbits = 0


def walk_tree(planet, orbit_count):
    global count_orbits

    for orbiter in orbits[planet]:
        count_orbits += orbit_count
        walk_tree(orbiter, orbit_count + 1)


walk_tree('COM', 1)
print("Part1: Number of direct and indirect orbits: ", count_orbits)

# Part 2
orbits = defaultdict(list)
with open('input') as file:
    for line in file:
        left, right = line[:-1].split(')')
        orbits[left].append(right)
        orbits[right].append(left)

destination = 'SAN'
seen_planets = {'YOU': 0}


def find_santa(start, moves):
    for planet in orbits[start]:
        if planet not in seen_planets:
            if not planet == destination:
                seen_planets[planet] = moves + 1
                find_santa(planet, seen_planets[planet])
            else:
                print("Santa found orbiting Planet:", orbits[planet][-1], " Steps taken: ", moves)

        elif seen_planets[planet] > moves + 1:
            seen_planets[planet] = moves + 1


find_santa('YOU', -1)  # -1 cause transfer from YOU to first orbiting planet doesn't count

