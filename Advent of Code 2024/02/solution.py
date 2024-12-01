filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

d = data[0].split("\n")

# ## Intermediate Steps 1



# ## Solution 1



# # Problem 2

# ## Intermediate Steps 2



# ## Solution 2


