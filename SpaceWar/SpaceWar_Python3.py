#Simple Turtle Graphics Game
#By @TokyoEdTech
#Python 3.x
import os
import random
from tkinter import messagebox

#Import the turtle module
import turtle
#Required on Mac to create turtle window
turtle.fd(0)
#Max animation speed
turtle.speed(0)
#Change the background color of the screen
turtle.bgcolor("black")
#Load the background image
turtle.bgpic("starfield.gif")
#Hide the turtle
turtle.ht()
#Set the undo buffer to 1 (to save memory and speed things up)
turtle.setundobuffer(1)
#Speed up drawing (Draw every 6 frames)
turtle.tracer(0)


class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 0
		
	def is_collision(self, other):
		if (self.xcor() >= (other.xcor() - 20)) and \
			(self.xcor() <= (other.xcor() + 20)) and \
			(self.ycor() >= (other.ycor() - 20)) and \
			(self.ycor() <= (other.ycor() + 20)):
			return True
		else:
			return False
			
	def move(self):
		self.fd(self.speed)
		
		if self.xcor() < -290:
			self.rt(60)
			self.setx(-290)
		
		elif self.xcor() > 290:
			self.rt(60)
			self.setx(290)
			
		if self.ycor() < -290:
			self.rt(60)
			self.sety(-290)		
		
		elif self.ycor() > 290:
			self.rt(60)
			self.sety(290)

class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 0
		self.lives = 3
		self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
		
	def turn_left(self):
		self.lt(45)
		
	def turn_right(self):
		self.rt(45)
				
	def accelerate(self):
		self.speed += 2
		
	def decelerate(self):
		self.speed -= 1
		
	def hyperspace(self):
		os.system("afplay hyperspace.mp3&")
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		self.goto(x, y)
		self.setheading(random.randint(0,360))
		self.speed *= 0.5
		
class Enemy(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 4
		self.setheading(random.randint(0,360))
		if self.xcor() < -290:
			self.rt(degrees)
			self.setx(-290)
		
		elif self.xcor() > 290:
			self.rt(degrees)
			self.setx(290)
			
		if self.ycor() < -290:
			self.rt(degrees)
			self.sety(-290)		
		
		elif self.ycor() > 290:
			self.rt(degrees)
			self.sety(290)
		
		
class Ally(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.speed = 6
		self.setheading(random.randint(0,360))
		
	def move(self):
		self.fd(self.speed)
		
		degrees = random.randint(20, 60)
		
		if self.xcor() < -290:
			self.lt(degrees)
			self.setx(-290)
		
		elif self.xcor() > 290:
			self.lt(degrees)
			self.setx(290)
			
		if self.ycor() < -290:
			self.lt(degrees)
			self.sety(-290)		
		
		elif self.ycor() > 290:
			self.lt(degrees)
			self.sety(290)
			
	def avoid(self, other):
		if (self.xcor() >= (other.xcor() -40)) and \
			(self.xcor() <= (other.xcor() + 40)) and \
			(self.ycor() >= (other.ycor() -40)) and \
			(self.ycor() <= (other.ycor() + 40)):	
			self.lt(30)	


class Bullet(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
		self.status = "ready"
		self.speed = 20
		
	def fire(self):
		if self.status == "ready":
			self.status = "shoot"
		
	def move(self):
		if self.status == "ready":
			self.hideturtle()
			#Move the turtle offscreen
			self.goto(-1000,1000)
		
		if self.status == "shoot":
			os.system("afplay laser.mp3&")
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading())
			self.showturtle()
			self.status = "firing"
		
		if self.status == "firing":
			self.fd(self.speed)
			
		
		#Border Check	
		if self.xcor() < -290 or self.xcor() > 290 \
			or self.ycor() < -290 or self.ycor() > 290:
			self.status = "ready"			
			
class Particle(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, -1000, -1000)
		self.frame = 0
		self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
		
	def explode(self, startx, starty):
		turtle.tracer(8)
		self.goto(startx, starty)
		self.setheading(random.randint(0, 360))
		self.frame = 1

		
	def move(self):
		if self.frame != 0:
			self.fd(18-self.frame)
			self.frame += 1
			
			if self.frame < 6:
				self.shapesize(stretch_wid=0.3, stretch_len=0.3, outline=None)
			elif self.frame < 11:
				self.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)
			else:
				self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
			
			if self.frame > 18:
				self.frame = 0
				self.goto(-1000, -1000)
				turtle.tracer(6)
						
class Game():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = "splash"
		self.pen = turtle.Turtle()
		self.lives = 3
		
	def draw_border(self):
		#Draw Border
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
		
	def show_status(self):
		self.pen.undo()
		if game.lives > 0:
			msg = "Level: %s Lives: %s Score: %s " %(self.level, self.lives, self.score)		
		else: 
			msg = "Game Over Score: %s" %(self.score)
		self.pen.penup()
		self.pen.goto(-300, 310)
		self.pen.write(msg, font=("Arial", 16, "normal"))

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Show the level and score
game.show_status()

#Create player and enemy objects
player = Player("triangle", "white", 0.0, 0.0)
#enemy = Enemy("circle", "red", 100.0, 0.0)
bullet = Bullet("triangle", "yellow", 0.0, 0.0)
#ally = Ally("square", "blue", 100, 100)

#Keyboard Bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.hyperspace, "Down")
turtle.onkey(bullet.fire, "space")
turtle.listen()

#Set up the game
#Create lists for sprites
#Add Enemies
if game.state == "splash":
	enemies = []

	for e in range(6):
		x = random.randint(-200, 200)
		y = random.randint(-200, 200)
		enemies.append(Enemy("circle", "red", x, y))

	#Add Allies
	allies = []
	for a in range(6):
		x = random.randint(-200, 200)
		y = random.randint(-200, 200)
		allies.append(Ally("square", "blue", x, y))
		
	particles = []

	for p in range(2):
		particles.append(Particle("circle", "yellow", -1000, -1000))
	for p in range(2):
		particles.append(Particle("circle", "red", -1000, -1000))
	for p in range(2):
		particles.append(Particle("circle", "orange", -1000, -1000))



	game.state = "playing"

while True:
	turtle.update()
	if game.state == "restart":
		game.lives = 3
		game.score = 0
		player.speed = 0
		player.goto(0,0)
		player.setheading(0)

		for enemy in enemies:
			enemy.goto(random.randint(-200, 200), random.randint(-200, 200))

		for ally in allies:
			ally.goto(random.randint(-200, 200), random.randint(-200, 200))	
		
		game.state = "playing"
	
	if game.state == "playing":
		player.move()
		bullet.move()
	
		for enemy in enemies:	
			enemy.move()

			#Check collisions
			if player.is_collision(enemy):
				os.system("afplay explosion.mp3&")
				player.color("red")
				for particle in particles:
					particle.explode(enemy.xcor(), enemy.ycor())
				player.rt(random.randint(100, 200))
				enemy.goto(random.randint(-200, 200), random.randint(-200, 200))	
				enemy.speed += 1
				game.lives -= 1
				if game.lives < 1:
					game.state = "gameover"
				game.show_status()
				player.color("white")
		
			if bullet.is_collision(enemy):
				os.system("afplay explosion.mp3&")
				for particle in particles:
					particle.explode(enemy.xcor(), enemy.ycor())
					
				bullet.status = "ready"
				enemy.goto(random.randint(-200, 200), random.randint(-200, 200))	
				enemy.speed += 1
				game.score += 100
				game.show_status()
			
		for ally in allies:
			ally.move()
			
			#Avoid enemy
			for enemy in enemies:	
				ally.avoid(enemy)
			
			#Allies should avoid player as well	
			ally.avoid(player)
	
			#Check collisions
			if bullet.is_collision(ally):
				os.system("afplay explosion.mp3&")
				for particle in particles:
					particle.explode(ally.xcor(), ally.ycor())
				bullet.status = "ready"
				ally.goto(random.randint(-200, 200), random.randint(-200, 200))	
				ally.speed += 1
				game.score -= 50
				game.show_status()
				
	for particle in particles:
		particle.move()
				
	if game.state == "gameover":
		for i in range(360):
			player.rt(1) 
		
		if messagebox.askyesno("Game Over", "Play again?") == True:
			game.state = "restart"
		else:
			exit()		
		
	
