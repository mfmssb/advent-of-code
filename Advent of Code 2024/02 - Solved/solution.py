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

import pandas as pd

d = data[1].split("\n")

# +
d_dict = {f"rep_{i}": x.split(" ") for i, x in enumerate(d)}

replen_max = -1
for k, v in d_dict.items():
    if len(v) > replen_max:
        replen_max = len(v)

for k, v in d_dict.items():
    if len(v) < 8:
        v.extend([None] * (replen_max - len(v)))

# +
# # %%timeit
df = pd.DataFrame(d_dict, dtype='Int64').T

for i in df.columns:
    if int(i) > 0:
        df[f"diff_{i}_{i+1}"] = df[i] - df[i-1]

diffcols = [col for col in df.columns if str(col).startswith('diff')]

rule1 = (df[diffcols].max(axis=1) <= 3)
rule2 = (df[diffcols].min(axis=1) >= -3)
rule3 = (df[diffcols] > 0).all(axis=1) | (df[diffcols] < 0).all(axis=1)
rule4 = (df[diffcols] == 0).any(axis=1) == False

df['is_safe'] = rule1 & rule2 & rule3 & rule4

ans = df['is_safe'].sum()
# -

# ## Solution 1

print(ans)

# # Problem 2

# ## Intermediate Steps 2

d = data[1].split("\n")

# +
d_dict = {f"rep_{i}": x.split(" ") for i, x in enumerate(d)}

replen_max = -1
for k, v in d_dict.items():
    if len(v) > replen_max:
        replen_max = len(v)

for k, v in d_dict.items():
    if len(v) < 8:
        v.extend([None] * (replen_max - len(v)))
# -

df = pd.DataFrame(d_dict, dtype='Int64').T

# +
all_rep_cols = df.columns

n1 = all_rep_cols.min()
n2 = all_rep_cols.max()

new_rep_cols = {}
for i in range(n1, n2+1):
    new_rep_cols[f"rem_{i}"] = [col for col in all_rep_cols if col != i]
# -

for key, cols,  in new_rep_cols.items():
    for i in range(len(cols)):
        if i > 0:
            df[f"diff_{cols[i]}_{i-1}"] = df[cols[i]] - df[cols[i-1]]
    
    diffcols = [col for col in df.columns if str(col).startswith('diff')]
    
    rule1 = (df[diffcols].max(axis=1) <= 3)
    rule2 = (df[diffcols].min(axis=1) >= -3)
    rule3 = (df[diffcols] > 0).all(axis=1) | (df[diffcols] < 0).all(axis=1)
    rule4 = (df[diffcols] == 0).any(axis=1) == False
    
    df[f'is_safe_{key}'] = rule1 & rule2 & rule3 & rule4
    
    df = df.drop(columns=diffcols)

df['is_safe'] = df[[col for col in df.columns if str(col).startswith("is_safe_rem")]].any(axis=1)

ans = df['is_safe'].sum()

# ## Solution 2

print(ans)
