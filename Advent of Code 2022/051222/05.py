# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %% [markdown]
# # Prep av indata
#

# %%

f = open("data.txt", "r")
datastr = f.read()
indata_split = datastr.split(" \n\n")

box_state = indata_split[0]
move_data = indata_split[1]

box_state_list = box_state.split("\n")
boxes_height = len(box_state_list)
boxes_turned = []

for i in range(boxes_height):
    boxes_turned.append(box_state_list[boxes_height - i - 1])
boxes_width = len(boxes_turned[0].replace(" ", ""))

stacks = [[] for _ in range(boxes_width) ] # deklarerer tom tabell

for i in range(boxes_width):
    for j in range(boxes_height):
        stacks[i].append(boxes_turned[j][4*i+1])

for i in range(boxes_height):
    # fjerner tomme elementer
    stacks[i] = list(filter(lambda item: item != ' ', stacks[i]))


# %%
def remove_box_from_stack(number):
    box_letter = stacks[number-1][-1]
    del stacks[number-1][-1]
    return box_letter

def add_box_to_stack(box_letter, number):
    stacks[number-1].append(box_letter)


# %% [markdown]
# # Del 1

# %%
moves = move_data.split("\n")
for move in moves:
    # splitter opp teksten og konverterer strengtall til int
    a = move.split(" from ")
    b = a[0].replace("move ", "")
    c = a[1].split(" to ")

    number_of_boxes_to_move = int(b)
    from_stack = int(c[0])
    to_stack = int(c[1])

    for i in range(number_of_boxes_to_move):
        box_letter = remove_box_from_stack(from_stack)
        add_box_to_stack(box_letter, to_stack)

# %%
solution1 = ""
for stack in stacks:
    solution1 += stack[-1]
solution1

# %% [markdown]
# # Prep igjen

# %%
f = open("data.txt", "r")
datastr = f.read()
indata_split = datastr.split(" \n\n")

box_state = indata_split[0]
move_data = indata_split[1]

box_state_list = box_state.split("\n")
boxes_height = len(box_state_list)
boxes_turned = []

for i in range(boxes_height):
    boxes_turned.append(box_state_list[boxes_height - i - 1])
boxes_width = len(boxes_turned[0].replace(" ", ""))

stacks = [[] for _ in range(boxes_width) ] # deklarerer tom tabell

for i in range(boxes_width):
    for j in range(boxes_height):
        stacks[i].append(boxes_turned[j][4*i+1])

for i in range(boxes_height):
    # fjerner tomme elementer
    stacks[i] = list(filter(lambda item: item != ' ', stacks[i]))


# %%
def remove_boxes_from_stack(number_of_boxes_to_move, stack_number):
    box_letters = ""
    for i in range(number_of_boxes_to_move):
        box_letters += remove_box_from_stack(stack_number)
    box_letters = box_letters[::-1] # reverserer strengen
    
    return box_letters

def add_boxes_to_stack(box_letters, stack_number):
    for l in box_letters:
        add_box_to_stack(l, stack_number)



# %% [markdown]
# # Del 2

# %%
moves = move_data.split("\n")
for move in moves:
    # splitter opp teksten og konverterer strengtall til int
    a = move.split(" from ")
    b = a[0].replace("move ", "")
    c = a[1].split(" to ")

    number_of_boxes_to_move = int(b)
    from_stack = int(c[0])
    to_stack = int(c[1])

    box_letters = remove_boxes_from_stack(number_of_boxes_to_move, from_stack)
    add_boxes_to_stack(box_letters, to_stack)


# %%
solution2 = ""
for stack in stacks:
    solution2 += stack[-1]
solution2
