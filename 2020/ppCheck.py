#Day 4 of Advent of Code 2020
#Nick Deighton

import re

with open('2020/passports.txt') as f:
    passports = f.readlines()

passports = [row.rstrip('\n') for row in passports]

reqID = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyeID = ['amb', 'blu', 'brn', 'gry','grn', 'hzl', 'oth']

def allowed_char(test):
    charRe = re.compile(r'[a-f0-9]*')
    test = charRe.search(test)
    return bool(test)

def countValid():

    i = 0
    tracker = 0
    counter = 0
    count = len(passports)

    while i < count:

        current = passports[i]

        if current == '':
            tracker = 0

        else:
            lineSplit = current.split(' ')

            for c in lineSplit:
                code = c.split(':')
                if code[0] in reqID:

                    if code[0] == 'byr' and code[1].isdigit():
                        if 1920 <= int(code[1]) <= 2002:
                            tracker += 1

                    elif code[0] == 'iyr' and code[1].isdigit():
                        if 2010 <= int(code[1]) <= 2020:
                            tracker += 1

                    elif code[0] == 'eyr' and code[1].isdigit():
                        if 2020 <= int(code[1]) <= 2030:
                            tracker += 1

                    elif code[0] == 'hgt' and code[1].isalnum():
                        if 'cm' in code[1]:
                            sp = code[1].split('cm')
                            if 150 <= int(sp[0]) <= 193:
                                tracker += 1
                        if 'in' in code[1]:
                            sp = code[1].split('in')
                            if 59 <= int(sp[0]) <= 76:
                                tracker += 1

                    elif code[0] == 'hcl':
                        hair = code[1]
                        if hair[0] == '#':
                            cut = hair[1:len(hair)]
                            if len(cut) == 6 and allowed_char(cut):
                                tracker += 1

                    elif code[0] == 'ecl' and code[1] in eyeID:
                            tracker += 1

                    elif code[0] == 'pid' and code[1].isdigit() and len(code[1]) == 9:
                            tracker += 1

        if tracker >= 7:
            counter += 1
            tracker = 0

        i += 1


    return counter

print(countValid())
