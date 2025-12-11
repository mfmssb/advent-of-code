from pathlib import Path

def parse_data(data_path: str) -> dict[str, list[str]]:
    f"""
    Store data as dictionary with connection in as the key and the corresponding
    connections out as a list. Each key is assumed unique.
    {
        "you": ["bbb", "ccc"]
        ...
    }
    """
    lines: list[str] = Path(data_path).read_text().strip().splitlines()
    result: dict[str, list[str]]= {
        first: rest.split()
        for first, rest in (s.split(": ", 1) for s in lines)
    }
    return result

def p1(data_path) -> int:
    """
    This code assumes that there are no loops.
    If i.e. "bbb" -> "ccc" -> "bbb" the code will not provide an answer.
    """
    devices = parse_data(data_path)
    path_list = [["you"]]

    while(True):
        next_step = []
        # Loop through all connections from last step
        for c_in in path_list[-1]:
            if c_in == "out":
                # If next devices says "out", copy it
                next_step += ["out"]
            else:
                # Find the next devices and add to next_step list
                c_out = devices[c_in]
                next_step += c_out
        
        path_list.append(next_step)
        # Break when all of the next devices in list says "out"
        if set(next_step) == {"out"}:
            break
    # Answer is the length of the list of "out"s
    return len(path_list[-1])
# %%
p1("/home/onyxia/work/advent-of-code/aoc_2025/11/data/data1.txt") # 323 μs
# %%
