#Day 4 of Advent of Code 2020
#Nick Deighton

with open('2020/passports.txt') as f:
    passports = f.readlines()

passports = [row.rstrip('\n') for row in passports]

reqID = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def countValid():

    i = 0
    count = len(passports)

    while i < count:

        current = passports[i]

        if current == '':
            tracker = 0
            
        lineSplit = current.split(':')

        tracker = 0

        j = 0
        while j < len(lineSplit):

            req = lineSplit[j]
            if req in reqID:
                tracker += 1

            j += 2
