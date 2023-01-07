from string import ascii_lowercase
import math

sum = 0

with open('Day 3 Input.txt', 'r') as f:
    for line in f:
    # maybe \n is considered in len(), careful
        half = math.ceil(len(line)/2)

        rucksack1 = line[0:half]
        rucksack2 = line[half:]

        print(rucksack1)
        print(rucksack2)

        for item in rucksack1:
            for itemCheck in rucksack2:
                if item == itemCheck and item.islower():
                    sum += int(ascii_lowercase.index(item))
                    print(sum)
                    break
                else:
                    sum += int(ascii_lowercase.index(item)) + 26
                    print(sum)
                    break

print(sum)