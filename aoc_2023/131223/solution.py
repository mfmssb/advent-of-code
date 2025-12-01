filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

import pandas as pd

d = data[1].split("\n\n")
d = [x.split("\n") for x in d]


# ## Intermediate Steps 1

def check_mirrored(df, horizontal=True):
    import numpy as np
    
    if df.shape[0] % 2 != 0 & horizontal == True:
        print(df.shape[1])
        raise ValueError("Not even number of columns")
    if (df.shape[0] % 2 != 0) & (horizontal == False):
        raise ValueError("Not even number of rows")
    if not horizontal:
        df = df.T
    
    split_i = int((df.shape[1] / 2))
    
    first = df.iloc[:, :split_i]
    second = df.iloc[:, split_i:]
    second_rev = second.loc[:, ::-1] 
    second_rev.columns = second.columns
    
    return np.array_equal(first.values, second_rev.values)


# %%time
num_cols = []
num_rows = []
verbose = False
for i in range(len(d)):
    df = pd.DataFrame([list(x) for x in d[i]])

    h = df.shape[0]
    w = df.shape[1]

    #### Horizontal mirror image
    ## From left
    mirror_pos = 0
    while 2*mirror_pos < w:
        mirror_pos += 1
        _to = 2*mirror_pos

        if check_mirrored(df.iloc[:, :_to]):
            num_cols.append(mirror_pos)
            if verbose: print(i, "Horizontal mirror image from left", mirror_pos)
            break

    ## From right
    mirror_pos = w-1
    while 2*mirror_pos > w:
        _from = w-2*(w-mirror_pos)

        if check_mirrored(df.iloc[:, _from:]):
            num_cols.append(mirror_pos)
            if verbose: print(i, "Horizontal mirror image from right", mirror_pos)
            break
        mirror_pos -= 1

    #### Vertical mirror image

    ## From top
    mirror_pos = 0
    while 2*mirror_pos < h - 1:
        mirror_pos += 1
        _to = 2*mirror_pos

        if check_mirrored(df.iloc[:_to, :], horizontal=False):
            num_rows.append(mirror_pos)
            if verbose: print(i, "Vertical mirror image from top",mirror_pos)
            break

    ## From bottom
    mirror_pos = h-1
    while 2*mirror_pos > h:
        _from = h-2*(h-mirror_pos)

        if check_mirrored(df.iloc[ _from:, :], horizontal=False):
            num_rows.append(mirror_pos)
            if verbose: print(i, "Vertical mirror image from bottom",mirror_pos)
            break
        mirror_pos -= 1

# ## Solution 1

print(100*sum(num_rows) + sum(num_cols))

# # Problem 2

# ## Intermediate Steps 1



# ## Solution 2


