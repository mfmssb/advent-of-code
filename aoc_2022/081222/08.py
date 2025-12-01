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
grid = datastr.split("\n")

H = len(grid)    # width
W = len(grid[0]) # height

N_EDGE = 2*W + 2*H - 4 # number of trees on edge
DIRS = ["North", "East", "South", "West"]


# %%
def set_direction(direction):
    if   direction == "North": (vx, vy) = (0, -1)
    elif direction == "East":  (vx, vy) = (1, 0)
    elif direction == "South": (vx, vy) = (0, 1)
    elif direction == "West":  (vx, vy) = (-1, 0)
    else:
        (vx, vy) = (None, None)
        print("ERROR direction")
    return (vx, vy)

def is_in_line_of_sight(x,y,direction):
    tree_height = int(grid[y][x])

    (vx, vy) = set_direction(direction)

    while (x > 0 and x < W-1 and y > 0 and y < H-1):
        x += vx
        y += vy
        if int(grid[y][x]) >= tree_height:
            return False

    return True


# %%
# check all trees in the interior
# notation: grid[y][x]

interior_visible_trees = 0
for y in range(1, H-1):
    for x in range(1, W-1):
        for d in DIRS:
            if is_in_line_of_sight(x,y,d):
                interior_visible_trees += 1
                break          

tot = N_EDGE + interior_visible_trees
print(f'There are totally {tot} visible trees.')


# %% [markdown]
# ### Part 2

# %%
def number_of_visible_trees(x,y,direction):
    tree_height = int(grid[y][x])

    (vx, vy) = set_direction(direction)

    num = 0
    while (x > 0 and x < W-1 and y > 0 and y < H-1):
        x += vx
        y += vy
        num += 1
        if int(grid[y][x]) >= tree_height:
            break
    return num

def calculate_scenic_score(x,y):
    score = 1
    for d in DIRS:
        score *= number_of_visible_trees(x,y,d)
    return score


# %%
best_view = 0
for y in range(1, H-1):
    for x in range(1, W-1):
        s = calculate_scenic_score(x,y)
        if s > best_view:
            best_view = s

print(f'The best possible scenic score is {best_view}.')
