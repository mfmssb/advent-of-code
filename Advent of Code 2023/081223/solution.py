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

graph = {
    'L': {},
    'R': {},
}

for node in nodes:
    key = node.split(" =")[0]
    left = node.split("= (")[1].split(",")[0]
    right = node.split("= (")[1].split(",")[1].replace(")", "").strip()
    
    graph['L'][key] = left
    graph['R'][key] = right

n = 'AAA'
count = 0
while n != 'ZZZ' and count < 100000:
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

nodes[0].split(" =")[0]

start_nodes = [a.split(" =")[0] for a in nodes if a.split(" =")[0].endswith("A")]
end_nodes = [z.split(" =")[0] for z in nodes if z.split(" =")[0].endswith("Z")]

start_nodes

end_nodes

cycles={}
cycles_start={}
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

cycles_start

cycles_length = [len(v) for k, v in cycles.items()]

cycles_length = [x-cycles_start[i] for i, x in enumerate(cycles_length)]

cycles_length

# +
from math import gcd
from functools import reduce

def find_lcm(numbers):
    """ Find the least common multiple (LCM) of a list of numbers. """
    lcm = lambda a, b: a * b // gcd(a, b)
    return reduce(lcm, numbers)

def find_n_values(numbers):
    """ Find the n_i values for each number in the list. """
    lcm_value = find_lcm(numbers)
    n_values = [lcm_value // number for number in numbers]
    return n_values, lcm_value

# Find n_i values and lcm
n_values, lcm_value = find_n_values(cycles_length)
n_values, lcm_value
# -

for i in range(len(cycles_length)):
    print(cycles_length[j]*n_values[j])

len(ins) * 36445519589



visited_nodes



# +
# count = 0
# visited_nodes = []
# node_pos = start_nodes[4]
# while count < 1000:
#     visited_nodes.append(node_pos)
#     for i in ins:
#         node_pos = graph[i][node_pos]

#     if node_pos in visited_nodes:
#         break
    
    
#     count += 1
# -

# count = 0
# while count < 100000:
#     for i in ins:
#         node_pos = [graph[i][n] for n in node_pos]      
#         count += 1
        







# ## Løsning


