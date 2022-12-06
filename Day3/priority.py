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
        print(line)
        common_letter = list(set(line[0])&set(line[1])&set(line[2]))
        val = ord(common_letter[0])
        total += ((val - 96) if val > 96 else (val - 38))
    return (total)

def parseStrat(content : str):
    tmp = content.splitlines()
    counter = 0
    tmpTable = []
    tmpStack = []
    for test_str in tmp:
        if counter == 3:
            counter = 0
            tmpTable.append(tmpStack)
            tmpStack = []
        tmpStack.append(test_str)
        counter += 1
    if tmpStack:
        tmpTable.append(tmpStack)
    return (tmpTable)

def main(av):
    content = openFile(av)
    content = parseStrat(content)
    result = findPrio(content)
    print(result)

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))