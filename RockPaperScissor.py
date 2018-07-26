#!/bin/python3

from random import randint

player = (input('Rock(r) or Paper(p) or Scissor(s)?'))
print("Player choose : ", player)

computer = randint(1,3)
if(computer == 1):
    computer = 'r'
elif (computer == 2):
    computer = 'p'
else:
    computer = 's'
print("Computer choose : ", computer)

print(player + " vs", end = ' ')
print(computer)

if(player == computer):
    print("DRAW!")
# Rock beats Scissor
elif(player == 'r' and computer == 's'):
    print("Player Wins!")
elif(player == 'r' and computer == 'p'):
    print("Computer Wins!")
# Paper beats Rock
elif(player == 'p' and computer == 'r'):
    print("Player Wins!")
elif(player == 'p' and computer == 's'):
    print("Computer Wins!")
# Scissor beats Paper
elif(player == 's' and computer == 'p'):
    print("Player Wins!")
elif(player == 's' and computer == 'r'):
    print("Computer Wins!")
    