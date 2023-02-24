#!/usr/bin/env python3
import sys
from collections import deque

######################## HELPER & MAIN ########################

def openFile(av):
    try:
        file = open(av[0], 'r')
    except IOError:
        exit(84)
    tmp_str = file.read()
    if (len(tmp_str) == 0):
        exit(84)
    return (tmp_str)

def signal(instruction: list):
    cycle = 1
    add = deque()
    result = []
    total = 1
    for line in instruction:
        if line[0] == 1:
            add.append((2, line[1]))
        while add:
            for i in range(len(add)):
                add[i] = (add[i][0] - 1, add[i][1])
            if cycle == 21 or cycle == 59 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                print(total)
                result.append(cycle * total)
            if add[0][0] == 0:
                _, elem = add.popleft()
                total += elem
            cycle += 1
    return (result)


def parseStrat(content : str):
    tmp = content.splitlines()
    result = []
    for line in tmp:
        if line.startswith("noop"):
            result.append((0, 0))
        else:
            result.append((1, int(line.split()[1])))
    return (result)

def main(av):
    content = openFile(av)
    table = parseStrat(content)
    total = signal(table)
    print(total)
    print(sum(total))

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))
