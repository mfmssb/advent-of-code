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

import re


def read_mul_and_calculate(s: str) -> int:
    s2 = s.replace("mul(", "").replace(")", "")
    split_s = s2.split(",")
    if len(split_s) != 2:
        raise ValueError("Given multiplication does not have two factors:", split_s)

    for x in split_s:
        try: 
            int(x)
        except:
            raise ValueError("Not numeric factor", s, s2, split_s, x)
    
    return int(split_s[0]) * int(split_s[1])


def findall_muls(s: str) -> list:
    pattern = r"mul[(]\d{1,3}[,]\d{1,3}[)]"
    return re.findall(pattern, s)


# +
d = data[1]

mul_patterns = findall_muls(d)
multiplications = [read_mul_and_calculate(mul) for mul in mul_patterns]

ans1 = sum(multiplications)
# -

# ## Solution 1

print(ans1)

# # Problem 2

# ## Intermediate Steps 2

# Fikk hjelp av ChatGPT til denne. Today I learned `re.finditer()` og `.group()`...

# Prøvde først å splitte på `don't()`, ta vare på de første `mul()` og for hver undersekvens lete etter `do()` og hente etterfølgende `mul()`. Er fortsatt litt usikker på hvorfor dette feilet.

d = data[1]

pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

instructions = re.finditer(pattern, d)

enabled = True
multiplications = []

for instr in instructions:
    s = instr.group()
    if s == "do()":
        enabled = True
    elif s == "don't()":
        enabled = False
    elif s.startswith("mul(") and enabled:
        result = read_mul_and_calculate(s)
        multiplications.append(result)

ans2 = sum(multiplications)

# ## Solution 2

print(ans2)


