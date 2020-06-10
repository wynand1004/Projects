# Vector Graphics Demo
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/

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


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class VectorShape():
    def __init__(self, shape, x, y, h, scale = 1):
        self.shape = shape
        self.x = x
        self.y = y
        self.h = h
        self.scale = scale
        
    def render(self, pen):
        pen.penup()
        pen.width(2)
        
        # Draw each line
        for i in range(0, len(self.shape)):
            xy = self.shape[i]
            
            # Empty
            if len(xy) == 0:
                pen.penup()
                i += 1
                xy = self.shape[i]
                
            # Rotation code
            angle = (self.h) * (math.pi/180)        
            new_x = math.cos(angle) * (xy[0]) - math.sin(angle) * (xy[1])
            new_y = math.sin(angle) * (xy[0]) + math.cos(angle) * (xy[1])
            pen.goto(self.x + new_x * self.scale, self.y + new_y * self.scale)
            
            pen.pendown()
            
class Starship(VectorShape):
    def __init__(self, shape, x, y, dx, dy, h, dh, scale):
        VectorShape.__init__(self, shape, x, y, h, scale)
        self.dx = dx
        self.dy = dy
        self.dh = dh
        self.speed = random.randint(1, 5)
        
    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x += self.dx
        self.y += self.dy
        self.h += self.dh
        
        self.dx = math.cos(math.radians(self.h)) * self.speed
        self.dy = math.sin(math.radians(self.h)) * self.speed
        
        if self.x > SCREEN_WIDTH / 2.0:
            self.x = -SCREEN_WIDTH / 2.0
        if self.x < -SCREEN_WIDTH / 2.0:
            self.x = SCREEN_WIDTH / 2.0
        if self.y > SCREEN_HEIGHT / 2.0:
            self.y = -SCREEN_HEIGHT / 2.0
        if self.y < -SCREEN_HEIGHT / 2.0:
            self.y = SCREEN_HEIGHT / 2.0

starship = ((-8, 4), (-2, 4), (), (-8, -4), (-2, -4), (), (-5, 3), (-3, 1), (), (-3, -1), (-5, -3), (), (-5, 0), (2, 0), (5, 3), (8, 0), (5, -3), (2,0))

wn.tracer(0)

enterprises = []
for _ in range(50):
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    h = random.randint(0, 360)
    dh = random.randint(-3, 3)
    scale = random.randint(5, 25) / 10

    enterprises.append(Starship(starship, x, y, 0, 0, h, dh, scale))
    
while True:
        
    # Clear the screen
    pen.clear()

    # Update objects
    for enterprise in enterprises:
        enterprise.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        enterprise.render(pen)

    # Update the screen
    wn.update()

wn.mainloop()
