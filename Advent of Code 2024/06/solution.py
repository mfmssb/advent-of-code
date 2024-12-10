filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")


# # Problem 1

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


def is_markable(d, posx, posy, obstacle='#'):
    if is_in_bounds(d, posx, posy) and d[posy][posx] != obstacle:
        return True
    return False


def mark_map(d: list, posx: int, posy: int, mark='X', obstacle='#'):
    if is_in_bounds(d, posx, posy):
        if d[posy][posx] != obstacle:
            line = d[posy]
            line = line[:posx] + mark + line[(posx + 1):]
            d[posy] = line
    return d


def take_step(d: list, guard: tuple, obstacle='#') -> (int, int, str):
    gx, gy, gdir = guard

    if is_markable(d, gx, gy):
        gx_new, gy_new = gx+DIRS[gdir][0], gy+DIRS[gdir][1]
        d_marked = mark_map(d, gx, gy)

        if is_in_bounds(d, gx_new, gy_new):
            if d[gy_new][gx_new] == obstacle:
                gdir = ROTATE90[gdir]
            else:
                gx, gy = gx_new, gy_new
        else:
            gx, gy = gx_new, gy_new
    else:
        d_marked = d
    
    return (d_marked, (gx, gy, gdir))


d = data[1].split("\n")

# `d[y][x]` med origo øverst til venstre

H = len(d)
W = len(d[0])

mapd = d[::]

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

g = locate_guard(mapd)

while is_in_bounds(mapd, g[0], g[1]):
    mapd, g = take_step(mapd, g)

count = 0
for line in mapd:
    count += line.count("X")
ans1 = count


# ## Intermediate Steps 1

print(ans1)

# ## Solution 1



# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


