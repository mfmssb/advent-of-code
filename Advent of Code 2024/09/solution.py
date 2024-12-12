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
        if i % 2 == 0:
            datanum = int(num)
            data_id = i // 2
            unpack.extend([str(data_id)] * datanum)
        else:
            free_space = int(num)
            unpack.extend(["."] * free_space)

    return unpack


def parse_diskmap(diskmap: str) -> list:
    unpack = []
    length = len(diskmap)

    # Hvis lengden er partall, er alt jevnt fordelt.
    # Hvis lengden er oddetall, vil siste tegn være en fil-lengde uten fri plass.
    pairs_end = length - (1 if length % 2 == 1 else 0)

    # Behandle alle komplette par (fil, fri plass)
    for i in range(0, pairs_end, 2):
        datanum = int(diskmap[i])
        free_space = int(diskmap[i+1])
        data_id = i // 2

        unpack.extend([data_id] * datanum)
        unpack.extend([-1] * free_space)

    # Hvis vi har et oddetall antall tegn, betyr det at siste tegn er en fil-lengde uten fri plass
    if length % 2 == 1:
        datanum = int(diskmap[-1])
        data_id = pairs_end // 2
        unpack.extend([data_id] * datanum)

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


def find_first_dot(s: list) -> int:
    for i, c in enumerate(s):
        if c == '.':
            return i


def calculate_checksum(s: str) -> int:
    result = 0
    for i, c in enumerate(s):
        if c != ".":
            result += i * int(c)
    return result


def calculate_checksum(blocks: list) -> int:
    result = 0
    for pos, val in enumerate(blocks):
        if val != -1:
            result += pos * val
    return result


d = data[0].split("\n")[0]

len(d)

diskmap = parse_diskmap("123817263812763812763")

num_dots = diskmap.count(".")

num_dots

dot_tail = num_dots * ["."]

while diskmap[-num_dots:] != dot_tail:
    first_dot_i = find_first_dot(diskmap)
    rightmost_non_dot_j = find_rightmost_non_dot(diskmap)
    diskmap = swap_position(diskmap, first_dot_i, rightmost_non_dot_j)

len(diskmap)

calculate_checksum(''.join(diskmap))

# ## Solution 1



# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


