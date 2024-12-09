filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")

# # Problem 1

d = data[1].split("\n")

# ## Intermediate Steps 1

from itertools import product


def evaluer(a, b, op):
    return eval(a, b, op)


def preprocess(line: str) -> (int, list):
    line_split = line.split(":")
    ans = int(line_split[0])
    nums_str = line_split[1]

    numbers = nums_str.split(" ")
    numbers = [x for x in numbers if x != '']
    return (ans, numbers)


def insert_operators(numbers: list, operators=['+', '*']) -> list:
    operator_combinations = list(product(operators, repeat=len(numbers)-1))
    results = []
    for combo in operator_combinations:
        parts = []
        for i, n in enumerate(numbers):
            parts.append(str(n))
            if i < len(combo):
                parts.append(combo[i])
        results.append(parts)
    return results


def eval_left_to_right(calculation: list) -> int:
    result = calculation[0]
    for i in range(2, len(calculation), 2):
        op = calculation[i-1]
        num = calculation[i]
        
        result = eval(f"{result}{op}{num}")
    return result


calibration_result = 0
for line in d:
    ans, nums = preprocess(line)
    calculations = insert_operators(nums)
    answers = [eval_left_to_right(calculation) for calculation in calculations]

    if ans in answers:
        calibration_result += ans
        

calibration_result

# ## Solution 1





# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


