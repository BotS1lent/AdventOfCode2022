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
    print(tmp)
    result = []
    for line in tmp:
        resultLine = []
        for elem in line:
            resultLine.append(int(elem))
        result.append(resultLine)
    return (result)

def main(av):
    print("yes")
    content = openFile(av)
    table = parseStrat(content)

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))
