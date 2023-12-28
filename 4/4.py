import math
from collections import defaultdict

def solve_cards(cards: list):
    points = 0
    ci = {}    
    for card_index in range(len(cards)):
        winner_count = 0
        new_points = 0
        winners = cards[card_index][0]
        your_nums = cards[card_index][1]
        for num in your_nums:
            if num in winners:
                winner_count += 1

        ci[card_index] = winner_count
        if winner_count > 0:
            new_points = 2 ** (winner_count - 1)
        points += new_points

    totals = {0:ci[0]}
    for i in range(len(cards)):
        totals[i] = 1
    for i in range(len(cards)):
        for j in range(i+1, i + ci[i] + 1):
            totals[j] += totals[i]
        
    card_count = []
    for i in range(len(cards)):
        card_count.append(totals[i])

    return points, sum(card_count)

def run_all(filename: str):
    cards = []
    with open(filename) as inp:
        for x in inp.readlines():
            cn, numbers = x.removesuffix("\n").split(":")
            wn, yn = numbers.split("|")
            cards.append((wn.split(), yn.split()))

    print("RESULT: ", solve_cards(cards))

if __name__ == "__main__":
    # run_all("4_input_test.txt") 
    run_all("4_input.txt")