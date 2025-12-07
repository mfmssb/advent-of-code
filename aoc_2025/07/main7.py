# %%
from typing import Any


import os
from pathlib import Path

def parse_data(data_path: str):
    data: list[str] = Path(data_path).read_text().split("\n")

    return data

def insert_ch_in_str_at(s: str, ch: str, index: int) -> str:
    return s[:index] + ch + s[index+1:]

def p1(data_path: str):
    data = parse_data(data_path)
    for y in range(1, len(data)):
        prev_row = data[y-1]

        for x in range(len(prev_row)):
            if prev_row[x] in ["S", "|"] and data[y][x] != "^":
                data[y] = insert_ch_in_str_at(data[y], "|", x)
            if data[y][x] == "^":
                if x - 1 >= 0:
                    data[y] = insert_ch_in_str_at(data[y], "|", x-1)
                if x + 1 < len(data[y]):
                    data[y] = insert_ch_in_str_at(data[y], "|", x+1)
    counter = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == "^" and data[y-1][x] == "|":
                counter += 1
    return counter
    
# %%
p1('/home/onyxia/work/advent-of-code/aoc_2025/07/data/data1.txt')
# %%
data_path = '/home/onyxia/work/advent-of-code/aoc_2025/07/data/data0.txt'
data = parse_data(data_path)

for y in range(1, len(data)):
    prev_row = data[y-1]
    for x in range(len(prev_row)):
        if prev_row[x] in ["S", "|"] and data[y][x] != "^":
            data[y] = insert_ch_in_str_at(data[y], "|", x)
        if data[y][x] == "^":
            if x - 1 >= 0:
                data[y] = insert_ch_in_str_at(data[y], "|", x-1)
            if x + 1 < len(data[y]):
                data[y] = insert_ch_in_str_at(data[y], "|", x+1)
counter = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "^" and data[y-1][x] == "|":
            counter += 1

# %%
counter
# 3094 too low
# %%
data
# %%
