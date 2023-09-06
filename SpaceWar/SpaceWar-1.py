#SpaceWar by @TokyoEdTech / Written in Python 2.7 
#Part I: Getting Started

import os
import random

#Import the Turtle module
import turtle
#Required by MacOSX to show the window
turtle.fd(0)
#Set the animations speed to the maximum
turtle.speed(0)
#Change the background color
turtle.bgcolor("black")
#Hide the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1
		

#Create my sprites
player = Sprite("triangle", "white", 0, 0)






delay = raw_input("Press enter to finish. > ")