# Projectile Motion
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/
# Use left and right arrows to rotate the cannon. Use the space bar to fire

import turtle
import math
import random
import time

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(width = SCREEN_WIDTH+20, height = SCREEN_HEIGHT + 20)
wn.title("Vector Graphics Demo by TokyoEdTech")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Cannon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 45
        self.shape = "triangle"
        self.power = 10
        
    def rotate_left(self):
        self.angle += 10
        
    def rotate_right(self):
        self.angle -= 10
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.5, 1)
        pen.setheading(self.angle)
        pen.stamp()

class Cannonball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.shape = "circle"
        self.state = "ready"
    
    def update(self, GRAVITY):
        if self.state == "fire":
            self.x += self.dx
            self.y += self.dy
            self.dy += GRAVITY
            
            if self.y < -300:
                self.state = "ready"
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.25, 0.25)
        pen.stamp()
        
    def fire(self):
        if self.state == "ready":
            self.x = cannon.x
            self.y = cannon.y
            self.dx = math.cos(math.radians(cannon.angle)) * cannon.power
            self.dy = math.sin(math.radians(cannon.angle)) * cannon.power
            self.state = "fire"
        

cannon = Cannon(-250, -200)
cannon.render(pen)

cannonball = Cannonball(-250, -200)
cannonball.render(pen)

# Keyboard bindings.
wn.listen()
wn.onkeypress(cannonball.fire, "space")
wn.onkeypress(cannon.rotate_left, "Left")
wn.onkeypress(cannon.rotate_right, "Right")

GRAVITY = -0.1

while True:
    pen.clear()
    
    cannonball.update(GRAVITY)
    
    cannon.render(pen)
    cannonball.render(pen)
    
    wn.update()

wn.mainloop()
