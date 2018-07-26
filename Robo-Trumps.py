#!/bin/python3

from turtle import *

screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()

robots={}
file = open("cards.txt",'r')
for line in file.read().splitlines():
  name,battery,intelligence,image=line.split(',')
  robots[name]=[battery,intelligence,image]
  screen.register_shape(image)
  
file.close()
print(robots)

while True:
  robot = input("Choose a Robot : ")
  if robot in robots:
    stats = robots[robot]
    style=('Arial',14,'bold')
    clear()
    goto(0,100)
    shape(stats[2])
    setheading(90)
    stamp()
    setheading(-90)
    forward(60)
    write('Name : ' + robot, font=style, align='centre')
    forward(25)
    write('Battery : ' + stats[0], font=style, align='centre')
    forward(25)
    write('Intelligance : ' + stats[1], font=style, align='centre')
  else:
    print("Robot doesn\'t exist")