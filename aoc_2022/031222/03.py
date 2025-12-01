# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %%
f = open("data.txt", "r")
datastr = f.read()
rucksacks = datastr.split("\n")

lowercase_letters_str = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters_str = lowercase_letters_str.upper()
all_letters = (lowercase_letters_str + uppercase_letters_str)

def priority(letter):
    for i in range(len(all_letters)):
        if all_letters[i] == letter:
            return i + 1
    print("ERROR Priority")
    return

def first_common_letter(str1, str2):
    for a in str1:
        for b in str2:
            if a == b:
                return a
    return "ERROR fcl"


tot = 0
for r in rucksacks:
    split_index = int(len(r)/2)
    part1 = r[:split_index]
    part2 = r[split_index:]
    unique = first_common_letter(part1, part2)
    tot += priority(unique)
print(f"First star answer: {tot}")


# %%
def only_common_letter(str1, str2, str3):
    for a in str1:
        for b in str2:
            for c in str3:
                if a == b and b == c:
                    return a
    return "ERROR ocl"


# %%
number_of_groups = int(len(rucksacks)/3)

tot = 0
for i in range(0, number_of_groups):
    r1 = rucksacks[3*i]
    r2 = rucksacks[3*i+1]
    r3 = rucksacks[3*i+2]
    unique = only_common_letter(r1, r2, r3)
    tot += priority(unique)
print(f"Second star answer: {tot}")
    
