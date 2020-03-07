from statistics import mode
from time import time

start = time()

# Stuff i dont understand incoming 
list_of_hands = open('poker_hands.txt', 'r')

list_of_hands_lines = []

if list_of_hands.mode == 'r':
    list_of_hands_lines = list_of_hands.readlines()



def consecutive_check(values):
    if sorted(values) == list(range(min(values), max(values) + 1)):
        return True
    
def royal_flush_checker(values,suits):
    if values == [10,11,12,13,14] and suits == ["H"] * 5 or suits == ["C"] * 5 or suits == ["S"] * 5 or suits == ["D"] * 5:
        return True

def straight_flush_checker(values,suits):
    if consecutive_check(values) == True and suits == ["H"] * 5 or consecutive_check(values) == True and suits == ["C"] * 5 or consecutive_check(values) == True and suits == ["S"] * 5 or consecutive_check(values) == True and suits == ["D"] * 5:
        return True
    
def four_of_a_kind_checker(values):
    if values.count(mode(values)) == 4:
        return True

def full_house_checker(values):
    if values.count(mode(values)) == 3 and values.count(max(values)) == 2 or values.count(mode(values)) == 3 and values.count(min(values)) == 2:
        return True

def flush_checker(suits):
    if suits == ["H"] * 5 or suits == ["C"] * 5 or suits == ["S"] * 5 or suits == ["D"] * 5:
        return True

def straight_checker(values):
    if consecutive_check(values) == True:
        return True

def three_of_a_kind_checker(values):
    if values.count(mode(values)) == 3:
        return True

def two_pairs_checker(values):
    if len(set(values)) == 3 and values.count(mode(values)) == 2:
        return True 

def one_pair_checker(values):
    if values.count(mode(values)) == 2:
        return True


def score(hand):
    
    values =  [x for x in hand if not isinstance(x, str)]
    suits = [x for x in hand if not isinstance(x, int)]
    
    score = 0

    if royal_flush_checker(values, suits) == True:
        score = 1000

    elif straight_flush_checker(values,suits) == True:
        score = 900 + max(values)

    elif four_of_a_kind_checker(values) == True:
        score = 800 + mode(values)

    elif full_house_checker(values) == True:
        score = 700 + mode(values)

    elif flush_checker(suits) == True:
        score = 600 + max(values)

    elif straight_checker(values) == True:
        score = 500 + max(values)
    
    elif three_of_a_kind_checker(values) == True:
        score = 400 + mode(values)

    elif two_pairs_checker(values) == True:
        score = 300 + mode(reversed(sorted(values)))

    elif one_pair_checker(values) == True:
        score = 200 + mode(values)

    else:
        score = 100 + max(values)

    return score

            

def line_cleaner(INPUT):
    
    NEW_INPUT = list(INPUT)
    
    while (" " in NEW_INPUT):
        NEW_INPUT.remove(" ")

    while ("\n" in NEW_INPUT):
        NEW_INPUT.remove("\n")

    for i in range(len(NEW_INPUT)):
        if NEW_INPUT[i] == "T":
            NEW_INPUT[i] = "10"

    for i in range(len(NEW_INPUT)):
        if NEW_INPUT[i] == "J":
            NEW_INPUT[i] = "11"

    for i in range(len(NEW_INPUT)):
        if NEW_INPUT[i] == "Q":
            NEW_INPUT[i] = "12"

    for i in range(len(NEW_INPUT)):
        if NEW_INPUT[i] == "K":
            NEW_INPUT[i] = "13"

    for i in range(len(NEW_INPUT)):
        if NEW_INPUT[i] == "A":
            NEW_INPUT[i] = "14"

    for i in range(len(NEW_INPUT)):
        if NEW_INPUT[i] == "2" or  NEW_INPUT[i] == "3" or  NEW_INPUT[i] == "4" or  NEW_INPUT[i] == "5" or  NEW_INPUT[i] == "6" or  NEW_INPUT[i] == "7" or  NEW_INPUT[i] == "8" or  NEW_INPUT[i] == "9" or  NEW_INPUT[i] == "10" or  NEW_INPUT[i] == "11" or  NEW_INPUT[i] == "12" or  NEW_INPUT[i] == "13" or  NEW_INPUT[i] == "14":
            NEW_INPUT[i] = int(NEW_INPUT[i])

    return NEW_INPUT

def score_comparison():

    player_1_wins = 0
    player_2_wins = 0
    undecided = 0

    for line in list_of_hands_lines:
        line = line_cleaner(line)
        hand_1 = line[:10]
        hand_2 = line[10:]

        if score(hand_1) > score(hand_2):
            player_1_wins += 1

        elif score(hand_2) > score(hand_1):
            player_2_wins += 1

        else:
            print("Tie breaker required: PLAYER 1 {} vs. PLAYER 2 {}" .format(hand_1, hand_2))
            undecided += 1


    return "Player 1 wins {} games" .format(player_1_wins), "Player 2 wins {} games" .format(player_2_wins), "{} games were undecided" .format(undecided)


print(score_comparison())

end = time()

print("That took {} seconds" .format(end - start))

