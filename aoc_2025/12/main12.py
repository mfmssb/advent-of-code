# %%
from pathlib import Path

def parse_data(data_path: str):
    input_: list[str] = Path(data_path).read_text()
    
    gifts, regions = input_.split("\n\n")[:-1], input_.split("\n\n")[-1]
    
    gifts = [(gift.split(":")[0], gift.split(":")[-1][1:].split("\n")) for gift in gifts]
    regions = regions.split("\n")
    regions = [region.split(": ") for region in regions]
    regions = [(region[0].split("x"), region[1].split(" ")) for region in regions]
    
    return gifts, regions

gifts, regions = parse_data("/home/onyxia/work/advent-of-code/aoc_2025/12/data/data0.txt")

class Gift:
    def __init__(self, index, layout):
        self.layout = layout
        self.index = str(index)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        gift_representation_map = dict(zip(range(len(alphabet)), alphabet))
        self.letter = gift_representation_map[int(self.index)]
    
    def __repr__(self):
        return ("\n").join([line.replace("#", self.letter) for line in self.layout])

    def rotate_clockwise(self):
        rotated_tuple = list(zip(*self.layout[::-1]))
        rotated = []
        for line in rotated_tuple:
            line_s = ""
            for s in line:
                line_s += s
            rotated.append(line_s)
        self.layout = rotated

    def get_piece(self):
        return [line.replace("#", self.letter) for line in self.layout]
    

gifts = [Gift(gift[0], gift[1]) for gift in gifts]

# %%
regions
# %%
def print_grid(grid):
    print(("\n").join(grid))


for region in regions:
    grid, gift_spec = region
    width, height = grid

    region = ["."*int(width)] * int(height)
    print_grid(region)
    print()

# %%
def is_gift_in_bound(gift_layout, region, pos_x, pos_y):
    gift_width = len(gift_layout[0])
    gift_height = len(gift_layout)
    region_width = len(region[0])
    region_height = len(region)

    print(gift_width, gift_height, region_width, region_height)
    if pos_x < 0 | pos_y < 0:
        return False
    
    if pos_x + gift_width > region_width - 1 | pos_y + gift_height > region_height - 1:
        return False
    
    return True



# def insert_gift_in_region(gift_layout, region, pos_x, pos_y)):
#     for i in range()

# %%
gifts[0].get_piece()
is_gift_in_bound(gifts[0].get_piece(), region, 4, 4)
# %%
