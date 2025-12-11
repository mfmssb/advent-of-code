# %%
from pathlib import Path
import itertools

def string_to_tuple(s: str, parenthesis: str) -> tuple[int, ...]:
    s = s.replace(parenthesis[0], "").replace(parenthesis[1], "")
    s = s.split(",")

    return tuple([int(x) for x in s])

def parse_data(data_path: str):
    lines: list[str] = Path(data_path).read_text().strip().splitlines()
    
    return [
        [
            line.split(" ")[0].replace("[", "").replace("]", ""),
            [string_to_tuple(s, "()") for s in line.split()[1:-1]],
            string_to_tuple(line.split()[-1], "{}"),
        ]
        for line in lines
    ]

def flip_light(i: int, state) -> str:
    flipped = "#" if state[i] == "." else "."
    return state[:i] + flipped + state[i+1:]

# %%
def push_button(button: tuple, state: str) -> str:
    new_state = state
    for i in button:
        new_state = flip_light(i, new_state)
        
    return new_state

def get_all_button_combinations(buttons:list[tuple]):
    choices = [(None, t) for t in buttons]

    all_combinations = []
    for combo in itertools.product(*choices):
        picked = tuple(x for x in combo if x is not None)
        all_combinations.append(picked)

    all_combinations = list(itertools.compress(all_combinations, [bool(t) for t in all_combinations]))

    return all_combinations

def get_successful_combinations(button_combinations: list, goal: str):
    successful_combinations = []
    for comb in button_combinations:
        state = "." * len(goal)
        for button in comb:
            state = push_button(button, state)
        if state == goal:
            successful_combinations.append(comb)
    return successful_combinations


# %%
def p1(data_path) -> int:
    machines = parse_data(data_path)
    sum_total_button_presses = 0
    for machine in machines:
        goal, buttons, _ = machine
        
        button_combinations = get_all_button_combinations(buttons)
        successfull_combinations = get_successful_combinations(button_combinations, goal)

        smallest_number_of_button_presses = min([len(x) for x in successfull_combinations])
        sum_total_button_presses += smallest_number_of_button_presses

    return sum_total_button_presses

# %%
p1("/home/onyxia/work/advent-of-code/aoc_2025/10/data/data1.txt")
# %%
def p2(data_path):
    
    return

p2("/home/onyxia/work/advent-of-code/aoc_2025/10/data/data1.txt")
# %%
