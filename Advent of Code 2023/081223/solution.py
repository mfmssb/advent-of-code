filnavn = ["data0.txt", "data1.txt", "data2.txt", "data3.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

# ## Mellomregning

d = data[2].split("\n")

# +
ins = d[0]

nodes = d[2:]
# -

# Split the graph into "L" and "R".
graph = {
    'L': {},
    'R': {},
}

for node in nodes:
    _from = node.split(" =")[0]
    left = node.split("= (")[1].split(",")[0]
    right = node.split("= (")[1].split(",")[1].replace(")", "").strip()
    
    graph['L'][_from] = left
    graph['R'][_from] = right

start_node = 'AAA'
count = 0
while start_node != 'ZZZ' and count < 100000:
    for i in ins:
        n = graph[i][n]
        count += 1

# ## Løsning

count

# # Oppgave 2

d = data[2].split("\n")

# +
ins = d[0]

nodes = d[2:]
# -

graph = {
    'L': {},
    'R': {},
}

# ## Mellomregning

for node in nodes:
    key = node.split(" =")[0]
    left = node.split("= (")[1].split(",")[0]
    right = node.split("= (")[1].split(",")[1].replace(")", "").strip()
    
    graph['L'][key] = left
    graph['R'][key] = right

# +
start_nodes = [a.split(" =")[0] for a in nodes if a.split(" =")[0].endswith("A")]
end_nodes = [z.split(" =")[0] for z in nodes if z.split(" =")[0].endswith("Z")]

print("Start nodes:\t", start_nodes)
print("End nodes:\t", end_nodes)
# -

# The key insight here is that each ghost must somewhere in its path go into a loop (this can be observed by taking more than `len(nodes)` steps).
#
# In the next code snippet I search for where in their paths each ghost start over in the loop. I also find which index it goes back to (`cycles_start`)

cycles = {}
cycles_start = {}
for j in range(len(start_nodes)):
    visited_nodes = []
    node_pos = start_nodes[j]
    count = 0
    while count < 1000:
        visited_nodes.append(node_pos)
        for i in ins:
            node_pos = graph[i][node_pos]

        if node_pos in visited_nodes:
            break
        count += 1
    cycles[j] = visited_nodes
    cycles_start[j] = [i for i, x in enumerate(visited_nodes) if x == node_pos][0]

# Calculate the length of cycles, and subtract the cycle start index
# The cycle start index is conveniently 1 for each ghost.
cycles_length = [len(v) for k, v in cycles.items()]
cycles_length = [x-cycles_start[i] for i, x in enumerate(cycles_length)]  # The length of each cycle

# +
# We find the least common multiple (minste felles multiplum) of the cycles length
# to determine how many steps each ghost must take to line up at the same spot

from math import gcd
from functools import reduce

def find_lcm(numbers):
    """ Find the least common multiple (LCM) of a list of numbers. """
    lcm = lambda a, b: a * b // gcd(a, b)
    return reduce(lcm, numbers)

def find_n_values(numbers):
    """
    Find the n_i values for each number in the list.
    n_i is the number of steps each ghost must take to line up with the other cycles.
    This is not needed for the puzzle, but I used it to check the logic.
    """
    lcm_value = find_lcm(numbers)
    n_values = [lcm_value // number for number in numbers]
    return n_values, lcm_value

# Find n_i values and lcm
n_values, lcm_value = find_n_values(cycles_length)
n_values, lcm_value
# -

# ## Løsning

# The ghosts must do these cycles for every instruction list.
len(ins) * lcm_value
# In the step after this they will all be at the cycle start index,
# so this is the "last" step before doing it all over.
