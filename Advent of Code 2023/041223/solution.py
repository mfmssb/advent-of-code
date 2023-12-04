filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

# # Oppgave 1

cards = data[1].split("\n")


# ## Mellomregning

# +
def parse_winning_numbers(card_str: str) -> list:
    """
    Returns list of winning numbers, given card string
    """
    c = card_str.split(" | ")[0].split(": ")[1].split(" ")
    c = [x for x in c if len(x) > 0]
    return c

def parse_my_numbers(card_str: str) -> list:
    """
    Returns list of my numbers, given card string
    """
    c = card_str.split(" | ")[1].replace("  ", " ").split(" ")
    c = [x for x in c if len(x) > 0]
    return c

def number_of_same_elements(l1: list, l2: list) -> int:
    """
    Returns the size of the intersection of two lists.
    -- Counts the number of wins.
    """
    count = 0
    for x in l1:
        if x in l2:
            count += 1
    return count


# -

sum_points = 0
for card in cards:
    win = parse_winning_numbers(card)
    my = parse_my_numbers(card)
    num_wins = number_of_same_elements(win, my)
    if num_wins == 0:
        points = 0
    else:
        points = 2**(num_wins-1)
    sum_points += points

# ## Løsning

sum_points

# # Oppgave 2

cards = data[1].split("\n")

# ## Mellomregning

# Dictionary keeping count of how many cards you have
processed_cards = {
    k: 1 for k in range(1, len(cards)+1)
}

# Loop all card numbers from card 1 and onwards.
# For each win (n points) add the value of processed cards for the n next cards
for card_number in range(1, len(cards)+1):
    card_index = card_number-1
    
    win = parse_winning_numbers(cards[card_index])
    my = parse_my_numbers(cards[card_index])
    num_wins = number_of_same_elements(win, my)
    
    number_of_cards = processed_cards[card_number]
    
    if num_wins != 0:
        for i in range(1, num_wins+1):
            processed_cards[card_number+i] += number_of_cards

# Add total number of cards
sum_processed_cards = 0
for k, v in processed_cards.items():
    sum_processed_cards += v

# ## Løsning

sum_processed_cards
