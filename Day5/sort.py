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

def findPrio(toSort : list, instruction : list):
    tmp = deque([])
    for line in instruction:
        for i in range(line[0]):
            tmp.appendleft(toSort[line[1]].popleft())
        for i in range(line[0]):
            toSort[line[2]].appendleft(tmp.popleft())
        tmp = deque([])
    return (toSort)

def parseStrat(content : str):
    tmp = content.splitlines()
    check = 9
    instruction = []
    toSort = []
    for i in tmp:
        if check:
            tmpSort = i.split()
            toSort.append(deque(tmpSort[2:]))
            check -= 1
            continue
        if i:
            tmpInstruction = i.split()
            instruction.append((int(tmpInstruction[1]), int(tmpInstruction[3]) - 1, int(tmpInstruction[5]) - 1))
    return (toSort, instruction)

def main(av):
    content = openFile(av)
    toSort, instruction = parseStrat(content)
    result = findPrio(toSort, instruction)
    for i in result:
        print(i[0], end='')
    print()

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))