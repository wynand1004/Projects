#SpaceWar by @TokyoEdTech / Written in Python 2.7 
#Part IV: Create an Enemy / Collision Checking

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
		
	def move(self):
		self.fd(self.speed)
		
		#Boundary detection
		if self.xcor() > 290:
			self.setx(290)
			self.rt(60)
		
		if self.xcor() < -290:
			self.setx(-290)
			self.rt(60)
		
		if self.ycor() > 290:
			self.sety(290)
			self.rt(60)
		
		if self.ycor() < -290:
			self.sety(-290)
			self.rt(60)
			
	def is_collision(self, other):
		if (self.xcor() >= (other.xcor() - 20)) and \
		(self.xcor() <= (other.xcor() + 20)) and \
		(self.ycor() >= (other.ycor() - 20)) and \
		(self.ycor() <= (other.ycor() + 20)):
			return True
		else:
			return False
				
class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 4
		self.lives = 3

	def turn_left(self):
		self.lt(45)
		
	def turn_right(self):
		self.rt(45)

	def accelerate(self):
		self.speed += 1
		
	def decelerate(self):
		self.speed -= 1
		
class Enemy(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 6
		self.setheading(random.randint(0,360))	

class Game():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = "playing"
		self.pen = turtle.Turtle()
		self.lives = 3
		
	def draw_border(self):
		#Draw border
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()
		
#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Create my sprites
player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)

#Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

#Main game loop
while True:
	player.move()
	enemy.move()
	
	#Check for a collision with the player
	if player.is_collision(enemy):
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		enemy.goto(x, y)


delay = raw_input("Press enter to finish. > ")