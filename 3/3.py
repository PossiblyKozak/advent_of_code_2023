import math


def solve_board(query: list):
    important_nums = []
    important_gears = 0
    all_nums = {}
    all_symbols = []
    all_gears = []

    for y in range(len(query)):
        q_line: str = query[y]
        for x in range(len(query)):
            if q_line[x] == "+" or q_line[x] == "*":
                all_symbols.append((y, x))
                if q_line[x] == "*":
                    all_gears.append((y, x))
        numbers = [num for num in q_line.replace("+",".").replace("*",".").split(".") if num != ""]
        si = 0
        for n in numbers:
            qil = q_line.index(n, si)
            all_nums[(y, qil)] = n
            si = qil + len(n)
            
    # print(all_nums)
    # print(all_symbols)

    for symbol_location in all_symbols:
        parts = []
        for num_loc in list(all_nums.keys()).copy():
            ny, nx_s = num_loc
            nx_e = nx_s + len(all_nums[num_loc]) - 1

            sy, sx = symbol_location[0], symbol_location[1]
            if abs(sy - ny) <= 1 and (abs(sx - nx_s) <= 1 or abs(sx - nx_e) <= 1):
                # print(f"Searching for '{all_nums[num_loc]}' -> sl0: {sx}, nx_s: {nx_s}, nx_e: {nx_e}, sl1: {sy}, ny: {ny}")
                # print(f"Adding number {all_nums[num_loc]} {num_loc} as it is close to {symbol_location}")
                important_nums.append(int(all_nums[num_loc]))
                parts.append(int(all_nums[num_loc]))
        if len(parts) == 2 and symbol_location in all_gears:
            important_gears += math.prod(parts)
    # print(sorted(important_nums))
    # print(important_gears)
    return sum(important_nums), important_gears

def replace_symbols(line: str):
    return ''.join(item if item in "1234567890.*" else "+" for item in line)


def run_all(filename: str):
    board = []
    with open(filename) as inp:
        for x in inp.readlines():
            board.append(replace_symbols(x.removesuffix("\n")))
    p1, p2 = solve_board(board)
    print("RESULT: ", p1)
    print("GEARS: ", p2)

if __name__ == "__main__":
    # run_all("3_input_test.txt") 
    run_all("3_input.txt")