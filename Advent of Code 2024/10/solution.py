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

def find_starting_positions(mapd: list) -> list:
    starting_positions = []
    for j, y in enumerate(mapd):
        for i, x in enumerate(y):
            if mapd[j][i] == 0:
                starting_positions.append((i, j))
    return starting_positions


def is_in_bounds(mapd: list, p: tuple) -> True:
    x, y = p
    
    H = len(mapd)
    W = len(mapd[0])
    
    return 0 <= x < W and 0 <= y < H


DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

d = data[1].split("\n")
d = [[int(e) for e in x] for x in d]
starting_positions = find_starting_positions(d)
scores = {k: 0 for k in starting_positions}


def find_possible_paths_from(mapd: list, p: tuple) -> list:
    x, y = p
    val = mapd[y][x]
    next_positions = []
    for dx, dy in DIRS:
        new_p = (x + dx, y + dy)
        if is_in_bounds(mapd, new_p) and mapd[new_p[1]][new_p[0]] == val + 1:
            next_positions.append(new_p)

    if not next_positions:
        return [[p]]

    all_paths = []
    for pos in next_positions:
        sub_paths = find_possible_paths_from(mapd, pos)
        for sp in sub_paths:
            all_paths.append([p] + sp)
    return all_paths


for p , v_ in scores.items():
    paths = find_possible_paths_from(d, p)
    paths = [path for path in paths if len(path) == 10]
    scores[p] = len(set([path[-1] for path in paths]))

ans1 = sum([v for k, v in scores.items()])

# ## Solution 1

ans1

# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


