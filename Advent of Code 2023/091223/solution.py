filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

d = data[1].split("\n")

p = []
for l in d:
    line = l.split(" ")
    line = [int(x) for x in line]
    p.append(line)


# ## Mellomregning

def is_list_of_zeros(l):
    """ Used to check if a list is all zeros """
    for x in l:
        if x != 0:
            return False
    return True


def diffs_of_progression(l: list):
    """ Calculate all diff rows of a progression. Return list of all diffs. """
    diffs = [l]
    next_diff = l.copy()
    while not is_list_of_zeros(next_diff):
        next_diff = [next_diff[i] - next_diff[i-1] for i in range(1, len(next_diff))]
        diffs.append(next_diff)
    return diffs


def next_number(l: list):
    """ Sum last column of diffs. (This is equivalent of doing the process described in the problem) """
    next_num = 0
    for e in l:
        next_num += e[-1]
    return next_num


# %%time
sum_of_extrapolated_values = 0
for prog in p:
    sum_of_extrapolated_values += next_number(
        diffs_of_progression(
            prog
        )
    )

# ## Løsning

print(sum_of_extrapolated_values)

# # Oppgave 2

d = data[1].split("\n")

p = []
for l in d:
    line = l.split(" ")
    line = [int(x) for x in line]
    p.append(line)


# ## Mellomregning

def prec_number(l: list):
    first_col_in_diff = [x[0] for x in l]
    prec_num = 0
    n = len(first_col_in_diff)
    for i in range(n):
        prec_num = first_col_in_diff[n - i - 1] - prec_num
    return prec_num


# %%time
sum_of_preceding_extrapolated_values = 0
for prog in p:
    sum_of_preceding_extrapolated_values += prec_number(
        diffs_of_progression(
            prog
        )
    )

# ## Løsning

print(sum_of_preceding_extrapolated_values)
