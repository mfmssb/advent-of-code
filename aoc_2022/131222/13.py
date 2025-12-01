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
datalines = [x for x in datalines if x != '']


# %%
def compare_first_smaller_than_second(l1, l2):
    # [[1],[2,3,4]]
    # [1,1,5,1,1]
    if type(l1) != list or type(l2) != list:
        print("Error. Not comparing lists")
        return
    to = min(len(l1), len(l2))
    
    for i in range(to):
        val1 = l1[i]
        val2 = l2[i]

        if type(val1) == int and type(val2) == int:
            if val1 != val2:
                return val1 < val2

        if type(val1) == list and type(val2) == int:
            if val1 != [val2]:
                return compare_first_smaller_than_second(val1, [val2])

        if type(val1) == int and type(val2) == list:
            if [val1] != val2:
                return compare_first_smaller_than_second([val1], val2)
        
        if type(val1) == list and type(val2) == list:
            if val1 != val2:
                return compare_first_smaller_than_second(val1, val2)

    if len(l1) != len(l2):
        return len(l1) < len(l2)
    return True



# %%
sum = 0
for i in range(round(len(datalines)/2)):
    a = eval(datalines[2*i])
    b = eval(datalines[2*i+1])

    if compare_first_smaller_than_second(a,b):
        sum += i+1
sum

# %% [markdown]
# # Part 2

# %%
f = open("data.txt", "r")
datastr = f.read()
datalines = datastr.split("\n")

# %%
datalines = [x for x in datalines if x != '']
datalines.append('[[2]]')
datalines.append('[[6]]')

# %%
import copy
def swap(l, n1, n2):
    a1 = copy2(l[n1])
    a2 = copy2(l[n2])
    l[n1] = a2
    l[n2] = a1
    return l

def copy2(x):
    if type(x) == list:
        return copy.deepcopy(x)
    return copy.deepcopy(x)


# %%
for i in range(len(datalines)):
    for j in range(i, len(datalines)):
        a = eval(datalines[i])
        b = eval(datalines[j])
        if not compare_first_smaller_than_second(a,b):
            datalines[i], datalines[j] = datalines[j], datalines[i]
# datalines

# %%
a,b = -1, -1
for i, x in enumerate(datalines):
    if x == '[[2]]':
        a = i
        print(i,x)
    if x == '[[6]]':
        b = i
        print(i,x)
a,b = a+1,b+1           # elves' indexing
print("Product = ", a*b)

# %%

# %%

# %%

# %%
# 19686 too high

# 19392 too low
