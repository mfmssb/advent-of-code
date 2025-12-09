# %%
from pathlib import Path

def parse_data(data_path: str) -> list[tuple[int, int]]:
    lines = Path(data_path).read_text().strip().splitlines()
    return [
        (int(xs), int(ys))
        for line in lines
        for xs, ys in [line.split(",")]
    ]

def get_rectangle_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (abs(x2 - x1) + 1) * (abs(y2 -y1) + 1)
# %%
def p1(data_path: str) -> int:
    data: list[tuple[int, int]] = parse_data(data_path)

    max_area = 0
    for tile1 in data:
        for tile2 in data:
            area = get_rectangle_area(tile1, tile2)
            if area > max_area:
                max_area = area
    return max_area
# %%
p1("/home/onyxia/work/advent-of-code/aoc_2025/09/data/data1.txt")
# %%
