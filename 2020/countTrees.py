#Day 3 of Advent of Code 2020
#Nick Deighton


with open('2020/path.txt') as f:
    path = f.readlines()

path = [row.rstrip('\n') for row in path]

def runPath(incX, incY):

    trees = 0
    x = 0
    y = 0
    rowCount = len(path)
    colCount = len(path[0])

    while y < rowCount:

        rowText = path[y]
        char = rowText[x]

        if char == '#':
            trees += 1

        if x + incX > colCount - 1:
            x = (x - colCount) + incX
            y += incY

        else:
            x += incX
            y += incY

    return trees

a = runPath(1, 1)
b = runPath(3, 1)
c = runPath(5, 1)
d = runPath(7, 1)
e = runPath(1, 2)

multi = a * b * c * d * e

print(multi)
