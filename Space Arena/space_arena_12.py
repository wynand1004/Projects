# Space Arena! 
# The Ultimate Python Turtle Graphics Game Tutorial
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/
# Part 12: Player/Enemy Collisions

import turtle
import math
import random

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
        self.level = 1
        
    def start_level(self):
        sprites.clear()
        
        # Add player
        sprites.append(player)
        
        # Add missile
        sprites.append(missile)
        
        # Add enemies
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, -2)
            sprites.append(Enemy(x, y, "square", "red"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy
            
        # Add powerups
        for _ in range(self.level):
            x = random.randint(-self.width/2, self.width/2)
            y = random.randint(-self.height/2, self.height/2)
            dx = random.randint(-2, 2)
            dy = random.randint(-2, -2)
            sprites.append(Powerup(x, y, "circle", "blue"))
            sprites[-1].dx = dx
            sprites[-1].dy = dy
            
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
        self.width = 20
        self.height = 20
        self.state = "active"

    def is_collision(self, other):
        if self.x < other.x + other.width and\
            self.x + self.width > other.x and\
            self.y < other.y + other.height and\
            self.y + self.height > other.y:
            return True
        else:
            return False

    def bounce(self, other):
        temp_dx = self.dx
        temp_dy = self.dy
        
        self.dx = other.dx
        self.dy = other.dy
        
        other.dx = temp_dx
        other.dy = temp_dy

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
        if self.state == "active":
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
    
    def fire(self):
        missile.fire(self.x, self.y, self.heading, self.dx, self. dy)
        
    def update(self):
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            
            self.x += self.dx
            self.y += self.dy
            
            self.border_check()
            
            # Check health
            if self.health <= 0:
                self.reset()
            
    def reset(self):
        self.x = 0
        self.y = 0
        self.health = self.max_health
        self.heading = 90
        self.dx = 0
        self.dy = 0
        self.lives -= 1
        
    def render(self, pen):
        pen.shapesize(0.5, 1.0, None)
        pen.goto(self.x, self.y)
        pen.setheading(self.heading)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()
        
        pen.shapesize(1.0, 1.0, None)
        
        self.render_health_meter(pen)

class Missile(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 8.0
        self.max_fuel = 200
        self.fuel = self.max_fuel
        self.height = 4
        self.width = 4

    def fire(self, x, y, heading, dx, dy):
        if self.state == "ready":
            self.state = "active"
            self.x = x
            self.y = y
            self.heading = heading
            self.dx = dx
            self.dy = dy
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust

    def update(self):
        if self.state == "active":
            self.fuel -= self.thrust
            if self.fuel <= 0:
                self.reset()
            
            self.heading += self.da
            self.heading %= 360
        
            self.x += self.dx
            self.y += self.dy
            
            self.border_check()

    def reset(self):
        self.fuel = self.max_fuel
        self.dx = 0
        self.dy = 0
        self.state = "ready"

    def render(self, pen):
        if self.state == "active":
            pen.shapesize(0.2, 0.2, None)
            pen.goto(self.x, self.y)
            pen.setheading(self.heading)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.stamp()
            
            pen.shapesize(1.0, 1.0, None)

class Enemy(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = 20
        self.health = self.max_health

    def update(self):
        if self.state == "active":
            self.heading += self.da
            self.heading %= 360
            
            self.dx += math.cos(math.radians(self.heading)) * self.thrust
            self.dy += math.sin(math.radians(self.heading)) * self.thrust
            
            self.x += self.dx
            self.y += self.dy
            
            self.border_check()
            
            # Check health
            if self.health <= 0:
                self.reset()
            
    def reset(self):
        self.state = "inactive"
        
class Powerup(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

# Create game object
game = Game(700, 500)

# Create player sprite
player = Player(0, 0, "triangle", "white")

# Create missile object
missile = Missile(0, 100, "circle", "yellow")

# Sprites list
sprites = []

# Setup the level
game.start_level()

# Keyboard bindings
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")

wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")

wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")

wn.onkeypress(player.fire, "space")

# Main Loop
while True:
    # Clear screen
    pen.clear()
    
    # Do game stuff
    # Update sprites
    for sprite in sprites:
        sprite.update()
        
    # Check for collisions
    for sprite in sprites:
        if isinstance(sprite, Enemy) and sprite.state == "active":
            if player.is_collision(sprite):
                sprite.health -= 10
                player.health -= 10
                player.bounce(sprite)
                
            if missile.state == "active" and missile.is_collision(sprite):
                sprite.health -= 10
                missile.reset()
                
        if isinstance(sprite, Powerup):
            if player.is_collision(sprite):
                sprite.x = 100
                sprite.y = 100
                
            if missile.state == "active" and missile.is_collision(sprite):
                sprite.x = 100
                sprite.y = -100
                missile.reset()
            

    # Render sprites
    for sprite in sprites:
        sprite.render(pen)
    
    game.render_border(pen)
    
    # Check for end of level
    end_of_level = True
    for sprite in sprites:
        # Look for an active enemy
        if isinstance(sprite, Enemy) and sprite.state == "active":
            end_of_level = False
    if end_of_level:
        game.level += 1
        game.start_level()
    
    # Update the screen
    wn.update()
    

