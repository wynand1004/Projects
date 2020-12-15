# Live Coding: Frogger! Part 5
# by @TokyoEdtech

# Topics: Classes, Inheritance, Turtle Graphics
# Adding game objects and their behavior
# Add a one minute timer

# Shoutouts:
# 16-Bit Members Kevin, Paul, Jan, and Mohd
# 8-Bit Member Kim-Siong

import turtle
import math
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.cv._rootwindow.resizable(False, False)
wn.title("Frogger by @tokyoedtech")
wn.setup(600, 800)
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.tracer(0)

# Register shape
shapes = ["frog.gif", "car_left.gif", "car_right.gif", "log_full.gif", "turtle_left.gif", "turtle_right.gif", "turtle_right_half.gif", 
    "turtle_left_half.gif", "turtle_submerged.gif", "home.gif", "frog_home.gif", "frog_small.gif"]
    
for shape in shapes:
    wn.register_shape(shape)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# Create classes
class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()
        
    def update(self):
        pass
        
    def is_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Player(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0
        self.collision = False
        self.frogs_home = 0
        self.max_time = 60
        self.time_remaining = 60
        self.start_time = time.time()
        self.lives = 3
        
    def up(self):
        self.y += 50

    def down(self):
        self.y -= 50

    def right(self):
        self.x += 50

    def left(self):
        self.x -= 50
        
    def update(self):
        self.x += self.dx
        # Border checking
        if self.x < -300 or self.x > 300:
            self.x = 0
            self.y = -300
            
        if self.y < -325:
            self.y = -325
        
        self.time_remaining = self.max_time - round(time.time() - self.start_time)
        
        # Out of time
        if self.time_remaining <= 0:
            player.lives -= 1
            self.go_home()
            
    def go_home(self):
        self.dx = 0
        self.x = 0
        self.y = -325
        self.max_time = 60
        self.time_remaining = 60
        self.start_time = time.time()
        
            
class Car(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400

class Log(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400

class Turtle(Sprite):
    def __init__(self, x, y, width, height, image, dx):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = dx
        self.state = "full" # half, submerged
        self.full_time = random.randint(8, 12)
        self.half_time = random.randint(4, 6)
        self.submerged_time = random.randint(4, 6)
        self.start_time = time.time()
        
    def update(self):
        self.x += self.dx
        
        # Border checking
        if self.x < -400:
            self.x = 400
            
        if self.x > 400:
            self.x = -400
            
        # Update image based on state
        if self.state == "full":
            if self.dx > 0:
                self.image = "turtle_right.gif"
            else:
                self.image = "turtle_left.gif"
        elif self.state == "half_up" or self.state == "half_down":
            if self.dx > 0:
                self.image = "turtle_right_half.gif"
            else:
                self.image = "turtle_left_half.gif"
        elif self.state == "submerged":
            self.image = "turtle_submerged.gif"

                
        # Timer stuff
        if self.state == "full" and time.time() - self.start_time > self.full_time:
            self.state = "half_down"
            self.start_time = time.time()
        elif self.state == "half_down" and time.time() - self.start_time > self.half_time:
            self.state = "submerged"
            self.start_time = time.time()
        elif self.state == "submerged" and time.time() - self.start_time > self.submerged_time:
            self.state = "half_up"
            self.start_time = time.time()
        elif self.state == "half_up" and time.time() - self.start_time > self.half_time:
            self.state = "full"
            self.start_time = time.time()            

class Home(Sprite):
    def __init__(self, x, y, width, height, image):
        Sprite.__init__(self, x, y, width, height, image)
        self.dx = 0

class Timer():
    def __init__(self, max_time):
        self.x = 200
        self.y = -375
        self.max_time = max_time
        self.width = 200
        
    def render(self, time, pen):
        pen.color("green")
        pen.pensize(5)
        pen.penup()
        pen.goto(self.x, self.y)
        pen.pendown()
        percent = time/self.max_time
        dx = percent * self.width
        pen.goto(self.x-dx, self.y)
        pen.penup()

# Create objects
player = Player(0, -325, 40, 40, "frog.gif")
timer = Timer(60)

level_1 = [
    Car(0, -275, 121, 40, "car_left.gif", -0.1),
    Car(221, -275, 121, 40, "car_left.gif", -0.1),
    
    Car(0, -225, 121, 40, "car_right.gif", 0.1),
    Car(221, -225, 121, 40, "car_right.gif", 0.1),
    
    Car(0, -175, 121, 40, "car_left.gif", -0.1),
    Car(221, -175, 121, 40, "car_left.gif", -0.1),
    
    Car(0, -125, 121, 40, "car_right.gif", 0.1),
    Car(221, -125, 121, 40, "car_right.gif", 0.1),
    
    Car(0, -75, 121, 40, "car_left.gif", -0.1),
    Car(221, -75, 121, 40, "car_left.gif", -0.1),
    
    Log(0, 25, 161, 40, "log_full.gif", 0.2),
    Log(261, 25, 161, 40, "log_full.gif", 0.2),
    
    Log(0, 75, 161, 40, "log_full.gif", -0.2),
    Log(261, 75, 161, 40, "log_full.gif", -0.2),
    
    Turtle(0, 125, 155, 40, "turtle_right.gif", 0.15),
    Turtle(255, 125, 155, 40, "turtle_right.gif", 0.15),
    
    Turtle(0, 175, 155, 40, "turtle_left.gif", -0.15),
    Turtle(255, 175, 155, 40, "turtle_left.gif", -0.15),
    
    Log(0, 225, 161, 40, "log_full.gif", 0.2),
    Log(261, 225, 161, 40, "log_full.gif", 0.2)
    ]

homes = [
    Home(0, 275, 50, 50, "home.gif"), 
    Home(-100, 275, 50, 50, "home.gif"),
    Home(-200, 275, 50, 50, "home.gif"),
    Home(100, 275, 50, 50, "home.gif"),
    Home(200, 275, 50, 50, "home.gif")
    ]

# Create list of sprites
sprites = level_1 + homes
sprites.append(player)

# Keyboard binding
wn.listen()
wn.onkeypress(player.up, "Up")
wn.onkeypress(player.down, "Down")
wn.onkeypress(player.right, "Right")
wn.onkeypress(player.left, "Left")

while True:    
    # Render
    for sprite in sprites:
        sprite.render(pen)
        sprite.update()
        
    # Render the timer
    timer.render(player.time_remaining, pen)
    
    # Render the lives
    pen.goto(-290, -375)
    pen.shape("frog_small.gif")
    for life in range(player.lives):
        pen.goto(-280 + (life * 30), -375)
        pen.stamp()
    
    # Check for collisions
    player.dx = 0
    player.collision = False
    for sprite in sprites:
        if player.is_collision(sprite):
            if isinstance(sprite, Car):
                player.lives -= 1
                player.go_home()
                break
            elif isinstance(sprite, Log):
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Turtle) and sprite.state != "submerged":
                player.dx = sprite.dx
                player.collision = True
                break
            elif isinstance(sprite, Home):
                player.go_home()
                sprite.image = "frog.gif"
                player.frogs_home += 1
                break
                
    # Check if we are not touching above y = 0
    if player.y > 0 and player.collision != True:
        player.lives -= 1
        player.go_home()

    # Made it home 5 times
    if player.frogs_home == 5:
        player.go_home()
        player.frogs_home = 0
        for home in homes:
            home.image = "home.gif"
        
    # Player runs out of lives
    if player.lives == 0:
        player.go_home()
        player.frogs_home = 0
        for home in homes:
            home.image = "home.gif"
        player.lives = 3    
    
    # Update screen
    wn.update()

    # Clear the pen
    pen.clear()
