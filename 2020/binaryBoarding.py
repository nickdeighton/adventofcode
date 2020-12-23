#Day 5 Advent of Code 2020
#Nick Deighton

import math

def lineReader():
    with open('2020/seating.txt') as f:
        seating = f.readlines()

    seating = [row.rstrip('\n') for row in seating]

    return seating

def calculate(line):

    rowMax = 127
    rowMin = 0
    colMax = 7
    colMin = 0

    row = 0
    col = 0

    for letter in line:

        if letter == 'F':
            half = (rowMax - rowMin + 1) / 2

            if half == 1:
                row = rowMin
            else:
                rowMax = half + rowMin - 1

        if letter == 'B':
            half = (rowMax - rowMin + 1) / 2

            if half == 1:
                row = rowMax
            else:
                rowMin = rowMin + half

        if letter == 'R':
            half = (colMax - colMin + 1) / 2

            if half == 1:
                col = colMax
            else:
                colMin = colMin + half

        if letter == 'L':
            half = (colMax - colMin + 1) / 2

            if half == 1:
                col = colMin
            else:
                colMax = colMin + half - 1

    return (row * 8) + col

max = 0
passIDs = []
bPass = lineReader()

for p in bPass:

    seat = calculate(p)
    passIDs.append(seat)

    if seat > max:
        max = seat

print(max)

passIDs.sort()

print(passIDs)

myPass = 0

x = 0

for i in passIDs:
    x += 1

    if x < len(passIDs):
        nextID = passIDs[x]

        if nextID - i > 1:
            myPass = i + 1
            break

print(myPass)
