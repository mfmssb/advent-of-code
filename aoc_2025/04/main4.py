def parse_data(data_path: str) -> list:
    with open(data_path, 'r') as file:
        content = file.read()
    return content.split("\n")


def get_neighbors(x, y, width, height):
    """
    Return the neighbouring coordinates of cell (x, y).
    Ignoring neigbors out of bounds in the grid.
    
    get_neighbors(0, 1, 10, 10)
        [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
    """
    neighbors = []

    for i in range(-1, 2):  # x direction
        for j in range(-1, 2):  # y direction
            if i != 0 or j != 0:
                nx = x + i
                ny = y + j
                if 0 <= nx < width and 0 <= ny < height:
                    neighbors.append((nx, ny))
    return neighbors


def p1(paper_locations):
    """
    Loop through all possible positions (x, y) in the factory once.
    If the position is the character "@" (indicating paper),
    call get_neighbors(x, y, ..) and count the number of times they 
    are "@".
    """
    width = len(paper_locations[0])
    height = len(paper_locations)
    forklift_access_points = []
    for x in range(0, width):
        for y in range(0, height):
            if paper_locations[y][x] == "@":
                ns = get_neighbors(x, y, width, height)
                num_paper_rolls = 0
            
                for n in ns:
                    nx = n[0]
                    ny = n[1]
                    if paper_locations[ny][nx] == "@":
                        num_paper_rolls += 1
                if num_paper_rolls < 4:
                    forklift_access_points.append((x, y))
    return len(forklift_access_points), forklift_access_points


def remove_paper(paper_locations, access_points_to_remove):
    """
    Loop through the possible access points for the forklift
    and change all these to "." <empty>. 
    Return the updated paper_locations.
    """
    for (x, y) in access_points_to_remove:
        new_row = paper_locations[y]
        new_row = new_row[:x] + "." + new_row[x+1:]
        paper_locations[y] = new_row
    
    return paper_locations


def p2(paper_locations):
    """
    Reuse part 1 to successively change the paper_locations.
    """
    total_rolls_removed = 0
    paper_locations_changed = paper_locations.copy()
    rolls_removed = -1
    while rolls_removed:  # stops when rolls_removed == 0
        rolls_removed, access_points = p1(paper_locations_changed)  # reuse part 1
        paper_locations_changed = remove_paper(paper_locations_changed, access_points).copy()
        total_rolls_removed += rolls_removed
    return total_rolls_removed


paper_locations = parse_data("data/data1.txt")

# %timeit p1(paper_locations)

# %timeit p2(paper_locations)
