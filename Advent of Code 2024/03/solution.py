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


# +
d = data[1]

pattern = "mul[(]\d{1,3}[,]\d{1,3}[)]"
mul_patterns = re.findall(pattern, d)

multiplications = [read_mul_and_calculate(x) for x in mul_patterns]

ans1 = sum(multiplications)
# -

# ## Solution 1

print(ans1)

# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


