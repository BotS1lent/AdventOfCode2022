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
    listKnown = []
    for i in range(len(content)):
        if (len(listKnown) == 14):
            return (i - 1)
            break
        if content[i] in listKnown:
            index = -1
            listKnown = []
            continue
        listKnown.append(content[i])
    return (0)


def main(av):
    content = openFile(av)
    index = parseStrat(content)
    print(index)

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))