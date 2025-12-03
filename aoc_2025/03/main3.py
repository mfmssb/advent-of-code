from itertools import combinations


def parse_data(data_path: str) -> list:
    with open(data_path, 'r') as file:
        content = file.read()
    return content.split("\n")


def p1(data: list) -> int:
    sum_joltages = 0
    for bank in data:
        maximum_joltage = 0
        for i in range(len(bank)-1):
            for j in range(i+1, len(bank)):
                left = bank[i]
                right = bank[j]
                joltage = int(left + right)
                if joltage > maximum_joltage:
                    maximum_joltage = joltage
        sum_joltages += maximum_joltage
    return sum_joltages


# +
data = parse_data("data/data0.txt")

p1(data)


# -

def p2_too_slow(data:list) -> int:
    """
    This code should provide the solution, but it is too slow as i inspects all combinations in the puzzle input
    """
    sum_joltages = 0
    for bank in data:
        max_joltage = 0
        max_combination = ()
        for x in combinations(bank, 12):
            comb = ("").join(list(x))
            num_com = int(comb)
            if  num_com > max_joltage:
                max_joltage = num_com
        sum_joltages += max_joltage
    return sum_joltages


def recursive_check_of_remaining_bank(max_bank, remaining_bank, num_remaining):
    if num_remaining == 0:
        return max_bank
    
    stripped_bank = remaining_bank[:-num_remaining]
    max_num = max(stripped_bank)
    max_index = stripped_bank.find(max_num)
    
    new_remaining_bank = remaining_bank[(max_index + 1):]

    if new_remaining_bank == remaining_bank:
        return max_bank + remaining_bank
    max_bank += max_num
    
    # print(f"{max_bank}, {new_remaining_bank}, {num_remaining}", )
    
    new_max_bank = recursive_check_of_remaining_bank(max_bank, new_remaining_bank, num_remaining - 1)
    return new_max_bank


test = recursive_check_of_remaining_bank("", "818181911112111", 12)
print(test)
test == "888911112111"

test

test == "987654321111"

len(test)

len("234234234234278")

len("234234234278")

"234234234278"[-11]

remaining_bank = '819181911112111'

num_remaining = 6

stripped_bank = remaining_bank[:-num_remaining]

max_num = max(stripped_bank)
max_index = stripped_bank.find(max_num)

new_remaining_bank = remaining_bank[(max_index + 1):]

new_remaining_bank

p2(data)
