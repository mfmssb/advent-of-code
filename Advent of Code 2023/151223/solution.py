filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

d = data[1].split(",")

len(d)


# ## Intermediate Steps 1

def apply_hash_rules(char, current):
    current += ord(char)
    current *= 17
    current = current % 256
    return current


start = 0
tot = 0
for seq in d:
    current = start
    for char in seq:
        current = apply_hash_rules(char, current)
    tot += current

# ## Solution 1

# %%time
print(tot)

# ---

# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


