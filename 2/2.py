from collections import namedtuple
import math

Move = namedtuple('Move', ['number', 'colour'])

known_colours = {
    "red": 12,
    "blue": 14,
    "green": 13
}

def solve_game(game: list):
    for moves in game:
        moves_total = {}
        for move in moves:
            moves_total[move.colour] = int(move.number)
        for colour in moves_total:
            if known_colours[colour] < moves_total[colour]:
                return False
    return True

def solve_min(game: list):
    max_colour = {}
    for moves in game:
        for move in moves:
            max_colour[move.colour] = max(int(move.number), int(max_colour.get(move.colour, 0)))
    result = 1
    for maxes in max_colour.values():
        result = result * int(maxes)
    return result


def run_all(filename: str):
    games = {}
    with open(filename) as inp:
        for x in inp.readlines():
            game_raw, moves = x.split(':')
            game_num = int(game_raw.split()[1])
            mvs = [mv for mv in moves.split(';')]
            games[game_num] = []
            for mv in mvs:
                games[game_num].append([Move(*m.split()) for m in mv.split(',')])
                
    total_result, min_result = 0, 0
    print(f"Total queries found {len(games)}")
    for game_num in games:
        add_min = solve_min(games[game_num])
        add_res = game_num if solve_game(games[game_num]) else 0
        min_result += add_min
        total_result += add_res
        print(f"Query Total: {total_result}({add_res}), min_total: {min_result}({add_min})")

    print(f"RESULT: {total_result}, MIN RESULT {min_result}")

if __name__ == "__main__":
    run_all("2_input.txt")