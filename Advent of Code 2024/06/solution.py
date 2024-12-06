filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")

# # Problem 1

d = data[0].split("\n")

# `d[y][x]` med origo øverst til venstre

H = len(d)
W = len(d[0])

d

DIRS = {
    '^': ( 0, -1),
    '>': ( 1,  0),
    'v': ( 0,  1),
    '<': (-1,  0),
}
ROTATE90 = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^',
}


def locate_guard(d: list, guard_chars=['^', '>', 'v', '<']) -> (int, int, str):
    for y in range(H):
        for x in range(W):
            if d[y][x] in guard_chars:
                return (x, y, d[y][x])
    raise ValueError("Guard not found")


def is_in_bounds(d: str, posx: int, posy: int) -> bool:
    if (0 <= posx < W) and (0 <= posy < H):
        return True
    return False
is_in_bounds(d, -1, 0)


def mark_map(d: list, posx: int, posy: int, mark='X'):
    if is_in_bounds(d, posx, posy):
        line = d[posy]
        line = line[:posx] + mark + line[(posx + 1):]
        d[posy] = line
    return d


mark_map(d, 9, 9)


# +
def take_step(d: list, guard: tuple) -> (int, int, str):
    gx, gy, gdir = guard
    
    
# -

locate_guard(d)

# ## Intermediate Steps 1



# ## Solution 1



# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


