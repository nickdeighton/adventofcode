#Day 6 Advent of Code 2020
#Nick Deighton

import re

with open('2020/survey.txt') as f:
    results = f.readlines()

results = [row.rstrip('\n') for row in results]

def count():

    i = 0
    sum = 0
    count = len(results)
    list = []

    while i < count:

        current = results[i]

        if current == '':
            list = []

        else:
            for c in current:
                if c not in list:
                    sum += 1
                    list.append(c)

        i += 1
    return sum

def countB():

    i = 0
    sum = 0
    group = 0
    count = len(results)
    list = []

    while i < count:

        match = []
        current = results[i]
        print(list)

        if current == '':
            sum += len(list)
            list = []
            group = 0

        else:
            if group == 0:
                for m in current:
                    match.append(m)

            if group > 0:
                for d in current:
                    if d in list:
                        match.append(d)

            list = []
            for x in match:
                list.append(x)

            group += 1

        if i + 1 == count:
            sum = sum + len(list)

        i += 1
    return sum

result = countB()
print(result)
