import math

def follow_nodes(start, nodes, order):
    curr_location = start
    index = 0
    print(start)
    while True:
        lr = order[index % len(order)]
        #print(index, curr_location, lr, nodes[curr_location])
        curr_location = nodes[curr_location][lr]
        index += 1
        if curr_location[-1] == "Z":
            break
            
    print(f"Found {start} -> {curr_location}")
    return index

def check_all_end(locations, end_letter):
    res = True
    for l in locations:
        if l[-1] != end_letter:
            res = False
            break
    return res

def follow_nodes_set(start, end, nodes, order):
    curr_location = start
    index = 0
    # print(start)
    is_incomplete = True
    while is_incomplete:
        is_incomplete = False
        lr = order[index % len(order)]
        for i in range(len(curr_location)):
            cli = curr_location[i]
            if index % 1000000 == 0:
                print(index, cli, lr, nodes[cli])
            curr_location[i] = nodes[cli][lr]
            if curr_location[i][-1] != end:
                is_incomplete = True
        index += 1
    return index

def run(filename):
    order = []
    nodes = {}
    starters = []
    enders = []
    with open(filename, "r") as inp:
        order = [1 if x == "R" else 0 for x in list(inp.readline().rstrip())]
        inp.readline()
        for line in inp.readlines():
            key, val = line.split('=')
            key = key.rstrip()
            val = val.replace(" ", "").replace("(", "").replace(")", "").replace("\n", "")
            nodes[key] = val.split(",")
            if key[-1] == "A":
                starters.append(key)
            if key[-1] == "Z":
                enders.append(key)

    all_sets = {}

    res = 0

    for s in starters:
        all_sets[s] = follow_nodes(s, nodes, order)
    print(all_sets)
    res = math.lcm(*list(all_sets.values()))
    # res = follow_nodes_set(starters, "Z", nodes, order)
    print(f"RESULT: {res}")

if __name__ == "__main__":
    # run("8tz.txt")
    # run("8t.txt")
    # run("8t2.txt")
    run("8.txt")