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



# ## Løsning


