filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

# ## Mellomregning

d = data[1].split("\n")
NUMERALS = "0123456789"

calibration_nums = []

for line in d:
    nums_in_line = []
    for char in line:
        if char in NUMERALS:
            nums_in_line.append(char)
    calibration_nums.append(nums_in_line[0] + nums_in_line[-1])


calibration_nums = [int(x) for x in calibration_nums]

# ## Løsning

sum(calibration_nums)

# # Oppgave 2

# ## Mellomregning

# +
d = data[1].split("\n")

NUMERALS_SPELLED = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
NUMERALS_STR = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# -

NUM_DICT = dict(zip(NUMERALS_SPELLED, NUMERALS_STR))

NUM_DICT

calibration_nums = []

for line in d:
    nums_in_line = []
    for i in range(len(line)):
        if line[i] in ("").join(NUMERALS_STR):
            nums_in_line.append((line[i], i))
    
    for num_s in NUMERALS_SPELLED:
        indexl = line.find(num_s)
        if indexl > -1:
            nums_in_line.append((num_s, indexl))
        indexr = line.rfind(num_s)
        if indexr > -1:
            nums_in_line.append((num_s, indexr))    
    calibration_nums.append(nums_in_line)


# +
calibration_nums_fixed = []

for c in calibration_nums:
    indecies = {"first_index": 10**10, "last_index": -1}

    for c_tuple in c:
        if c_tuple[1] < indecies["first_index"]:
            indecies["first_index"] = c_tuple[1]
        if c_tuple[1] > indecies["last_index"]:
            indecies["last_index"] = c_tuple[1]

    values = {"first_value": None, "last_value": None}
    for i in range(len(c)):
        if c[i][1] == indecies["first_index"]:
            values["first_value"] = c[i][0]
        if c[i][1] == indecies["last_index"]:
            values["last_value"] = c[i][0]
    values = {key: NUM_DICT.get(value, value) for key, value in values.items()}
    calibration_nums_fixed.append(int(values["first_value"] + values["last_value"]))

# +
# list(zip(calibration_nums_fixed, d))
# -

# ## Løsning

sum(calibration_nums_fixed)

sum(calibration_nums_fixed)

# ## Løsning


