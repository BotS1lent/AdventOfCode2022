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

def parseStrat(content : str):
    tmp = content.splitlines()
    result = []
    for line in tmp:
        resultLine = []
        for elem in line:
            resultLine.append(int(elem))
        result.append(resultLine)
    return (result)

def getTotal(table: list):
    total = 0
    nbLine = len(table)
    lenLine = len(table[0])
    total = 0
    up, left, right, down = 0, 0, 0, 0
    checker = 0
    for i in range(nbLine):
        for j in range(lenLine):
            up, left, right, down = 0, 0, 0, 0
            if (i == 0 or i == nbLine -1 or j == 0 or j == lenLine - 1):
                continue
            for x in range(i - 1, -1, -1):
                up += 1
                if (table[x][j] >= table[i][j]):
                    checker += 1
                    break
            for x in range(i + 1, nbLine):
                down += 1
                if (table[x][j] >= table[i][j]):
                    checker += 1
                    break
            for x in range(j - 1, -1, -1):
                left += 1
                if (table[i][x] >= table[i][j]):
                    checker += 1
                    break
            for x in range(j + 1, lenLine):
                right += 1
                if (table[i][x] >= table[i][j]):
                    checker += 1
                    break
            checker = up * left * down * right
            total = checker if checker > total else total
    return (total)

def main(av):
    content = openFile(av)
    table = parseStrat(content)
    total = getTotal(table)
    print(total)

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))
