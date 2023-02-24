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

def inRange(head : tuple, tail: tuple):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        return(False)
    return (True)

def aligned(head: tuple, tail: tuple, option: int):
    print(head, tail, option)
    if option:
        if head[0] == tail[0]:
            return(True)
    else:
        if head[1] == tail[1]:
            return (True)
    return (False)

def diagonalized(head: list, tail: list):
    if head[0] > tail[0] and head[1] > tail[1]:
        result = (1, 1)
    elif head[0] > tail[0] and head[1] < tail[1]:
        result = (1, -1)
    elif head[0] < tail[0] and head[1] > tail[1]:
        result = (-1, 1)
    elif head[0] < tail[0] and head[1] < tail[1]:
        result = (-1, -1)
    return ((tail[0] + result[0], tail[1] + result[1]))

def moveRope(instruction: list):
    head = (0, 0)
    tail = (0, 0)
    visited = [(0, 0)]
    dir = {'D' : (1, 0), 'U' : (-1, 0), 'L' : (0, -1), 'R' : (0, 1)}
    for line in instruction:
        for i in range(line[1]):
            head = (head[0] + dir[line[0]][0], head[1] + dir[line[0]][1])
            while not inRange(head, tail):
                if aligned(head, tail, 0) and head[0] < tail[0]:
                    print("---MOVE UP : ", head, tail)
                    tail = (tail[0] + dir['U'][0], tail[1] + dir['U'][1])
                    print("---MOVED UP : ", head, tail)
                if aligned(head, tail, 0) and head[0] > tail[0]:
                    print("---MOVE DOWN : ", head, tail)
                    tail = (tail[0] + dir['D'][0], tail[1] + dir['D'][1])
                    print("---MOVED DOWN : ", head, tail)
                if aligned(head, tail, 1) and head[1] < tail[1]:
                    print("---MOVE LEFT : ", head, tail)
                    tail = (tail[0] + dir['L'][0], tail[1] + dir['L'][1])
                    print("---MOVED LEFT : ", head, tail)
                if aligned(head, tail, 1) and head[1] > tail[1]:
                    print("---MOVE RIGHT : ", head, tail)
                    tail = (tail[0] + dir['R'][0], tail[1] + dir['R'][1])
                    print("---MOVED RIGHT : ", head, tail)
                if not aligned(head, tail , 1) and not aligned(head, tail, 0):
                    tail = diagonalized(head, tail)
            if tail not in visited:
                visited.append(tail)
            print("END INSTRUC", head, tail)
    print((visited))
    return (len(visited))

def parseStrat(content : str):
    tmp = content.splitlines()
    instruction = []
    for line in tmp:
        instruction.append((line.split()[0], int(line.split()[1])))
    return (instruction)

def main(av):
    content = openFile(av)
    table = parseStrat(content)
    total = moveRope(table)
    print(total)

if __name__  == "__main__":
    sys.exit(main(sys.argv[1:]))
