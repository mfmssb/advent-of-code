# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %%
f = open("data.txt", "r")
datastr = f.read()
datalines = datastr.split("\n")

H = len(datalines)

gridsize = H*2
(MIDX, MIDY) = (H, H)

(hx, hy) = (MIDX, MIDY)
(tx, ty) = (MIDX, MIDY)
# making an empty grid
grid = [[0] * gridsize for y in range(gridsize)]
grid[ty][tx] = 1


# %%
def move_head(hx, hy, tx, ty, direction, num_steps):
    (vx, vy) = get_direction_vector(direction)
    
    for i in range(num_steps):
        fx = hx + vx
        hy = hy + vy
        (tx, ty) = update_tail(hx, hy, tx, ty)
    
    return (hx, hy, tx, ty)

def update_tail(hx, hy, tx, ty):
    diffx = hx-tx
    diffy = hy-ty
    
    offset = abs(diffx) + abs(diffy)

    sdiffx = sign(diffx)
    sdiffy = sign(diffy)
    
    if offset == 0 or offset == 1:
        return (tx, ty)

    if offset > 3:
        print("Error something is wrong")

    # offset = 2 (north, east, south, west) + short diagonals
    
    if abs(diffx) == 1 and abs(diffy) == 1: # short diagonals
        return (tx, ty)
    
    # offset = 3 long diagonals

    tx += sdiffx
    ty += sdiffy

    grid[ty][tx] = 1  

    return (tx, ty)

def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1

def get_direction_vector(direction):
    if   direction == "U": (vx, vy) = (0, -1)
    elif direction == "R": (vx, vy) = (1, 0)
    elif direction == "D": (vx, vy) = (0, 1)
    elif direction == "L": (vx, vy) = (-1, 0)
    else:
        (vx, vy) = (None, None)
        print("ERROR direction")
    return (vx, vy)

def draw_board(hx,hy,tx,ty):
    print("-" * 50)
    hprev = grid[hy][hx] 
    tprev = grid[ty][tx]

    grid[hy][hx] = 3
    grid[ty][tx] = 2

    for row in grid:
        print(row)
    grid[hy][hx] = hprev
    grid[ty][tx] = tprev


# %%
for line in datalines:
    instruction = line.split(" ")
    
    dir = instruction[0]
    steps = int(instruction[1]) 
     
    (hx, hy, tx, ty) = move_head(hx, hy, tx, ty, dir, steps)


# %%
# draw_board(hx,hy,tx,ty) # warning 4000x4000 table ;)

# %%
sum([sum(row) for row in grid])

# %% [markdown]
# ### Part 2

# %%
f = open("test.txt", "r")
datastr = f.read()
datalines = datastr.split("\n")

H = len(datalines)
ROPELENGTH = 10

gridsize = H*2
(MIDX, MIDY) = (H, H)

# rope = ROPELENGTH*[[H,H].copy()]
rope = [[H,H] for i in range(ROPELENGTH)]

# making an empty grid
grid = [[0] * gridsize for y in range(gridsize)]


# %%
def move_head2(rope, direction, num_steps):
    (vx, vy) = get_direction_vector(direction)
    
    for i in range(num_steps):
        rope[0][0] += vx
        rope[0][1] += vy

        for i in range(1,ROPELENGTH):
            # draw_board2(rope)
            rope[i] = update_tail2(rope[i], rope[i-1])

            if i == ROPELENGTH-1:
                # set grid value to be 1 if tail has been there
                grid[rope[i][1]][rope[i][0]] = 1  

def update_tail2(front_part, behind_part):
    fx = front_part[0]
    fy = front_part[1]
    bx = behind_part[0]
    by = behind_part[1]

    diffx = fx-bx
    diffy = fy-by  
    
    offset = abs(diffx) + abs(diffy)

    sdiffx = sign(diffx)
    sdiffy = sign(diffy)
    
    if offset == 0 or offset == 1:
        return [bx, by]

    if offset > 3:
        print("Error something is wrong")

    # offset = 2 is north, east, south, west + short diagonals
    
    if abs(diffx) == 1 and abs(diffy) == 1: # short diagonals
        return [bx, by]
    
    # offset = 3 long diagonals

    bx += sdiffx
    by += sdiffy

    

    return [bx, by]

def draw_board2(rope):
    print("-" * 50)
    
    prev_values = []
    for i in range(ROPELENGTH):
        (x, y) = (rope[i][0], rope[i][1])
        prev_values.append(grid[y][x])
    
    for i in range(ROPELENGTH):
        (x, y) = (rope[i][0], rope[i][1])
        grid[y][x] = "MAGNE"
        # grid[y][x] = ROPELENGTH - i - 1

    for row in grid:
        print(row)

    for i in range(ROPELENGTH):
        (x, y) = (rope[i][0], rope[i][1])
        grid[y][x] = prev_values[i]



# %%
move_head2(rope, "D", 6)
draw_board2(rope)

# %%
draw_board2(rope)
