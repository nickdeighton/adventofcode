#Day1 of Advent of Code 2020
#Nick Deighton

def findProduct(find):

    for i in range(0, len(E) - 1):

        r = len(E) -1

        while(i < r):

            if(E[i] + E[r] == find):
                multi = E[i] *E[r]
                print("The numbers are {} and {}".format(E[i], E[r]))
                return multi

            else:
                r -= 1

def findTres(find):
    for i in range(0, len(E) - 2):

        l = i+1
        r = len(E) - 1

        while (l < r):

            if(E[i] + E[l] + E[r] == find):
                tripleMulti = E[i] * E[l] * E[r]
                print("The numbers are {}, {}, and {}".format(E[i], E[l], E[r]))
                return tripleMulti

            elif (E[i] + E[l] + E[r] < find):
                l += 1

            else:
                r -= 1

E = []

with open('expensereport.txt') as f:
    for line in f:
        add = int(line.rstrip())
        E.append(add)

E.sort()

find = 2020

print("Product of two is: {}\n".format(findProduct(find)))
print("Product of 3 is: {}\n".format(findTres(find)))
