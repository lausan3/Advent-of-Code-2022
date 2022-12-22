#read file
file = open('Day 2 Input.txt', 'r')
lines = file.readlines()

points = 0
elfChoice = ''
condition = ''

#read line by line
for line in lines:
    lineSplit = line.split(" ")

    #elfChoice initialization
    if (lineSplit[0] == "A"):
        elfChoice = 'rock'
    elif (lineSplit[0] == 'B'):
        elfChoice = 'paper'
    else:
        elfChoice = 'scissors'

    #playerChoice initialization
    if (lineSplit[1] == "X\n"):
        condition = 'loss'
    elif (lineSplit[1] == 'Y\n'):
        condition = 'tie'
        points += 3
    else:
        condition = 'win'
        points += 6

    #round start
    #   losses
    if (condition == 'loss'):
        # choice check
        if (elfChoice == "rock"):
            points += 3
        elif (elfChoice == 'paper'):
            points += 1
        else:
            points += 2
    #   ties
    if (condition == 'tie'):
        # choice check
        if (elfChoice == "rock"):
            points += 1
        elif (elfChoice == 'paper'):
            points += 2
        else:
            points += 3
    #   wins
    if (condition == 'win'):
        # choice check
        if (elfChoice == "rock"):
            points += 2
        elif (elfChoice == 'paper'):
            points += 3
        else:
            points += 1


print(points)