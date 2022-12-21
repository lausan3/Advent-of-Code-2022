sum = 0
biggestSum = [0, 0, 0];

file = open('Day 1 Input.txt', 'r')
lines = file.readlines()

#read input
for line in lines:
  if (line == '\n'):
    sum = 0
    continue

  sum += int(line)

  i = 0

  #if current sum is bigger than an index in the array biggestSum, replace it and go to the next line
  for l in biggestSum:
    if sum > biggestSum[i]:
      biggestSum[i] = sum
      break
    i += 1

print(biggestSum[0] + biggestSum[1] + biggestSum[2])

file.close()