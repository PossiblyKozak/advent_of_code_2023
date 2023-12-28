import math

def solve_races(times, distances):
    print(times, distances)
    recs = []
    for index in range(len(times)):
        record_count = 0
        for i in range(times[index]//2):
            if i * (times[index] - i) > distances[index]:
                record_count += times[index] - (i * 2) + 1
                break
        recs.append(record_count)
    return recs

def run_all(filename: str):
    times = []
    distances = []
    with open(filename) as inp:
        times = list(map(int, (inp.readline().split(":")[1]).split()))
        distances = list(map(int, (inp.readline().split(":")[1]).split()))
    recs = solve_races(times, distances)

    print(recs)
    print("RESULT: ", math.prod(recs))


if __name__ == "__main__":
    #run_all("6_input_test.txt") 
    #run_all("6_input.txt")
    run_all("6_input_2.txt")