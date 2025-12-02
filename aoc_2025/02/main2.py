import math


def parse_data(data_path: str) -> list:
    with open(data_path, 'r') as file:
        content = file.readlines()
    return content[0].split(",")


def is_valid1(id_str: str) -> bool:
    id_length = len(id_str)
    if id_length % 2 == 1:
        return True
    
    half_index = int(id_length/2)
    
    id_part1 = id_str[:half_index]
    id_part2 = id_str[half_index:]
    
    return id_part1 != id_part2


def proper_divisors(n: int) -> list:
    """
    Return list of all proper divisors of n.
    proper_divisors(6)
        [1, 2, 3]
    """
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            divs.extend([i, n/i])
        
    return [int(x) for x in list(set(divs))]


def is_valid2(id_str: str) -> bool:
    """
    Check all partitions of an id split into equal parts

    is_valid2("123123")
        length is 6 -> can be split into equal parts of length 1, 2 and 3
        ["1", "2", "3", "1", "2", "3"]  # not equal
        ["12", "31", "23"]  # not equal
        ["123", "123"]  # equal, so "123123" is not valid
    """
    id_length = len(id_str)
    if id_length == 1:
        return True
        
    length_divisors = proper_divisors(id_length)
    for d in length_divisors:
        partitions = []
        for i in range(0, id_length, d):
            partitions.append(id_str[i:i+d])
        if len(set(partitions)) == 1:
            return False
    return True


def p(data, is_valid):
    id_sum = 0
    for interval in data:
        from_, to_ = interval.split("-")
        for i in range(int(from_), int(to_) + 1):
            id_str = str(i)
            if not is_valid(id_str):
                id_sum += i
    return id_sum


data = parse_data("data/data1.txt")

print("Part 1:", p(data, is_valid1))
print("Part 2:", p(data, is_valid2))

# %timeit p(data, is_valid1)

# %timeit p(data, is_valid2)


