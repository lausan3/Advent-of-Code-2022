#read file
file = open('Day 2 Input.txt', 'r')
lines = file.readlines()

points = 0;
elfChoice = ''
playerChoice = ''

#read line by line
for line in lines:

    #elfChoice initialization
    if (line.split(" ")[0] == "A"):
        elfChoice = 'rock'
    elif (line.split(" ")[0] == 'B'):
        elfChoice = 'paper'
    else:
        elfChoice = 'scissors'

    #playerChoice initialization
    if (line.split(" ")[1] == " X"):
        playerChoice = 'rock'
        points += 1
    elif (line.split(" ")[1] == ' Y'):
        playerChoice = 'paper'
        points += 2
    else:
        playerChoice = 'scissors'
        points += 3

    print(elfChoice, playerChoice)

    #round start
    #   ties
    if ((elfChoice == 'rock' and playerChoice == 'rock') or (elfChoice == 'paper' and playerChoice == 'paper') or (elfChoice == 'scissors' and playerChoice == 'scissors')):
        points += 3
    #   wins
    if ((elfChoice == 'rock' and playerChoice == 'paper') or (elfChoice == 'paper' and playerChoice == 'scissors') or (elfChoice == 'scissors' and playerChoice == 'rock')):
        points += 6

    print(points)

print(points)