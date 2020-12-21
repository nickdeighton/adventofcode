#Day 4 of Advent of Code 2020
#Nick Deighton

with open('2020/passports.txt') as f:
    passports = f.readlines()

passports = [row.rstrip('\n') for row in passports]

reqID = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

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
            lineSplit = current.split(':')

            j = 0
            while j < len(lineSplit):

                req = lineSplit[j]
                if req in reqID:
                    tracker += 1

                j += 2
                
        if tracker >= 7:
            counter += 1
            tracker = 0
        
        i++
        
        
    return counter
    
print(countValid())


