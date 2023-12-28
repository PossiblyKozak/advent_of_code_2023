from collections import Counter
from functools import cmp_to_key

#card_rank = "23456789TJQKA"
card_rank = "AKQJT98765432"

def tv(value):
    return card_rank.index(value)

def comp_v(a,b):
    return tv(a) > tv(b)

def comp(a,b):
    return 1 if comp_v(a[0], b[0]) else -1

def go_high_card(a: Counter, b : Counter):
    ae = sorted(list(map(tv, a.elements())))
    be = sorted(list(map(tv, b.elements())))
    # print(ae, be)
    for i in range(len(ae)):
        if ae[i] != be[i]:
            # print(1 if ae[i] > be[i] else -1, ae[i], be[i])
            # input()
            return 1 if ae[i] > be[i] else -1

def compare_hands(a, b):
    ac, bc = a[0].most_common(), b[0].most_common()

    if ac[0][1] != bc[0][1]:
        return 1 if ac[0][1] < bc[0][1] else -1
    else:
        if ac[0][1] == 1:
            return go_high_card(a[0], b[0])

        if ac[1][1] != bc[1][1]:
            return 1 if ac[1][1] < bc[1][1] else -1
        else:
            if ac[1][1] > 1:
                if ac[0][0] != bc[0][0]:
                    return comp(ac[0], bc[0])
                elif ac[1][0] != bc[1][0]:
                    return comp(ac[1], bc[1])
                else:
                    return comp(ac[-1], bc[-1])
            else:
                if ac[0] == bc[0]:
                    # if len(ac) == 4:
                    #     print(ac, ac[1:], end=" -> ")
                    #     print(bc, bc[1:])
                    return go_high_card(Counter(dict(ac[1:])), Counter(dict(bc[1:])))
                return comp(ac[0], bc[0])
    return 0
                

def solve_hands(all_hands : list):
    res = 0
    index = 1    

    for p in sorted(all_hands, key=cmp_to_key(compare_hands), reverse=True):
        pr = sorted(p[0], key=lambda x: (-p[0][x], tv(x)))
        res += p[1] * index
        print("".join(p[0].elements()), p[1], "*", index, f"--(+{p[1] * index})-->", res)
        index += 1
        
    return res

def run_all(filename: str):
    all_hands = []
    with open(filename) as inp:
        for hand in inp.readlines():
            cards, bet = hand.split()
            all_hands.append((Counter(cards), int(bet)))

    recs = solve_hands(all_hands)

    print(f"RESULT: {recs}")


if __name__ == "__main__":
    #run_all("7_input_test.txt") 
    run_all("7_input.txt")
    #run_all("7_input_2.txt")