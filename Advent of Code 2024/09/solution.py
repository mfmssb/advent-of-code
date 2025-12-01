filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")


# # Problem 1

# The digits alternate between indicating the length of a file and the length of free space.
#
# So, a disk map like 12345 would represent a one-block file, two blocks of free space, a three-block file, four blocks of free space, and then a five-block file. A disk map like 90909 would represent three nine-block files in a row (with no free space between them).

# ## Intermediate Steps 1

def parse_diskmap(diskmap: str) -> list:
    unpack = []
    for i, num in enumerate(diskmap):
        length = int(num)
        if i % 2 == 0:
            # Filblokk
            file_id = i // 2
            unpack.extend([file_id] * length)
        else:
            # Fri plass
            unpack.extend(["."] * length)
    return unpack



def swap_position(s: list, i, j) -> list:
    s[i], s[j] = s[j], s[i]
    return s


def find_rightmost_non_dot(s: list) -> int:
    for i in range(len(s)):
        j = len(s) - i - 1
        if s[j] != ".":
            break
    return j


def find_dot_from_index(s: list, from_index=0) -> int:
    for i, c in enumerate(s[from_index:], start=from_index):
        if c == '.':
            return i
    raise ValueError("No dots found")


def calculate_checksum(s: list) -> int:
    result = 0
    for i, c in enumerate(s):
        if c != ".":
            result += i * c
    return result


d = data[1].split("\n")[0]

diskmap = parse_diskmap(d)

num_dots = diskmap.count(".")

dot_tail = num_dots * ["."]

# %%time
while diskmap[-num_dots:] != dot_tail:
    first_dot_i = find_dot_from_index(diskmap)
    rightmost_non_dot_j = find_rightmost_non_dot(diskmap)
    diskmap = swap_position(diskmap, first_dot_i, rightmost_non_dot_j)

ans1 = calculate_checksum(diskmap)

# ## Solution 1

print(ans1)


# # Problem 2

# ## Intermediate Steps 2

def file_indexes(s: list) -> tuple:
    i = find_rightmost_non_dot(s)
    file_id = s[i]
    length = 1
    while s[i-length] != file_id:
        length += 1
    return (i, length)


def get_dot_length(s: list), from_index: int) -> tuple:
    i = find_dot_from_index(s, from_index)
    length = 1
    while s[i+length] != ".":
        length += 1
    return (i, length)


# +
d = data[0].split("\n")[0]

diskmap_raw = parse_diskmap(d)
diskmap = diskmap_raw[::]
num_dots = diskmap.count(".")
dot_tail = num_dots * ["."]
# -



# %%time
while diskmap[-num_dots:] != dot_tail:
    dot_i = 0
    cont = True
    while (dot_i < len(diskmap) & cont):
        (dot_i, length_dots) = get_dot_length(diskmap)
        (fileindex_right, length_file) = file_indexes(diskmap)
    
        if length_dots >= length_file:
            # swap positions
            cont = False

    
    first_dot_i = find_first_dot(diskmap)
    rightmost_non_dot_j = find_rightmost_non_dot(diskmap)
    diskmap = swap_position(diskmap, first_dot_i, rightmost_non_dot_j)

d

diskmap_raw

"".join([str(x) for x in diskmap_raw])

"".join([str(x) for x in diskmap])

# ## Solution 2


