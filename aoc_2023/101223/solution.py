filnavn = ["data0.txt", "data1.txt", "data2.txt", "data3.txt", "data4.txt", "data5.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Oppgave 1

d = data[5].split("\n")


# ## Mellomregning

def locate_S(_map):
    """ Assumes one S in map """
    for j in range(len(_map)):
        for i in range(len(_map[j])):
            if _map[j][i] == "S":
                return i, j


def is_valid_index(m, x, y):
    len_x = len(m[0])
    len_y = len(m)
    return (0 <= x < len_x) and 0 <= y < len_y


def infer_start_connection(m, parsed_map, x, y):
    directions = {
        "N": (0, -1, "S"),
        "S": (0, 1, "N"),
        "E": (1, 0, "W"),
        "W": (-1, 0, "E")
    }
    start_dict = {_dir: 0 for _dir in directions}

    for _dir, (dx, dy, opposite) in directions.items():
        new_x, new_y = x + dx, y + dy
        if is_valid_index(m, new_x, new_y) and parsed_map[new_y][new_x][opposite] == 1:
            start_dict[_dir] = 1

    return start_dict


parse_map = {
    "|": {"N": 1, "S": 1, "E": 0, "W": 0 },  # is a vertical pipe connecting north and south.
    "-": {"N": 0, "S": 0, "E": 1, "W": 1 },  # is a horizontal pipe connecting east and west.
    "L": {"N": 1, "S": 0, "E": 1, "W": 0 },  # is a 90-degree bend connecting north and east.
    "J": {"N": 1, "S": 0, "E": 0, "W": 1 },  # is a 90-degree bend connecting north and west.
    "7": {"N": 0, "S": 1, "E": 0, "W": 1 },  # is a 90-degree bend connecting south and west.
    "F": {"N": 0, "S": 1, "E": 1, "W": 0 },  # is a 90-degree bend connecting south and east.
    ".": {"N": 0, "S": 0, "E": 0, "W": 0 },  # is ground; there is no pipe in this tile.
}

# +
parsed_map = [[None for _ in range(len(d[0]))] for _ in range(len(d))]

for pipesymbol, NSEW in parse_map.items():
    for i in range(len(d[0])):
        for j in range(len(d)):    
            if pipesymbol == d[j][i]:
                parsed_map[j][i] = NSEW
# -

Sx, Sy = locate_S(d)

parsed_map[Sy][Sx] = infer_start_connection(d, parsed_map, Sx, Sy)

pm = [[-1 for _ in range(len(d[0]))] for _ in range(len(d))]
pm[Sy][Sx] = 0



directions = {
    "N": (0, -1, "S"),
    "S": (0, 1, "N"),
    "E": (1, 0, "W"),
    "W": (-1, 0, "E")
}

x

other_dir = None
x, y = Sx, Sy
for _dir, binary in parsed_map[Sy][Sx].items():
    if binary == 1 and not bool(other_dir):
        x1 = x + directions[_dir][0]
        y1 = y + directions[_dir][1]
        other_dir = _dir
    if binary == 1 and bool(other_dir):
        x2 = x + directions[_dir][0]
        y2 = y + directions[_dir][1]


def next_pipe(m, parsed_map, x, y, prev_x, prev_y):
    directions = {
        "N": (0, -1, "S"),
        "S": (0, 1, "N"),
        "E": (1, 0, "W"),
        "W": (-1, 0, "E")
    }
    current_connections = parsed_map[y][x]
    for direction, (dx, dy, required) in directions.items():

        if current_connections.get(direction):
            new_x, new_y = x + dx, y + dy

            if is_valid_index(m, new_x, new_y) and (new_x, new_y) != (prev_x, prev_y):
                if parsed_map[new_y][new_x] and parsed_map[new_y][new_x].get(required):
                    return new_x, new_y
    return None, None


# Start traversal
prev_x, prev_y = None, None
x, y = Sx, Sy

# Traverse the pipes
counter = 1
while True:
    new_x, new_y = next_pipe(d, parsed_map, x, y, prev_x, prev_y)
    if new_x is None or new_y is None:
        break
    if new_x == Sx and new_y == Sy and (prev_x, prev_y) != (None, None):
        break
    pm[new_y][new_x] = counter
    counter += 1
    prev_x, prev_y = x, y
    x, y = new_x, new_y

    # print(f"Moved to {x}, {y} (Step {counter})")

# See the input map
for w in d:
    print(w)

# ## Løsning

# The furthest point from S is half the steps taken to traverse the whole path
print(counter/2)

# # Oppgave 2

# ## Mellomregning

# Visualize pipes
["".join(["#" if y != -1 else "." for y in x]) for x in pm]

# ## Løsning


