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


# %%
height_grid = []
for y in datalines:
    height_grid.append(list(y))

def create_grid(w, h, val):
    eg = []
    for j in range(h):
        eg.append([val] * w)
    return eg

H = len(datalines)
W = len(datalines[0])
INFINITY = 9999

score_grid = create_grid(W,H,INFINITY)

dir_dict = {0: [0, -1], 1: [1, 0], 2: [0, 1], 3: [-1, 0]}


# %%
def locate_start_end_points():
    sx, sy, ex, ey = -1, -1, -1, -1
    for i, l in enumerate(datalines):
        x = l.find("S")
        if x != -1:
            sy = i
            sx = x

    for i, l in enumerate(datalines):
        x = l.find("E")
        if x != -1:
            ey = i
            ex = x
    return sx, sy, ex, ey
(START_X, START_Y, END_X, END_Y) = locate_start_end_points()


# %%
def step_value(letter_on, letter_side):
    HEIGHT_ORDER = "abcdefghijklmnopqrstuvwxyz" # S for start, 
    if len(letter_on) != 1 or len(letter_side) != 1:
        print("Error legal step")
        return False
    if letter_side == "S": # Start has height a
        letter_side = "a"
    if letter_side == "E": # End has height z
        letter_side = "z"
    i_on = HEIGHT_ORDER.find(letter_on)
    i_side = HEIGHT_ORDER.find(letter_side)

    return i_side - i_on


# %%
def probe_neighbours(grid, cx, cy):
    if cy-1 >= 0:
        north = grid[cy-1][cx]
    else:
        north = None
    if cy+1 < len(grid):
        south = grid[cy+1][cx]
    else:
        south = None
    if cx-1 >= 0:
        west = grid[cy][cx-1]
    else:
        west = None
    if cx+1 < len(grid[0]):
        east = grid[cy][cx+1]
    else:
        east = None
    return (north, east, south, west)

# %%
# def Dijkstra(Graph, source):
    
#     for each v in Graph.Vertices: # vertex = node
#         dist[v] ← INFINITY               # array that contains the current distances from the source to other vertices
#         prev[v] ← UNDEFINED              
#         add v to Q
#     dist[source] ← 0
    
#     while Q is not empty:
#         u ← vertex in Q with min dist[u]
#         remove u from Q
        
#         for each neighbor v of u still in Q:
#             alt ← dist[u] + Graph.Edges(u, v)
#             if alt < dist[v]:
#                 dist[v] ← alt
#                 prev[v] ← u
#     return dist[], prev[]

# %%
# S ← empty sequence
# u ← target
# if prev[u] is defined or u = source:          # Do something only if the vertex is reachable
#     while u is defined:                       # Construct the shortest path with a stack S
#         insert u at the beginning of S        # Push the vertex onto the stack
#         u ← prev[u]                           # Traverse from target to source

# %%
# # Step 2
# nx = START_X
# ny = START_Y
# score_grid[ny][nx] = 0
# visited = create_grid(W,H,-1)

# counter = 0
# while(counter < H*W):
#     counter += 1
#     # Step 3

#     # legal nodes: return values: (North, East, South, West)
#     neighbour_scores = probe_neighbours(score_grid, nx, ny)

#     # fill score values around current node
#     for i in range(4):
#         if neighbour_scores[i] != None:
#             v = dir_dict[i]
#             if step_value(height_grid[ny][nx], height_grid[ny+v[1]][nx+v[0]]) <= 1: # step is legal
#                 new_val = score_grid[ny][nx] + 1
#                 old_val = score_grid[ny+v[1]][nx+v[0]]
#                 if new_val < old_val:
#                     score_grid[ny+v[1]][nx+v[0]] = new_val

#     # Step 4)
#     visited[ny][nx] = 1

#     # Step 5) 
#     neighbour_visited = probe_neighbours(visited, nx, ny)
#     neighbour_scores = probe_neighbours(score_grid, nx, ny)

#     # found_new_cell = False
#     # for i in range(4):
#     #     if neighbour_visited[i] != None and neighbour_visited[i] != 1 and neighbour_scores[i] < INFINITY: 
#     #         v = dir_dict[i]
#     #         nx += v[0]
#     #         ny += v[1]
#     #         found_new_cell = True   
#     #         break

#     smallest = INFINITY
#     sx, sy = -1, -1
#     for i in range(W):
#         for j in range(H):
#             if score_grid[j][i] < INFINITY and visited[j][i] == -1 and score_grid[j][i] < smallest:
#                 smallest = score_grid[j][i]
#                 sx, sy = i, j
#     nx, ny = sx, sy

#     if nx == END_X and ny == END_Y:
#         break
#     print("--"*50)
#     for l in score_grid:
#         print(l[(nx-3):nx+3])
#     print("--"*50)
    


# %%
nx = START_X
ny = START_Y
score_grid[ny][nx] = 0
visited = create_grid(W,H,-1)

# %%
counter = 0
while(counter < H*W):
    counter += 1
    neighbours_scores = probe_neighbours(score_grid,nx,ny)
    for i in range(len(neighbours_scores)):
        if neighbours_scores[i] != None:
            [vx,vy] = dir_dict[i]
            x = nx + vx
            y = ny + vy
            letter_on = height_grid[ny][nx]
            letter_side = height_grid[y][x]
            if step_value(letter_on, letter_side) <= 1 and score_grid[y][x] > score_grid[ny][nx] + 1:
                score_grid[y][x] = score_grid[ny][nx] + 1
    
    visited[ny][nx] = 1

    smallest = INFINITY
    sx, sy = -1, -1

    for i in range(W):
        for j in range(H):
            if score_grid[j][i] < smallest and visited[j][i] == -1:
                smallest = score_grid[j][i]
                sx, sy = i, j
    nx, ny = sx, sy

# %%
print("Shortest distance:", score_grid[END_Y][END_X])

# %%
for i in range(W):
    for j in range(H):
        score_grid[j][i] = str(score_grid[j][i]) + " " * (4-len(str(score_grid[j][i])))

for l in score_grid:
    l = [str(x) for x in l]
    
    print("  ".join(l))
counter += 1

# %%
height_grid[END_Y][END_X]

# %%
END_X, END_Y

# %%

# %%
# 590 is too high 442 443
