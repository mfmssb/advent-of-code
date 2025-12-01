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


# `d[y][x]` med origo øverst til venstre

# +
d = data[0].split("\n")

H = len(d)
W = len(d[0])

mapd = d[::]

g = locate_guard(mapd)
# -

while is_in_bounds(mapd, g[0], g[1]):
    mapd, g = take_step(mapd, g)

ans1 = sum([line.count("X") for line in mapd])

# ## Solution 1

print(ans1)

# # Problem 2

# ## Intermediate Steps 2

mapd

# ## Solution 2

mapd

(gx, gy, gd) = locate_guard(new_map)

gx, gy

# For alle "X" i mapd som ikke er guard startpos:
#
#     - sett inn en obstacle "#" i new_map
#     - gjør take_step uten å markere i kartet
#     - lagre indeksene der vakten har gått med retning i en dict, med liste over retningene
#     - sjekke om vakten har vært på posisjon i en spesiell retning før.
#         - Dersom dette skjer, har vi funnet en loop og vi teller count +=1
#     - gå til neste obstacle

d

new_map = d[::]
