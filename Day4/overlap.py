#!/usr/bin/env python3
import sys

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

def findPrio(table : list):
    total = 0
    for line in table:
        if (line[1][0] <= line[0][0] <= line[1][1] or line[1][0] <= line[0][1] <= line[1][1]):
            total += 1
            continue
        if (line[0][0] <= line[1][0] <= line[0][1] or line[0][0] <= line[1][1] <= line[0][1]):
            total += 1
    return (total)

def parseStrat(content : str):
    tmp = content.splitlines()
    result = []
    for i in tmp:
        pair = i.split(',')
        pairOne = pair[0].split('-')
        pairOne[0] = int(pairOne[0])
        pairOne[1] = int(pairOne[1])
        pairTwo = pair[1].split('-')
        pairTwo[0] = int(pairTwo[0])
        pairTwo[1] = int(pairTwo[1])
        result.append((pairOne, pairTwo))
    return (result)

def main(av):
    content = openFile(av)
    content = parseStrat(content)
    result = findPrio(content)
    print(result)

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))