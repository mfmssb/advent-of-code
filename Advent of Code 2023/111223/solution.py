filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Oppgave 1

d = data[1].split("\n")


# ## Mellomregning

def manhattan_dist(x1, y1, x2, y2):
    xdiff = x1 - x2
    ydiff = y1 - y2
    return abs(xdiff) + abs(ydiff)


dexp = d.copy()

# y expansion
count = 0
for i, y in enumerate(dexp):
    if y == len(dexp[0])*".":
        dexp = dexp[:i + count] + [len(dexp[0])*"."] + dexp[(i + count):]
        count += 1
        # dexp = dexp.insert(i-1, len(dexp[0])*".")

# +
# x expansion
x_gaps = list(range(len(dexp[0])))
for j in range(len(dexp)):
    for i in range(len(dexp[0])):
        if dexp[j][i] == "#":
            x_gaps[i] = -1

x_gaps = [x for x in x_gaps if x != -1]

for j in range(len(dexp)):
    count = 0
    for i in x_gaps:
        dexp[j] = dexp[j][:(i+count)] + "." + dexp[j][(i+count):]
        count += 1
# -

dexp

stars = []
for i in range(len(dexp[0])):
    for j in range(len(dexp)):
        if dexp[j][i] == "#":
            stars.append([i, j])

stars

sum_of_dists = 0
for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        [x1, y1] = stars[i]
        [x2, y2] = stars[j]
        sum_of_dists += manhattan_dist(x1, y1, x2, y2)

# ## Løsning

print(sum_of_dists)

# # Oppgave 2

# ## Mellomregning



# ## Løsning


