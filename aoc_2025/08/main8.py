# %%
from pathlib import Path
from itertools import combinations
import pandas as pd

def parse_data(data_path: str) -> list[tuple[int, ...]]:
    data: list[str] = Path(data_path).read_text().split("\n")
    data: list[str] = [tuple(x.split(",")) for x in data]
    return [tuple(int(x) for x in tup) for tup in data]


def square_distance_between(p1, p2) -> int:
    """
    Calculate the square distance between to points (tuples).
    The square root is not needed to establish the order of distances.
    """
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2

    return ((x1 - x2) ** 2
            + (y1 - y2) ** 2
            + (z1 - z2) ** 2)

def p1(data_path: str) -> int:
    """
    This solution utilizes Python sets {} to store unordered unique points.
    """
    if data_path[-5] == "0":
        number_of_junctions_to_check = 10
    else:
        number_of_junctions_to_check = 1000
    
    points: list[tuple[int, ...]] = parse_data(data_path)
    pairs: list[tuple[set[tuple[int, ...]], int]]= [
        ({p1, p2}, square_distance_between(p1, p2))
        for p1, p2 in combinations(points, 2)
    ]
    # sort by square distance
    pairs.sort(key=lambda x: x[1])

    # trim the list
    pairs = pairs[:number_of_junctions_to_check]  
    
    # get rid of distance and consider each pair a circuit
    circuits = [pair for pair, _ in pairs]  
    
    # loop through circuits and join to circuits if the share a point
    for c1 in circuits:
        for c2 in circuits:
            if c1 != c2:
                for p in c1:
                    if p in c2:
                        c2.update(c1)

    # today I learned about frozensets to make them hashable
    # get rid of duplicated circuits
    unique_circuits = [set(fs) for fs in {frozenset(s) for s in circuits}]

    circuit_lengths = [len(x) for x in unique_circuits]
    
    # calculate the product of the three largest circuits
    circuit_lengths.sort()
    product = 1
    for length in circuit_lengths[-3:]:
        product *= length
    return product
# %%
p1("/home/onyxia/work/advent-of-code/aoc_2025/08/data/data1.txt")
# %%
