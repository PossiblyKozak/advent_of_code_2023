import re
from collections import defaultdict
from math import prod

if '__main__' == __name__:
    lines = list(open("3_input.txt").readlines())
    lineLength = len(lines[0])

    if any(len(line) != lineLength for line in lines):
        print('Error: Input lines are not all the same length.')
        exit(-1)

    data = ''.join(lines)
    vectors = tuple(lineLength * row + col
                    for row in range(-1, 2) for col in range(-1, 2)
                    if row or col)

    total = 0
    total_list = []
    gears = defaultdict(list)
    for match in re.finditer(r'\d+', data):
        for i in {ci for mi in range(*match.span()) for v in vectors
                  if 0 <= (ci := mi + v) < len(data)}:
            if (checkChar := data[i]) not in '\n.0123456789':
                total += (partNumber := int(match.group()))
                total_list.append(partNumber)
                if checkChar == '*':
                    gears[i].append(partNumber)
                break
    print(sorted(total_list))
    print('Part 1 result:', total)
    print('Part 2 result:',
          sum(map(prod, filter(lambda x: len(x) == 2, gears.values()))))