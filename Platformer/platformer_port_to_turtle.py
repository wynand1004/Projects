# Porting a Platformer Game From Pygame to the Turtle Module
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import turtle
import sys
import math
import random

WIDTH = 1200
HEIGHT = 800

GRAVITY = -0.01

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
wn = turtle.Screen()
wn.colormode(255)
wn.title("Platformer Game Intro by @TokyoEdtech")
wn.setup(WIDTH, HEIGHT)
wn.bgcolor(BLACK)
wn.tracer(0)

# Create pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color(WHITE)
pen.hideturtle()

# Create classes
class Sprite():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.color = WHITE
        self.friction = 0.99
        
    def goto(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        pen.pencolor(self.color)
        pen.fillcolor(self.color)
        pen.penup()
        pen.goto(self.x-self.width/2.0, self.y+self.height/2.0)
        pen.pendown()
        pen.begin_fill()
        pen.goto(self.x+self.width/2.0, self.y+self.height/2.0)
        pen.goto(self.x+self.width/2.0, self.y-self.height/2.0)
        pen.goto(self.x-self.width/2.0, self.y-self.height/2.0)
        pen.goto(self.x-self.width/2.0, self.y+self.height/2.0)
        pen.end_fill()
        pen.penup()

    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self, x, y, width, height)
        self.color=GREEN
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy += GRAVITY
        
    def jump(self):
        self.dy = 2.5
        
    def left(self):
        self.dx -= 1
        if self.dx < -3:
            self.dx = -3
        
    def right(self):
        self.dx += 1
        if self.dx > 3:
            self.dx = 3

# Create font

# Create sounds

# Create game objects
player = Player(0, 400, 20, 40)
blocks = []
blocks.append(Sprite(0, 200, 400, 20))
blocks.append(Sprite(0, 0, 600, 20))
blocks.append(Sprite(0, -200, 1000, 20))
blocks.append(Sprite(400, -100, 100, 200))
blocks.append(Sprite(-400, -100, 100, 200))

def player_jump():
    for block in blocks:
        if player.is_aabb_collision(block):
            player.jump()
            break

# Keyboard binding
wn.listen()
wn.onkeypress(player.left, "Left")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player_jump, "space")

# Main game loop
while True:
    # Move/Update objects
    player.move()

    # Check for collisions
    for block in blocks:
        if player.is_aabb_collision(block):
            # Player is to the left
            if player.x < block.x - block.width/2.0 and player.dx > 0:
                player.dx = 0
                player.x = block.x - block.width/2.0 - player.width/2.0
            # Player is to the right
            elif player.x > block.x + block.width/2.0 and player.dx < 0:
                player.dx = 0
                player.x = block.x + block.width/2.0 + player.width/2.0
            # Player is above
            elif player.y > block.y:
                player.dy = 0
                player.y = block.y + block.height/2.0 + player.height/2.0 - 1
                player.dx *= block.friction
            # Player is below
            elif player.y < block.y:
                player.dy = 0
                player.y = block.y - block.height/2.0 - player.height/2.0 

    # Border check the player
    if player.y < -400:
        player.goto(0, 400)
        player.dx = 0
        player.dy = 0
        
    # Render (Draw stuff)
    
    # Render objects
    player.render()
    for block in blocks:
        block.render()
     
    # Flip the display
    wn.update()
    
    # Clear the screen
    pen.clear()
