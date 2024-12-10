filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")


# # Problem 1

# ## Intermediate Steps 1

def identify_antennas(mapd: list, not_antennas=set('.')) -> set:
    unique_antennas = set()
    for line in mapd:
        unique_antennas |= set(line)
    return list(unique_antennas - not_antennas)


def get_antenna_locations(antennas: list, mapd: list) -> dict:
    antenna_locations = {}
    for antenna in antennas:
        locations = []
        for y in range(len(d)):
            for x in range(len(d[0])):
                if d[y][x] == antenna:
                    locations.append((x, y))
        antenna_locations[antenna] = locations
    return antenna_locations


def vector_add(u: tuple, v: tuple) -> tuple:
    # Assume 2D vector
    return (u[0]+v[0], u[1]+v[1])


def vector_difference(u: tuple, v: tuple) -> tuple:
    # Assume 2D vector
    return (u[0]-v[0], u[1]-v[1])


def vector_scalar(t: int, v: tuple) -> tuple:
    # Assume 2D vector
    return (t*v[0], t*v[1])


def is_in_bounds(point, mapd) -> bool:
    x = point[0]
    y = point[1]
    h = len(mapd)
    w = len(mapd[0])

    return 0 <= x < w and 0 <= y < h


def mark_map(x: int, y: int, mapd: list, mark="#") -> list:
    line = mapd[y]

    new_line = line[:x] + mark + line[(x+1):]
    mapd[y] = new_line
    return mapd


from itertools import combinations

d = data[1].split("\n")
antinode_map = d[::]
antennas = identify_antennas(d)
antenna_locations = get_antenna_locations(antennas, d)

for a_name, l in antenna_locations.items():
    combs = list(combinations(l, 2))
    for comb in combs:
        p1, p2 = comb
        v1 = vector_difference(p1, p2)
        v2 = vector_scalar(-1, v1)

        a1 = vector_add(p2, v2)
        a2 = vector_add(p1, v1)
        
        if is_in_bounds(a1, d):
            mark_map(a1[0], a1[1], antinode_map)
        if is_in_bounds(a2, d):
            mark_map(a2[0], a2[1], antinode_map)


num_antinodes = sum([line.count("#") for line in antinode_map])
ans1 = num_antinodes

# ## Solution 1

ans1

# # Problem 2

# ## Intermediate Steps 2

d = data[0].split("\n")
antinode_map = d[::]
antennas = identify_antennas(d)
antenna_locations = get_antenna_locations(antennas, d)

for a_name, l in antenna_locations.items():
    combs = list(combinations(l, 2))
    for comb in combs:
        p1, p2 = comb
        v1 = vector_difference(p1, p2)
        v2 = vector_scalar(-1, v1)

        a1 = vector_add(p2, v2)
        a2 = vector_add(p1, v1)

        while is_in_bounds(a1, d):
            mark_map(a1[0], a1[1], antinode_map)
            a1 = vector_add(a1, v2)

        while is_in_bounds(a2, d):
            mark_map(a2[0], a2[1], antinode_map)
            a2 = vector_add(a2, v1)

# +
# num_antinodes = sum([line.count("#") for line in antinode_map])
num_antinodes = 0
for line in antinode_map:
    print(num_antinodes)
    num_antinodes += len(line) - line.count(".")

ans2 = num_antinodes
# -



ans2

antinode_map

test = [
    "##....#....#",
    ".#.#....0...",
    "..#.#0....#.",
    "..##...0....",
    "....0....#..",
    ".#...#A....#",
    "...#..#.....",
    "#....#.#....",
    "..#.....A...",
    "....#....A..",
    ".#........#.",
    "...#......##"]

sum([line.count("#") for line in test])

antinode_map

# ## Solution 2

print(ans2)


