filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")

# # Problem 1

# ## Intermediate Steps 1

from itertools import product


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
    result = int(calculation[0])
    if len(calculation) > 1:
        for i in range(2, len(calculation), 2):
            op = calculation[i-1]
            num = int(calculation[i])
            
            if op == '+':
                result += num
            elif op == '*':
                result *= num
            elif op == '||':
                result = int(str(result) + str(num))
            else:
                raise ValueError("Not a valid operator.")
    return result


def calibration_result(data):
    result = 0
    for line in data:
        ans, nums = preprocess(line)
        calculations = insert_operators(nums)
    
        for calculation in calculations:
            if eval_left_to_right(calculation) == ans:
                result += ans
                break
    return result


# ## Solution 1

calibration_result(data[1].split("\n"))


# # Problem 2

# ## Intermediate Steps 2

def fix_concat(calculation: list) -> list:
    while '||' in calculation:
        for i, element in enumerate(calculation):
            if element == '||':
                new_calculation =(calculation[:i-1] +
                                  [calculation[i-1] + calculation[i+1]] +
                                  calculation[i+2:])
                calculation = new_calculation
                break
    return calculation


data = data[1].split("\n")

result = 0
for line in data:
    ans, nums = preprocess(line)
    calculations = insert_operators(nums, operators=['+', '*', '||'])
    
    for calculation in calculations:
        if eval_left_to_right(calculation) == ans:
            result += ans
            break

# ## Solution 2

ans2 = result
print(ans2)


