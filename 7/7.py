from collections import Counter
from functools import cmp_to_key

#card_rank = "23456789TJQKA"
card_rank = "AKQT98765432J"

def tv(value):
    return card_rank.index(value)

def comp_v(a,b):
    return tv(a) > tv(b)

def comp(a,b):
    return 1 if comp_v(a[0], b[0]) else -1

def go_high_card(a: str, b : str):
    ae = list(map(tv, a))
    be = list(map(tv, b))
    # print(ae, be)
    for i in range(len(ae)):
        if ae[i] != be[i]:
            # print(1 if ae[i] > be[i] else -1, ae[i], be[i])
            # input()
            return 1 if ae[i] < be[i] else -1

def get_rank(cards: list):
    if cards[0][1] == 5:
        return 6
    elif cards[0][1] == 4:
        return 5
    elif cards[0][1] == 3:
        if cards[1][1] == 2:
            return 4
        else:
            return 3
    elif cards[0][1] == 2:
        if cards[1][1] == 2:
            return 2
        else:
            return 1
    else:
        return 0

def compare_hands(a, b):
    a_rank, b_rank = get_rank(a[1].most_common()), get_rank(b[1].most_common())

    if a_rank != b_rank:
        return 1 if a_rank > b_rank else -1
    else:
        return go_high_card(a[0], b[0])
                

def solve_hands(all_hands : list):
    res = 0
    index = 1

    for p in sorted(all_hands, key=cmp_to_key(compare_hands)):
        res += p[2] * index
        print(p[0], f"--(+{p[2] * index})-->", res)
        index += 1
        
    return res

def run_all(filename: str):
    all_hands = []
    with open(filename) as inp:
        for hand in inp.readlines():
            cards, bet = hand.split()
            cc = Counter(cards)
            if "J" in cc:
                pp = cc.most_common(2)
                for i in pp:
                    if i[0] != "J":
                        cc[i[0]] += cc.pop("J")
                        break
            all_hands.append((cards, cc, int(bet)))

    recs = solve_hands(all_hands)

    print(f"RESULT: {recs}")


if __name__ == "__main__":
    #run_all("7_input_test.txt") 
    run_all("7_input.txt")
    #run_all("7_input_2.txt")