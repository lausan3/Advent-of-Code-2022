from string import ascii_lowercase

file = open('Day 3 Input.txt', 'r')
lines = file.readlines()

rucksack1 = ''
rucksack2 = ''

sum = 0

for line in lines:
    # maybe \n is considered in len(), careful
    rucksack1 = line[0, len(line)/2]
    rucksack2 = line[len(line)/2, ]

    print(rucksack1)
    print(rucksack2)

    for item in rucksack1:
        for itemCheck in rucksack2:
            if item.islower():
                sum += item.ascii_lowercase()
                print(sum)
                break
            else:
                sum += item.ascii_lowercase() + 26