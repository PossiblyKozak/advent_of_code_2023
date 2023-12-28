
def check_mirror(board_l, board_r):
    ind = min(len(board_r), len(board_l))

    bl = "".join(board_l[:ind])
    br = "".join(board_r[:ind])

    return sum(1 for a, b in zip(bl, br) if a != b) == 1 # Allowed errors


def solve_board(board):
    res = 0
    for row_index in range(len(board)-1):
        if check_mirror(board[:row_index + 1][::-1], board[row_index + 1:]):
            res += (row_index + 1) * 100

    board_rotate = [''.join(_) for _ in zip(*board)]
    for col_index in range(len(board_rotate)-1):
        if check_mirror(board_rotate[:col_index + 1][::-1], board_rotate[col_index + 1:]):
            res += col_index + 1
    return res



def run_all(filename: str, repeats = 1):
    boards = []
    with open(filename) as inp:
        board = []
        for x in inp.readlines():
            if x == "\n":
                boards.append(board.copy())
                board = []
            else:
                board.append(x.removesuffix("\n"))

    total_result = 0
    print(f"Total boards found {len(boards)}")
    for i in boards:
        add_res = solve_board(i)
        total_result += add_res
        print(f"Board Score: {add_res}, NEW_TOTAL: {total_result}")
        print("Board: ", '\n'.join(i))

    print("RESULT: ", total_result)

if __name__ == "__main__":
    run_all("13_input.txt")