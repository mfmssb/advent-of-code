filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

d = data[0].split("\n")

d

# +
springs = []
cfgs = []

for x in d: 
    cfg = x.split(" ")[1].split(",")
    spring = x.split(" ")[0]
    springs.append(spring)
    cfgs.append([int(x) for x in cfg])


# -

# ## Intermediate Steps 1

def find_cfg(s):
    cfg = []
    counter = 0
    for i in range(len(s)):
        if s[i] == "#":
            counter += 1
        else:
            if counter > 0:
                cfg.append(counter)
                counter=0
    if s[-1] == "#":
        cfg.append(counter)
    return cfg


def replace_char(s, new_char, index):
    if index >= len(s):
        raise ValueError("Index out of bounds", index)
    return s[:index] + new_char + s[(index+1):]


def all_combinations(symbols: list, length: int):
    import itertools
    combinations = list(itertools.product(symbols, repeat=length))
    return combinations


import re

# %%time
number_of_variations = 0
for ind, s in enumerate(springs):
    qm_i = [match.start(0) for match in re.finditer("\?", s)]
    combinations = all_combinations(["#", "."], len(qm_i))
    variations = []

    for combination in combinations:
        new_s = s
        for i, val in enumerate(combination):
            new_s = replace_char(new_s, val, qm_i[i])
        variations.append(new_s)
        if find_cfg(new_s) == cfgs[ind]:
            number_of_variations += 1

# ## Solution 1

print(number_of_variations)

# # Problem 2

d = data[0].split("\n")

# +
springs = []
cfgs = []

for x in d: 
    cfg = x.split(" ")[1].split(",")
    spring = x.split(" ")[0]
    springs.append(spring)
    cfgs.append([int(x) for x in cfg])

# +
# num_copies = 5
# cfgs = [num_copies*cfg for cfg in cfgs]
# springs = [("?").join(num_copies*[s]) for s in springs]
# -

cfgs

springs


# ## Intermediate Steps 2

def possibilities(substr):
    """
    Takes a series of "?" starting and ending by "." or spring boundaries and returns a list
    of tuples with possible arrangements and how many there can be.
    Ex:
    substring='.#????.'
    return [([1,1,1], 1), ([2, 1], 2), ([1, 2], 2), ([1, 3], 1), ([3, 1], 1), ([4], 1), ([5], 1)]
    """


# ## Solution 2


