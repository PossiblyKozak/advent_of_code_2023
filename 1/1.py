_KNOWN_NUMS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def solve_query(query: list):
    index = 0
    nums = []
    while index < len(query):
        if query[index].isdigit():
            nums.append(query[index])
        else:
            for num in _KNOWN_NUMS.keys():
                if query[index:index + len(num)] == num:
                    nums.append(_KNOWN_NUMS[num])
        index += 1
    return int(nums[0] + nums[-1])



def run_all(filename: str):
    queries = []
    with open(filename) as inp:
        for x in inp.readlines():
            queries.append(x.removesuffix("\n"))
                

    total_result = 0
    print(f"Total queries found {len(queries)}")
    for query in queries:
        add_res = solve_query(query)
        total_result += add_res
        print(f"Query Score: {add_res}, NEW_TOTAL: {total_result}")
        print("Query: ", query)

    print("RESULT: ", total_result)

if __name__ == "__main__":
    run_all("1_input.txt")