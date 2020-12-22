# VecTrek Technology Demo
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

# Snake Shoutouts: Kevin & Paul
# Invader Shoutouts: Jan, Mohd, Kim-Siong, and Finnesz

import turtle
import math
import random
import time

SCREEN_WIDTH = 1200  
SCREEN_HEIGHT = 800

wn = turtle.Screen()
wn.setup(width = SCREEN_WIDTH+20, height = SCREEN_HEIGHT + 20)
wn.title("VecTrek Technology Demo by TokyoEdtech")
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
        self.active = True
        self.color = "white"
        self.phaser_power = 100
        self.photon_torpedos = 1
        self.shields = 100
        
        min_x = self.shape[0][0]
        max_x = self.shape[0][0]
        min_y = self.shape[0][1]
        max_y = self.shape[0][1]
        for xy in self.shape:
            if len(xy) == 2:
                x = xy[0] * scale
                y = xy[1] * scale
                
                if x < min_x:
                    min_x = x
                if x > max_x:
                    max_x = x
                if y < min_y:
                    min_y = y
                if y > max_y:
                    max_y = y
                    
        self.width = max_x - min_x
        self.height = max_y - min_y
        
    def render(self, pen):
        if self.active:
            pen.penup()
            pen.width(2)
            pen.color(self.color)
            
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

    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
        
    def get_distance(self, other):
        return (((self.x-other.x)**2)+((self.y-other.y)**2))**0.5
            
class Starship(VectorShape):
    def __init__(self, shape, x, y, dx, dy, h, dh, scale):
        VectorShape.__init__(self, shape, x, y, h, scale)
        self.dx = dx
        self.dy = dy
        self.dh = dh
        self.speed = 0
        self.active = True
        
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

    def fire_phaser(self, enemy):
        min_distance = 10000
        target = None
        for vector in vectors:
            if isinstance(vector, Enemy):
                distance_to_enemy = vector.get_distance(player)
                if distance_to_enemy < min_distance:
                    min_distance = distance_to_enemy
                    target = vector
        if target:
            phaser.fire(self, target)
            target.shields -= 10     

class PhotonTorpedo(VectorShape):
    def __init__(self, shape, x, y, dx, dy, h, dh, scale):
        VectorShape.__init__(self, shape, x, y, h, scale)
        self.dx = dx
        self.dy = dy
        self.dh = dh
        self.speed = 0
        self.active = False
        self.color = "yellow"
        
    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x += self.dx
        self.y += self.dy
        self.h += self.dh
        
        self.dx = math.cos(math.radians(self.h)) * self.speed
        self.dy = math.sin(math.radians(self.h)) * self.speed
        
        if self.x > SCREEN_WIDTH / 2.0:
            self.active = False
        if self.x < -SCREEN_WIDTH / 2.0:
            self.active = False
        if self.y > SCREEN_HEIGHT / 2.0:
            self.active = False
        if self.y < -SCREEN_HEIGHT / 2.0:
            self.active = False

class Enemy(VectorShape):
    def __init__(self, shape, x, y, dx, dy, h, dh, scale):
        VectorShape.__init__(self, shape, x, y, h, scale)
        self.dx = dx
        self.dy = dy
        self.dh = dh
        self.speed = 0
        self.active = True
        self.color = "green"
        
        
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
            
        # Check status
        if self.shields <= 0:
            self.destroy()
            
    def destroy(self):
        self.active = False
        self.x = -100000
        self.y = -100000

class Phaser():
    def __init__(self):
        self.v1 = None
        self.v2 = None
        self.timer = 0
        self.active = False

    def fire(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.timer = 10
        self.active = True

    def render(self, pen):
        if self.active and self.timer > 0:
            pen.penup()
            pen.goto(self.v1.x, self.v1.y)
            pen.color("red")
            pen.pendown()
            pen.pensize(3)
            pen.goto(self.v2.x, self.v2.y)
            pen.penup()
            pen.pensize(1)
            self.timer -= 1
        else:
            self.reset()
            
    def reset(self):
        self.v1 = None
        self.v2 = None
        self.timer = 0
        self.active = 0
        
    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        pass

starship_shape = ((-8, 4), (-2, 4), (), (-8, -4), (-2, -4), (), (-5, 3), (-3, 1), (), (-3, -1), (-5, -3), (), (-5, 0), (2, 0), (5, 3), (8, 0), (5, -3), (2,0))
photon_torpedo_shape = ((-2, 0), (-1, 1), (0, -1), (1, 1), (2, 0))
bird_of_prey_shape = ((-8,0),(-5,5),(-2,0),(-5,-5),(-8,0),(),(-7,6),(-3,6),(),(-7,-6),(-3,-6),(),(-2,0),(2,0),(4,2),(6,0),(4,-2),(2,0))
phaser = Phaser()

wn.tracer(0)

def player_left():
    player.h += 30
    
def player_right():
    player.h -= 30
    
def player_accelerate():
    player.speed += 0.1
    
def player_decelerate():
    player.speed -= 0.1

def player_fire_photon():
    if photon_torpedo.active == False:
        photon_torpedo.x = player.x
        photon_torpedo.y = player.y
        photon_torpedo.h = player.h
        photon_torpedo.speed = 1
        photon_torpedo.active = True
        
def player_fire_phaser():
    player.fire_phaser(vectors)
    
# Keyboard Binding
wn.listen()
wn.onkeypress(player_left, "Left")
wn.onkeypress(player_right, "Right")
wn.onkeypress(player_accelerate, "Up")
wn.onkeypress(player_decelerate, "Down")
wn.onkeypress(player_fire_photon, "space")
wn.onkeypress(player_fire_phaser, "Shift_L")

player = Starship(starship_shape, 0, 0, 0, 0, 90, 0, 2.0)
photon_torpedo = PhotonTorpedo(photon_torpedo_shape, 0, 0, 0, 0, 0, 0, 1.0)
enemy_torpedo = PhotonTorpedo(photon_torpedo_shape, 0, 0, 0, 0, 0, 0, 1.0)

vectors = [player, photon_torpedo, phaser, enemy_torpedo]

for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    h = random.randint(0, 360)
    vectors.append(Enemy(bird_of_prey_shape, x, y, 0, 0, h, 0, 2))
    vectors[-1].speed = 0.2

while True:
    # Clear the screen
    pen.clear()

    # Update vectors
    for vector in vectors:
        vector.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        vector.render(pen)

        if isinstance(vector, Enemy):
            if vector.is_aabb_collision(photon_torpedo):
                vector.shields -= 50
                photon_torpedo.x = 1000
                photon_torpedo.y = 1000
                photon_torpedo.active = False
                
    # Fire enemy torpedo
    if enemy_torpedo.active == False:
        vector = random.choice(vectors)
        if isinstance(vector, Enemy) and vector.get_distance(player) < 200:
            enemy_torpedo.x = vector.x
            enemy_torpedo.y = vector.y
            enemy_torpedo.h = vector.h
            enemy_torpedo.speed = 1
            enemy_torpedo.active = True

    # Update the screen
    wn.update()

wn.mainloop()
