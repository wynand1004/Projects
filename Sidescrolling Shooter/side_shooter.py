# TokyoEdTech
# Side Scrolling Shooter
# Geany IDE
# Python 3.8
# Linux
# Live Coding Demo: https://youtu.be/oNOCx9My8FY

import turtle
import random

wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Sidescrolling Shooter by TokyoEdTech")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()

# Create classes
class Player():
	def __init__(self):
		self.color = "green"
		self.x = -350
		self.y = 0
		self.shape = "triangle"
		self.dy = 0
		self.dx = 0
		
	def up(self):
		self.dy = 0.4
		
	def down(self):
		self.dy = -0.4
	
	def left(self):
		self.dx = -0.4
	
	def right(self):
		self.dx = 0.4
	
	def move(self):
		self.y = self.y + self.dy
		self.x = self.x + self.dx
		
		# Check for border collision
		if self.y > 280:
			self.y = 280
			self.dy = 0
			
		elif self.y < -280:
			self.y = -280
			self.dy = 0
			
		if self.x < -390:
			self.x = -390
			self.dx = 0
		
		elif self.x > -190:
			self.x = -190
			self.dx = 0
	
	def distance(self, other):
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
			
	def render(self, pen):
		pen.goto(self.x, self.y)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.shapesize(1, 1, 0)
		pen.stamp()

class Missile():
	def __init__(self):
		self.color = "red"
		self.x = 0
		self.y = 1000
		self.shape = "circle"
		self.size = 0.3
		self.dx = 0
	
	def fire(self):
		self.x = player.x
		self.y = player.y
		self.dx = 1
	
	def move(self):
		self.x = self.x + self.dx 

	def distance(self, other):
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

	def render(self, pen):
		pen.goto(self.x, self.y)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.shapesize(0.3, 0.3, 0)
		pen.stamp()

class Enemy():
	def __init__(self):
		colors = ["yellow", "purple", "blue", "white", "gray"]
		self.color = random.choice(colors)
		self.x = 400
		self.y = random.randint(-290, 290)
		self.shape = "square"
		self.dx = random.randint(1, 5) / -10

	def move(self):
		self.x = self.x + self.dx
		
		# Border check
		if self.x < -400:
			self.x = random.randint(400, 480)
			self.y = random.randint(-350, 350)
			self.dx *= 1.1		

	def distance(self, other):
		return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

	def render(self, pen):
		pen.goto(self.x, self.y)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.shapesize(1, 1, 0)
		pen.stamp()
	
# Create game objects
player = Player()
missile = Missile()

# Create enemies
enemies = []

for _ in range(5):
	enemies.append(Enemy())


# Keyboard binding
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.right, "Right")
wn.onkeypress(missile.fire, "space")

# Main game loop
while True:
	wn.update()
	pen.clear()
	
	player.move()
	missile.move()
	
	player.render(pen)
	missile.render(pen)
	
	for enemy in enemies:
		enemy.move()
		
		# Check for collision
		if enemy.distance(missile) < 13:
			enemy.x = 400
			enemy.y = random.randint(-350, 350)
			enemy.dx *= 0.8
			missile.dx = 0
			missile.x = 0
			missile.y = 1000
		
		# Check for collision
		if enemy.distance(player) < 20:
			print("Game over!")
			exit()
			
		enemy.render(pen)


