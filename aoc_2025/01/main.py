# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
direction_mapping = {
    "R": 1,
    "L": -1
}


# %%
def parse_data(data_path: str) -> list:
    with open(data_path, 'r') as file:
        content = file.read()
    return content.split("\n")


# %%
def p1(data_path: str,
       tot_dial_numbers: int,
       goal_index: int,
       dial_start_index: int) -> int:

    data = parse_data(data_path)

    current_dial_index = dial_start_index
    goal_count = 0
    
    for r in data:
        direction = r[0]
        num_steps = int(r[1:])
        num_steps_dir = direction_mapping[direction] * num_steps
        current_dial_index = (current_dial_index + num_steps_dir) % tot_dial_numbers
        goal_count += 1 if current_dial_index == goal_index else 0
    
    return goal_count


# %%
def p2(data_path: str,
       tot_dial_numbers: int,
       goal_index: int,
       dial_start_index: int) -> int:
    import math
    data = parse_data(data_path)

    current_dial_index = dial_start_index
    goal_count = 0
    
    for r in data:
        direction = r[0]
        num_steps = int(r[1:])
        
        num_steps_revolutions = math.floor(num_steps / tot_dial_numbers)
        num_steps_remainder = num_steps - num_steps_revolutions * tot_dial_numbers

        num_steps_remainder_dir = num_steps_remainder * direction_mapping[direction]
         
        goal_count += num_steps_revolutions

        new_index = current_dial_index + num_steps_remainder_dir

        if current_dial_index != 0 and not 0 < new_index < tot_dial_numbers:
            goal_count += 1
        
        current_dial_index = new_index % tot_dial_numbers
    return goal_count


# %%
# %%timeit
p1(data_path="data/data1.txt",
   tot_dial_numbers=100,
   goal_index=0,
   dial_start_index=50
)

# %%
# %%timeit
p2(
    data_path="data/data1.txt",
    tot_dial_numbers=100,
    goal_index=0,
    dial_start_index=50
)

# %%
