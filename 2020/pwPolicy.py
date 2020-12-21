#Day2 of Advent of Code 2020
#Nick Deighton

def part1():

    pwV = []
    pwI = []

    with open('corrupt.txt') as f:
        for line in f:
            add = line.rstrip()
            info = add.split(': ')
            range = info[0].split(' ')
            numbers = range[0].split('-')

            start = int(numbers[0])
            end = int(numbers[1])
            letter = range[1]
            password = info[1]

            count = 0
            for i in password:
                if i == letter:
                    count += 1

            if (start <= count <= end):
                pwV.append(add)

            else:
                pwI.append(add)

    print("Valid Passwords: {}".format(len(pwV)))
    print("Invalid Passwords: {}".format(len(pwI)))

def part2():

    pwV = []
    pwI = []

    with open('corrupt.txt') as f:
        for line in f:
            add = line.rstrip()
            info = add.split(': ')
            range = info[0].split(' ')
            numbers = range[0].split('-')

            start = int(numbers[0])
            end = int(numbers[1])
            letter = range[1]
            password = info[1]

            count = 0
            if password[start - 1] == letter:
                count += 1

            if password[end - 1] == letter:
                count += 1

            if count == 1:
                pwV.append(add)

            else:
                pwI.append(add)

    print("Valid Passwords: {}".format(len(pwV)))
    print("Invalid Passwords: {}".format(len(pwI)))

part1()
part2()
