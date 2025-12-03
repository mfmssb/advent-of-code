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


from itertools import combinations
def p2_too_slow(data:list) -> int:
    """
    This code should provide the solution, but it is too slow as i inspects all combinations in the puzzle input.
    The search goes on to find a more optimal sollution
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
    num_remaining -= 1
    if num_remaining == 0:
        return max_bank + max(remaining_bank)
    
    if len(remaining_bank) == num_remaining:
        return max_bank + remaining_bank
    
    stripped_bank = remaining_bank[:-num_remaining]

    max_num = max(stripped_bank)
    max_index = stripped_bank.find(max_num)
    
    new_remaining_bank = remaining_bank[(max_index + 1):]
    max_bank += max_num
    
    new_max_bank = recursive_check_of_remaining_bank(max_bank, new_remaining_bank, num_remaining)
    return new_max_bank


def p2(data, num_batteries_to_turn):
    sum_joltages = 0
    for bank in data:
        max_bank = recursive_check_of_remaining_bank("", bank, num_batteries_to_turn)
        sum_joltages += int(max_bank)
    return sum_joltages


data = parse_data("data/data1.txt")

# %timeit p1(data)

# %timeit p2(data, 2)

# %timeit p2(data, 12)



# +
### TEST SUITE
tests = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]
answers = [
    "987654321111",
    "811111111119",
    "434234234278",
    "888911112111"
]

for (test, answer) in zip(tests, answers):
    try:
        proposal = recursive_check_of_remaining_bank("", test, 12)
        print(test,
              proposal,
              answer, "👌" if answer == proposal else "❌",
              len(proposal))
    except:
        print(test, answer, "⚠️")
