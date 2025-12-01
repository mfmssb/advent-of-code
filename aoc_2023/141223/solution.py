filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

d = data[1].split("\n")

d = [[char for char in x] for x in d]


# ## Intermediate Steps 1

# +
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

def reverse_columns(matrix):
    return [row[::-1] for row in matrix]

def rotate_90_clockwise(matrix):
    return reverse_columns(transpose(matrix))

def rotate_90_counterclockwise(matrix):
    transposed = transpose(matrix)
    return transposed[::-1]


# -

def swap(s, i, j):
    """ Swap characters in string s at index i and j"""
    a = s[i]
    b = s[j]
    new_s = s[:i] + b + s[(i+1):]
    new_s = new_s[:j] + a + new_s[(j+1):]
    return new_s


import re
def tilt_row(row):
    """ Tilt row to the left (west)"""
    
    row_str = "".join(row)
    
    ind_o = [match.start() for match in re.finditer("O", row_str)]
    ind_stop = [match.start() for match in re.finditer("#", row_str)]
    
    prev_stop = -1
    for stop in ([-1] + ind_stop + [len(row_str)]):
        if stop == -1:
            continue
            
        offset = 1
        while True:
            if prev_stop + offset >= len(row_str):
                break
            if row_str[prev_stop + offset] == "O":
                offset += 1
            else:
                break
        
        for o in ind_o:
            if (prev_stop < o < stop) and (prev_stop + offset < o):
                row_str = swap(row_str, prev_stop + offset, o)
                offset += 1
        prev_stop = stop
    return [char for char in row_str]


def tilt(matrix, direction="W"):
    
    # Transform to direction West before tilting
    if direction == "N": matrix = rotate_90_counterclockwise(matrix)
    if direction == "S": matrix = rotate_90_clockwise(matrix)
    if direction == "E": matrix = rotate_90_clockwise(rotate_90_clockwise(matrix))

    matrix = [tilt_row(row) for row in matrix]
            
    # Undo transformation
    if direction == "N": matrix = rotate_90_clockwise(matrix)
    if direction == "S": matrix = rotate_90_counterclockwise(matrix)
    if direction == "E": matrix = rotate_90_clockwise(rotate_90_clockwise(matrix))
    
    return matrix


def calculate_load(matrix):
    """ Calculate load given board state """
    load = len(matrix)
    
    total_load = 0
    for row in matrix:
        row_str = "".join(row)
        total_load += load * row_str.count("O")
        load -= 1
    return total_load


# %%time
ans1 = calculate_load(tilt(d, direction="N"))

# ## Solution 1

print(ans1)

# # Problem 2

d = data[1].split("\n")

d = [[char for char in x] for x in d]


# ## Intermediate Steps 2

def print_state(state):
    """ Print board state for debugging """
    for line in state:
        print(("").join(line))
    print(20*"-")


# +
cycle = ["N", "W", "S", "E"]

num_cycles = 1000  # arbitrary number to limit the search for all possible board states

# +
# %%time
previous_states = []
tilted = d.copy()

for i in range(num_cycles):
    for _dir in cycle:
        tilted = tilt(tilted, direction=_dir)
    
    break_outer = False
    for j, state in enumerate(previous_states):
        if tilted == state:         
            break_outer = True
            break
    if break_outer:
        cycle_start = j  # index were the the repeating board states starts
        last_number_of_cycles = i  # the number of cycles before the board state repeats itself
        break
    previous_states.append(tilted)


# -

def calc_index(n, cycle_start, last_number_of_cycles):
    """ Calculate index of the board state in previous_states that corresponds to n cycles """
    cycle_length = last_number_of_cycles - cycle_start  # the length of repeating board states
    if n < cycle_length + cycle_start:
        return n
    return ((n - cycle_start + 1) % cycle_length) + cycle_start - 1


# ## Solution 2

print(calculate_load(previous_states[calc_index(10**9-1, cycle_start, last_number_of_cycles)]))
