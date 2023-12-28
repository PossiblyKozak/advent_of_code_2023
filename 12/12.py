from collections import namedtuple

Query = namedtuple('Query', ['board', 'label'])

active_count = 0
raw_ql, question_lines = [], []

# ??????#??? 7,1
# ?#####???????#.. 5,1,1,1

def is_solved(curr_board, label):
    result = label == [len(_) for _ in curr_board.split(".") if _ != ""]
    return result

def is_solvable(curr_board: str, label: list):
    pockets = [len(_) for _ in curr_board.split(".") if _ != ""]
    sets = [len(_) for _ in curr_board[:curr_board.index("?")].split(".") if _ != ""]
    all_labels = len(label)
    p_ci = 0
    while len(pockets) > 0 and p_ci < all_labels:
        if pockets[0] >= label[p_ci]:
            pockets[0] = pockets[0] - (label[p_ci] + 1)
            p_ci += 1
            if pockets[0] <= 0:
                pockets.pop(0)
        else:
            pockets.pop(0)

    s_ci = 0
    cl = label.copy()
    #print("EXISTING SETS: ", sets)
    while len(cl) > 0 and s_ci < len(sets):
        #print(cl, sets[s_ci])
        if cl[0] == sets[s_ci] or (cl[0] > sets[s_ci] and len(sets) - 1 == s_ci):
            cl[0] = cl[0] - (sets[s_ci] + 1)
            s_ci += 1
            cl.pop(0)
        else:
            break

    #print(curr_board, all_labels == p_ci and s_ci == len(sets), label)
    #print(f"all_Labels: {all_labels}, p_ci: {p_ci}, s_ci: {s_ci}, len(sets): {len(sets)}")

    return all_labels == p_ci and s_ci == len(sets)



def solve_board(curr_board: str, label: list):
    result = 0
    if "?" in curr_board:
        if is_solvable(curr_board, label):
            result += solve_board(curr_board.replace("?", ".", 1), label)
            result += solve_board(curr_board.replace("?", "#", 1), label)
            return result
        else:
            return 0
    elif is_solved(curr_board, label):
        print(curr_board)
        result += 1 
    return result


def run_all(filename: str, repeats = 1):
    with open(filename) as inp:
        for x in inp.readlines():
            board, labels = x.removesuffix("\n").split(" ")
            raw_ql.append(Query(board, list(map(int, labels.split(',')))))



    for i in range(len(raw_ql)):
        nql = raw_ql[i]
        joiner = [nql.board for _ in range(repeats)]
        question_lines.append(Query("?".join(joiner), nql.label * repeats))

    total_result = 0
    for i in question_lines:
        add_res = solve_board(i.board, i.label)
        total_result += add_res
        print(f"Board Score: {add_res}, Board: {i.board}, Label: {i.label}\nNEW_TOTAL: {total_result}")

    print("RESULT: ", total_result)

if __name__ == "__main__":
    run_all("12_input_test.txt", 3)
    #run_all("12_input.txt", 5)
    #is_solvable("..#######.#.#######..#.#######..##.????#??????????#???", [7, 1, 7, 1, 7, 1, 7, 1, 7, 1])
    #is_solvable("#######.#.##...###??????????#??????????#??????????#???", [7, 1, 7, 1, 7, 1, 7, 1, 7, 1])
    #is_solvable("#######.#.##.#.#######??????#??????????#??????????#???", [7, 1, 7, 1, 7, 1, 7, 1, 7, 1])
    #is_solvable("#######.#..#######.#..#######.#..#######.#...#????#???", [7, 1, 7, 1, 7, 1, 7, 1, 7, 1])