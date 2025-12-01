filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("** Inndata størrelse **")
for i, x in enumerate(data):
    print(f"data[{i}]: {len(x):8} tegn")

# # Problem 1

d = data[1].split("\n")


# ## Intermediate Steps 1

def search_horizontally(word: str, grid: list) -> int:
    word_rev = word[::-1]
    h = len(grid)
    w = len(grid[0])
    l = len(word)

    count = 0
    for y in range(h):
        for x in range(w-l+1):
            if grid[y][x: x+l] in [word, word_rev]:
                count += 1
    return count


def search_vertically(word: str, grid: list) -> int:
    word_rev = word[::-1]
    h = len(grid)
    w = len(grid[0])
    l = len(word)

    count = 0
    for y in range(h-l+1):
        for x in range(w):
            check = ""
            for j in range(l):
                check += grid[y+j][x]
            if check in [word, word_rev]:
                count += 1
    return count


def search_diagonally(word: str, grid: list) -> int:
    word_rev = word[::-1]
    h = len(grid)
    w = len(grid[0])
    l = len(word)

    count = 0
    for y in range(h-l+1):
        for x in range(w):
            # check diagonal from top left to bottom right
            check = ""
            if (w - x >= l):
                for i in range(l):
                    check += grid[y+i][x+i]
                
                if check in [word, word_rev]:
                    count += 1

            
            check = ""
            # check diagonal from top right to bottom left
            if (x + 1 >= l):
                for i in range(l):
                    check += grid[y+i][x-i]
                if check in [word, word_rev]:
                    count += 1
    return count


def search_all(word, grid):
    count = search_horizontally(word, grid)
    count += search_vertically(word, grid)
    count += search_diagonally(word, grid)
    return count


ans1 = search_all("XMAS", d)

# ## Solution 1

print(ans1)


# # Problem 2

# ## Intermediate Steps 2

def search_x(grid: list, word = "MAS") -> int:
    word_rev = word[::-1]
    h = len(grid)
    w = len(grid[0])
    l = len(word)

    count = 0
    for y in range(h-l+1):
        for x in range(w-l+1):
            # check diagonal from top left to bottom right
            check1 = ""
            for i in range(l):
                check1 += grid[y+i][x+i]
            
            check2 = ""
            # check diagonal from top right to bottom left
            for i in range(l):
                check2 += grid[y+i][x+(l-1)-i]
            
            if (check1 in [word, word_rev]) & (check2 in [word, word_rev]):
                count += 1
    return count


d = data[1].split("\n")

ans2 = search_x(d)

# ## Solution 2

print(ans2)
