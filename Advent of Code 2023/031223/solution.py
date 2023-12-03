filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

# ## Mellomregning

engine = data[1].split("\n")


def find_indices_of_number_from(i: int, j: int, e: list) -> list:
    """
    Returns a list of the indices of a number in the engine
    i: x-coordinate
    j: y-coordinate
    e: engine map
    """
    indices = []
    while check_valid_index(i, j, e):
        if e[j][i].isdigit():
            indices.append((i, j))
        else:
            break
        i += 1
    return indices



def check_valid_index(i: int, j: int, e: list) -> bool:
    """
    Returns True if index (i, j) is valid
    i: x-coordinate
    j: y-coordinate
    e: engine map
    """
    return 0 <= i < len(engine[0]) and 0 <= j < len(engine)


def print_number(l: list, e: list) -> int:
    """
    Returns number from an index list.
    l: A list of indices retrieved from find_indices_of_number_from()
    """
    num = ""
    for x in l:
        num += e[x[1]][x[0]]
    return int(num)


def is_part_symbol(s: str) -> bool:
    """
    Returns True if input string is not "." or numeric
    """
    return s not in ".0123456789"


def is_engine_part(indices: list, e: list) -> bool:
    """
    Returns True if one of the adjacent cells of input index-list is a part symbol
    """
    if not indices:
        return False
    
    x0, y0 = indices[0]
    xn, yn = indices[-1]

    for j in [y0 - 1, y0, y0 + 1]:
        for i in range(x0 - 1, xn + 2):
            if check_valid_index(i, j, engine) and is_part_symbol(engine[j][i]):
                return True
    return False


# Loop through engine map from top left and search for numbers and adjacent engine parts
sum_of_parts = 0
j = 0
while j < len(engine):
    i = 0
    while i < len(engine[j]):
        if engine[j][i].isdigit():
            indices = find_indices_of_number_from(i, j, engine)
            i += len(indices)-1
            # print(indices, print_number(indices, engine), is_engine_part(indices, engine))
            if is_engine_part(indices, engine):
                sum_of_parts += print_number(indices, engine)
        i += 1
    j += 1

# ## Løsning

print(sum_of_parts)


# # Oppgave 2

# ## Mellomregning

def index_of_adjacent_star(indices: list, e: list) -> list:
    """
    Modified version of is_engine_part(). Searches adjacent cells for "*" and returns index of the star if it is found.
    """
    if not indices:
        return []
    
    x0, y0 = indices[0]
    xn, yn = indices[-1]

    for j in [y0 - 1, y0, y0 + 1]:
        for i in range(x0 - 1, xn + 2):
            if check_valid_index(i, j, engine) and engine[j][i] == "*":
                return [i, j]
    return []


# Loop through engine map from top left
# If number is found, search for adjacent "*" and append star index and number index to star_list
star_list = []
j = 0
while j < len(engine):
    i = 0
    while i < len(engine[j]):
        if engine[j][i].isdigit():
            indices = find_indices_of_number_from(i, j, engine)
            
            # print(indices, print_number(indices, engine), is_engine_part(indices, engine))
            star_index = index_of_adjacent_star(indices, engine)
            if len(star_index) > 0:
                star_list.append([star_index, [i, j]])
            i += len(indices)-1
        i += 1
    j += 1

# +
# Group all star indices as dict key, and set dict values of numbers adjacent to star as value
star_dict = {}
for pair in star_list:
    key = tuple(pair[0])
    if key not in star_dict:
        star_dict[key] = []

    star_dict[key].append(pair[1])

# Throw all stars with just one entry (No cases of more than two numbers)
star_dict = {key: value for key, value in star_dict.items() if len(value) == 2}
# -

# Loop through star_dict and apply print_number() to retrieve numeric value from indices.
# Calculate gear ratio and add
sum_ratios = 0
for k, v in star_dict.items():
    indices1 = find_indices_of_number_from(v[0][0], v[0][1], engine)
    indices2 = find_indices_of_number_from(v[1][0], v[1][1], engine)
    
    # print(indices1, print_number(indices1, engine))
    # print(indices2, print_number(indices2, engine))
    gear_ratio = print_number(indices1, engine) * print_number(indices2, engine)
    sum_ratios += gear_ratio
    # print(50*"-")

# ## Løsning

sum_ratios
