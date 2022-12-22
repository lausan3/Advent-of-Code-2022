#read file
file = open('Day 2 Input.txt', 'r')
lines = file.readlines()

points = 0;
elfChoice = ''
playerChoice = ''

#read line by line
for line in lines:
    lineSplit = line.split(" ")

    #elfChoice initialization
<<<<<<< Updated upstream
    if (line[0] == "A"):
        elfChoice = 'rock'
    elif (line[0] == 'B'):
=======
    if (lineSplit[0] == "A"):
        elfChoice = 'rock'
    elif (lineSplit[0] == 'B'):
>>>>>>> Stashed changes
        elfChoice = 'paper'
    else:
        elfChoice = 'scissors'

    #playerChoice initialization
<<<<<<< Updated upstream
    if (line[1] == " X"):
        playerChoice = 'rock'
        points += 1
    elif (line[1] == ' Y'):
=======
    if (lineSplit[1] == "X\n"):
        playerChoice = 'rock'
        points += 1
    elif (lineSplit[1] == 'Y\n'):
>>>>>>> Stashed changes
        playerChoice = 'paper'
        points += 2
    else:
        playerChoice = 'scissors'
        points += 3

    #round start
    #   ties
    if ((elfChoice == 'rock' and playerChoice == 'rock') or (elfChoice == 'paper' and playerChoice == 'paper') or (elfChoice == 'scissors' and playerChoice == 'scissors')):
        points += 3
    #   wins
    if ((elfChoice == 'rock' and playerChoice == 'paper') or (elfChoice == 'paper' and playerChoice == 'scissors') or (elfChoice == 'scissors' and playerChoice == 'rock')):
        points += 6

print(points)