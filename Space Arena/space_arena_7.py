# Space Arena! 
# The Ultimate Python Turtle Graphics Game Tutorial
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/
# Part 7: Arena Borders

import turtle
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Space Arena! by @TokyoEdTech")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def render_border(self, pen):
        pen.color("white")
        pen.width(3)
        pen.penup()
        
        left = -self.width/2.0
        right = self.width/2.0
        top = self.height/2.0
        bottom = -self.height/2.0
        
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()
        

class Sprite():
    # Constructor
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0.0
        self.acceleration = 0.2
        self.health = 100
        self.max_health = 100
        
    def update(self):
        self.heading += self.da
        self.heading %= 360
        
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
        self.x += self.dx
        self.y += self.dy
        
        self.border_check()
        
    def border_check(self):
        if self.x > game.width/2.0 - 10:
            self.x = game.width/2.0 - 10
            self.dx *= -1
            
        elif self.x < -game.width/2.0 + 10:
            self.x = -game.width/2.0 + 10
            self.dx *= -1

        if self.y > game.height/2.0 - 10:
            self.y = game.height/2.0 - 10
            self.dy *= -1
            
        elif self.y < -game.height/2.0 + 10:
            self.y = -game.height/2.0 + 10
            self.dy *= -1            
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        
        self.render_health_meter(pen)
        
    def render_health_meter(self, pen):
        # Draw health meter
        pen.goto(self.x - 10, self.y + 20)
        pen.width(3)
        pen.pendown()
        pen.setheading(0)
        
        if self.health/self.max_health < 0.3:
            pen.color("red")
        elif self.health/self.max_health < 0.7:
            pen.color("yellow")
        else:
            pen.color("green")

        pen.fd(20.0 * (self.health/self.max_health))
        
        if self.health != self.max_health:
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health-self.health)/self.max_health))
        
        pen.penup()
        
class Player(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, 0, 0, shape, color)
        self.lives = 3
        self.score = 0
        self.heading = 90
        self.da = 0
        
    def rotate_left(self):
        self.da = 5
        
    def rotate_right(self):
        self.da = -5
        
    def stop_rotation(self):
        self.da = 0
        
    def accelerate(self):
        self.thrust += self.acceleration
        
    def decelerate(self):
        self.thrust = 0.0
        
    def render(self, pen):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        
        pen.shapesize(1.0, 1.0, None)
        
        self.render_health_meter(pen)

# Create game object
game = Game(1000, 300)

# Create player sprite
player = Player(0, 0, "triangle", "white")

enemy = Sprite(0, 100, "square", "red")
enemy.dx = -1
enemy.dy = -0.3

powerup = Sprite(0, -100, "circle", "blue")
powerup.dy = 1
powerup.dx = 0.1

# Sprites list
sprites = []
sprites.append(player)
sprites.append(enemy)
sprites.append(powerup)

# Keyboard bindings
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")

wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")

wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")

# Main Loop
while True:
    # Clear screen
    pen.clear()
    
    # Do game stuff
    # Update sprites
    for sprite in sprites:
        sprite.update()

    # Render sprites
    for sprite in sprites:
        sprite.render(pen)
    
    game.render_border(pen)
    
    # Update the screen
    wn.update()
    

