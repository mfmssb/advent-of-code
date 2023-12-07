filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for x in data:
    print(len(x))

import re

# # Oppgave 1

D = data[1].split("\n")


# ## Mellomregning

def analyze_hand(hand):
    """
    Returns dictionary with number of equal symbols in hand.
    Ex:
    "KK3K1" returns {1: 2, 3: 1}
    """
    symbol_count = {}
    for c in set(hand):
        num_c = len(re.findall(c, hand))
        if num_c in symbol_count.keys():
            symbol_count[num_c] += 1
        else:
            symbol_count[num_c] = 1
    return symbol_count


def find_hand_type(hand):
    hand_type = analyze_hand(hand)
    hand_types = {
        "Five of a kind": {5: 1},
        "Four of a kind": {1: 1, 4: 1},
        "Full house": {3: 1, 2: 1},
        "Three of a kind": {3: 1, 1: 2},
        "Two pair": {2: 2, 1: 1},
        "One pair": {1: 3, 2: 1},
        "High card": {1: 5},
    }
    for k, v in hand_types.items():
        if v == hand_type:
            return k
    
    raise ValueError("No card type found", hand)



type_value_ordering = {
    "Five of a kind": 0,
    "Four of a kind": 1,
    "Full house": 2,
    "Three of a kind": 3,
    "Two pair": 4,
    "One pair": 5,
    "High card": 6,
}


def hand_strength(hand: list):
    """
    Return list of value of each card in hand.
    """
    card_strengths = {  # inversed for sorting
        "A": 2,
        "K": 3, 
        "Q": 4, 
        "J": 5, 
        "T": 6, 
        "9": 7, 
        "8": 8, 
        "7": 9, 
        "6": 10, 
        "5": 11, 
        "4": 12, 
        "3": 13, 
        "2": 14, 
    }
    strength = []
    
    for card in hand:
        strength.append(card_strengths[card])
    return strength


ranks = []
for handbid in D:
    hand, bid = handbid.split(" ")
    to_rank_sort = [
        type_value_ordering[find_hand_type(hand)],
        hand_strength(hand),
        hand,
        int(bid),
    ]
    ranks.append(to_rank_sort)

# +
# Utilizing the listsorting in Python: List are sorted by comparing each element from left to right

ranks.sort()
# -

total_winnings = 0
for i in range(len(ranks)):
    ranknum = len(ranks) - i
    
    total_winnings += ranknum * ranks[i][3]

# ## Løsning

total_winnings

# # Oppgave 2

D = data[1].split("\n")


# ## Mellomregning

def hand_strength2(hand: list):
    """
    Return list of value of each card in hand. Rule set #2
    """
    card_strengths = {  # inversed for sorting
        "A": 2,
        "K": 3, 
        "Q": 4, 
        "J": 15, 
        "T": 6, 
        "9": 7, 
        "8": 8, 
        "7": 9, 
        "6": 10, 
        "5": 11, 
        "4": 12, 
        "3": 13, 
        "2": 14, 
    }
    strength = []
    
    for card in hand:
        strength.append(card_strengths[card])
    return strength


def find_best_hand_type(hand):
    if "J" not in hand:
        return hand
    
    possible_subs = list(set(hand) - set("J"))
    possible_subs.append("A")
    
    new_hands = []
    
    for sub in possible_subs:
        hand_copy = hand.replace("J", sub)
        
        new_hands.append(hand_copy)
    
    ranking = []

    for hand in new_hands:
        ranking.append([type_value_ordering[find_hand_type(hand)], hand_strength(hand), hand])
    ranking.sort()
    return ranking[0][2]


# +
# find_best_hand_type("5JJJK")
# -

ranks = []
for handbid in D:
    hand, bid = handbid.split(" ")

    J_sub_best = find_best_hand_type(hand)

    to_rank_sort = [
        type_value_ordering[find_hand_type(J_sub_best)],
        hand_strength2(hand),
        J_sub_best,
        hand,
        int(bid),
    ]
    ranks.append(to_rank_sort)

ranks.sort()

total_winnings = 0
for i in range(len(ranks)):
    ranknum = len(ranks) - i
    
    total_winnings += ranknum * ranks[i][4]

# ## Løsning

total_winnings
