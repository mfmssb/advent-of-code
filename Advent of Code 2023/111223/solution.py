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

# I this solution we expand the data `d` with with empty rows and columns.

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

stars = []
for i in range(len(dexp[0])):
    for j in range(len(dexp)):
        if dexp[j][i] == "#":
            stars.append([i, j])

sum_of_dists = 0
for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        [x1, y1] = stars[i]
        [x2, y2] = stars[j]
        sum_of_dists += manhattan_dist(x1, y1, x2, y2)

# ## Løsning

print(sum_of_dists)

# # Oppgave 2

# Implementing expansion factor in the `manhattan_dist` to avoid the large amount of dots (".") in the dataset. Captain Hindsight reports that this would have been a better implementation of problem 1.

d = data[1].split("\n")


# ## Mellomregning

# +
def manhattan_dist_exp(x1, y1, x2, y2, num_gaps_x, num_gaps_y, expansion_factor):
    """
    Calculate the Manhattan distance between two points adjusted by number
    of gaps and the expansion factor
    """
    xdiff = x1 - x2
    ydiff = y1 - y2
    return abs(xdiff) + abs(ydiff) + (num_gaps_x + num_gaps_y) * (expansion_factor - 1)

def find_number_of_elements_between(l: list, num0: int, num1: int):
    """ Use to count the number of gaps between two stars """
    return sum(num0 < x < num1 or num1 < x < num0 for x in l)


# -

def solution2(expansion_factor = 2):
    # Count number of stars
    stars = []
    for i in range(len(d[0])):
        for j in range(len(d)):
            if d[j][i] == "#":
                stars.append([i, j])

    # Number of y gaps
    y_gaps = []
    for j, y in enumerate(d):
        if y == len(d[0])*".":
            y_gaps.append(j)

    # Number of x gaps
    x_gaps = list(range(len(d[0])))
    for j in range(len(d)):
        for i in range(len(d[0])):
            if d[j][i] == "#":
                x_gaps[i] = -1

    x_gaps = [x for x in x_gaps if x != -1]

    x_gaps.sort()
    y_gaps.sort()

    sum_of_dists = 0
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            [x1, y1] = stars[i]
            [x2, y2] = stars[j]

            num_gaps_x = find_number_of_elements_between(x_gaps, x1, x2)
            num_gaps_y = find_number_of_elements_between(y_gaps, y1, y2)

            sum_of_dists += manhattan_dist_exp(x1, y1, x2, y2, num_gaps_x, num_gaps_y, expansion_factor)
    return sum_of_dists


# ## Løsning

# %%timeit
print(solution2(10**6))


