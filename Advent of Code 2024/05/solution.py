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

d = data[1].split("\n\n")
rules = d[0].split("\n")
updates = d[1].split("\n")

for rule in rules:
    split = rule.split('|')
    left = split[0]
    right = split[1]
    
    for u in updates:
        if (u.count(left) > 1) | (u.count(right) > 1):
            raise ValueError("There are updates with duplicate pages", rule, u)

updates_in_order = []
for i, update in enumerate(updates):
    is_in_order = True
    for rule in rules:
        split = rule.split('|')
        left = split[0]
        right = split[1]

        left_index_in_update = update.find(left)
        right_index_in_update = update.find(right)

        if (left_index_in_update > right_index_in_update) & (right_index_in_update != -1):
            is_in_order = False
            continue

    if is_in_order:
        updates_in_order.append(update)

sum_mid_pages = 0
for update in updates_in_order:
    split = update.split(",")
    mid_index = int(len(split) / 2)
    sum_mid_pages += int(split[mid_index])

ans1 = sum_mid_pages

# ## Solution 1

print(ans1)



# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


