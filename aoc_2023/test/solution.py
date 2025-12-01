# # Day 2 2021

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

# +
mapping = {"forward": "x = x +", "up": "y = y -", "down": "y = y +"}

_input = data[1]

for k, v in mapping.items():
    _input = _input.replace(k, v)

instruks = _input.split("\n")

x, y = 0, 0

for i in instruks:
    exec(i)

print(x, y)
# -

# ## Løsning

print(x*y)

# # Oppgave 2

# ## Mellomregning

instruks = data[2].split("\n")

x, y, aim = 0, 0, 0

for i in instruks:
    value = int(i.split(" ")[1])
    if i.startswith("forward"):
        x += value
        y = y + aim*value
    if i.startswith("down"):
        aim += value
    if i.startswith("up"):
        aim -= value

# - forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
# - down 5 adds 5 to your aim, resulting in a value of 5.
# - forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
# - up 3 decreases your aim by 3, resulting in a value of 2.
# - down 8 adds 8 to your aim, resulting in a value of 10.
# - forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.

# ## Løsning

print(x*y)
