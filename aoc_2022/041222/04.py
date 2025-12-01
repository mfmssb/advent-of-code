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
interval_pairs = datastr.split("\n")

def split_string_pair(string_pair):
    list_pair = string_pair.split(",")
    interval1 = list_pair[0]
    interval2 = list_pair[1]
    
    min1 = int(interval1.split("-")[0])
    max1 = int(interval1.split("-")[1])
    min2 = int(interval2.split("-")[0])
    max2 = int(interval2.split("-")[1])

    return (min1, max1, min2, max2)

def is_fully_contained(string_pair):

    (min1, max1, min2, max2) = split_string_pair(string_pair)
   
    if min1 <= min2 and max1 >= max2:
        return True
    if min2 <= min1 and max2 >= max1:
        return True
    return False


# %%
tot = 0
for pair in interval_pairs:
    if is_fully_contained(pair):
        tot += 1
    # print(pair, is_fully_contained(pair))
print(f'Number of assignment pairs where one is fully containing the other: {tot}')


# %%
def is_overlapping(string_pair):
    (min1, max1, min2, max2) = split_string_pair(string_pair)
   
    # Lettere å se på negasjonen av ikke-overlapp
    if not (max1 < min2 or max2 < min1): 
        return True
    return False
tot = 0
for pair in interval_pairs:
    if is_overlapping(pair):
        tot += 1
    # print(pair, is_overlapping(pair))
print(f'Number of assignment pairs where one is overlapping the other: {tot}')
