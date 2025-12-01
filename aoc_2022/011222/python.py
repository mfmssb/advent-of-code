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

elves = datastr.split("\n\n")

sacks = []

for e in elves:
    sack_str = e.split("\n")
    sack_int = [int(x) for x in sack_str]
    sacks.append(sum(sack_int))

print(max(sacks))

# %%
sacks.sort()

# %%
sum(sacks[-3:])
