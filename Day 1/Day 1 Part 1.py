sum = 0
biggestSum = 0;

file = open('Day 1 Input.txt', 'r')
lines = file.readlines()

for line in lines:
    if (line == '\n'):
      sum = 0
      continue

    sum += int(line)

    if sum > biggestSum:
      biggestSum = sum

print(biggestSum)

file.close()