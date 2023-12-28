import math
from collections import defaultdict

def solve_seeds(seeds, maps):
    all_seeds = []
    for seed in seeds:
        cs = seed
        for map in maps:
            for m in map:
                if cs >= m[0] and cs < m[1]:
                    cs = cs + m[2]
                    break
        all_seeds.append(cs)
    return min(all_seeds)

def is_in_seeds(seeds, target):
    is_found = False
    for seed_ranges in seeds:
        if seed_ranges[0] <= target and seed_ranges[1] >= target:
            is_found = True
            break
    return is_found

def find_first_seed(seeds, maps):
    curr_seed = 0
    rev_map = maps[::-1]
    # print(rev_map)
    while True:
        cs = curr_seed
        for map in rev_map:
            # print(cs, map)
            for m in map:
                if cs >= m[0] and cs < m[1]:
                    # print(f"Moving {cs} -{m}-> {cs + m[2]}")
                    cs = cs + m[2]
                    break
        # print(f"checking dest {curr_seed} -> {cs} -> {seeds}")
        if is_in_seeds(seeds, cs):
            # print(curr_seed, cs)
            return curr_seed
        else:
            curr_seed += 1

def expand_seeds(seeds):
    index = 0
    ns = []
    while index < len(seeds):
        ns.append((seeds[index], seeds[index] + seeds[index + 1]))
        index += 2
    return ns

def run_all(filename: str):
    seeds = []
    maps = []
    with open(filename) as inp:
        seeds = list(map(int, (inp.readline().split(":")[1]).split()))
        seeds = expand_seeds(seeds)
        mp = []
        for rl in inp.readlines():
            if len(rl) < 2 or ":" in rl:
                if len(mp) > 0:
                    maps.append(mp)
                    mp = []
            else:
                dest, source, dist = list(map(int, rl.split()))
                mp.append((dest, dest + dist, source - dest))

    print("RESULT: ", find_first_seed(seeds, maps))

if __name__ == "__main__":
    # run_all("5_input_test.txt") 
    run_all("5_input.txt")