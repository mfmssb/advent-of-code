filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

# ## Mellomregning

d = data[1].split("\n")


# +
def get_game_id(gameline: str) -> int:
    """
    Ex:
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    Returns 1
    """
    gamestr = gameline.split(":")[0]
    
    return int(gamestr.split(" ")[1])

def get_game_sets(gameline: str) -> list:
    """
    Ex:
    'Game 100: 5 green, 7 red, 4 blue; 11 green, 9 red, 8 blue; 2 blue, 12 green'
    Returns [[[5, 'green'], [7, 'red'], [4, 'blue']], [[11, 'green'], [9, 'red'], [8, 'blue']], [[2, 'blue'], [12, 'green']]]
    """
    g = gameline.split(":")[1]
    g = g.split("; ")
    g2 = []
    for _set in g:
        g2.append(_set.split(","))
    
    for i in range(len(g2)):
        for j in range(len(g2[i])):
            g2[i][j] = g2[i][j].strip()
            g2[i][j] = g2[i][j].split(" ")
            g2[i][j][0] = int(g2[i][j][0])
    
    return g2

def find_max_balls_in_game(game: list) -> dict:
    """
    Ex:
    [[[5, 'green'], [7, 'red'], [4, 'blue']], [[11, 'green'], [9, 'red'], [8, 'blue']], [[2, 'blue'], [12, 'green']]]
    Returns {'blue': 8, 'green': 12, 'red': 9}
    """
    
    max_balls_in_game = {
        'blue': 0,
        'green': 0,
        'red': 0
    }
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j][0] > max_balls_in_game[game[i][j][1]]:
                max_balls_in_game[game[i][j][1]] = game[i][j][0]
    return max_balls_in_game

def check_balls_in_game_is_possible(max_balls: dict) -> bool:
    """
    Returns True if the number of blue, green and red balls doesn't exceed the limit
    """
    to_check = {
        'blue': 14,
        'green': 13,
        'red': 12
    }
    for k, v in to_check.items():
        if v < max_balls[k]:
            return False
    return True


# -

sum_ids = 0
for game in d:
    game_id = get_game_id(game)
    game_sets = get_game_sets(game)
    game_max = find_max_balls_in_game(game_sets)
    if check_balls_in_game_is_possible(game_max):
        sum_ids += game_id

print(game)
print(game_id)
print(game_sets)
print(game_max)

# ## Løsning

print(sum_ids)

# # Oppgave 2

# ## Mellomregning

sum_powers = 0
for game in d:
    game_id = get_game_id(game)
    game_sets = get_game_sets(game)
    game_max = find_max_balls_in_game(game_sets)
    
    power = 1
    for k, v in game_max.items():
        power *= v
    
    sum_powers += power

# ## Løsning

sum_powers
