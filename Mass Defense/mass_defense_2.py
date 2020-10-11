# Mass Defense Game Part 2
# By @TokyoEdtech
# Python 3.8 using the Geany editor
# Ubuntu Linux

import turtle
import random
import math
import time

wn = turtle.Screen()
wn.setup(1200, 800)
wn.bgcolor("black")
wn.title("Mass Defense Game by @TokyoEdtech")
wn.tracer(0)

class Sprite():
    
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.active = True
        self.heading = 0
        self.health = 10
        
    def render(self):
        Sprite.pen.shapesize(1, 1, 0)
            
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()
        
    def move(self):
        
        self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
        self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
        
        self.x += self.dx
        self.y += self.dy
        
    def is_collision(self, other, tolerance):
        d = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if d < tolerance:
            return True
        else:
            return False

class Defender(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.health = 50
        
    def render(self):

        Sprite.pen.shapesize(2, 2, 0)
            
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()
        
class DefenderWeapon(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.speed = 10
        
    def render(self):

        Sprite.pen.shapesize(0.2, 0.2, 0)
            
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()
        
    def move(self):
        self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
        self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
        
        self.x += self.dx
        self.y += self.dy
        
        # Border checks
        if self.x > 600 or self.x < -600 or self.y > 400 or self.y < -400:
            self.x = -1000
            self.active = False

class Attacker(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)
        self.health = 10
        
    def render(self):
        Sprite.pen.shapesize(1, 1, 0)
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()
        
    def move(self):
        
        self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
        self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
        
        self.x += self.dx
        self.y += self.dy
    
        if self.y > 390 :
            self.heading = random.randint(190, 210)
            
        elif self.y < -390:
            self.heading = random.randint(140, 170)
            
        # Moves off screen
        if self.x < -600:
            self.x += random.randint(1200, 1500)

sprites = []

defenders = []
defender_weapons = []

attackers = []
attacker_weapons = []

# Defenders
for _ in range(10):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    defenders.append(Defender(x, y, "circle", "blue"))

# Attackers
for _ in range(200):
    x = random.randint(300, 500)
    y = random.randint(-300, 300)
    attackers.append(Attacker(x, y, "circle", "red"))
    attackers[-1].speed = random.randint(2, 5)
    attackers[-1].heading = random.randint(160, 200)

# Weapons
for _ in range(10):
    x = -1000
    y = -1000
    defender_weapons.append(DefenderWeapon(x, y, "circle", "lightblue"))
    defender_weapons[-1].active = False
    
# Main game loop
while True:
    # Assign weapon to sprite
    for weapon in defender_weapons:
        if weapon.active == False:
            defender = random.choice(defenders)
            weapon.x = defender.x
            weapon.y = defender.y
            weapon.active = True
            
            # Find enemy to aim at
            attacker = random.choice(attackers)
            weapon.heading = math.atan2(attacker.y - defender.y, attacker.x - defender.x) * 57.298 
            break
    
    # Check for collisions between enemy and weapons
    for weapon in defender_weapons:
        if weapon.active == True:
            for attacker in attackers:
                if attacker.is_collision(weapon, 12):
                    attacker.health -= random.randint(3, 7)
                    if attacker.health <= 0:
                        attackers.remove(attacker)
                    else:
                        attacker.x += weapon.dx
                        attacker.y += weapon.dy
                        
                    weapon.x = -1000
                    weapon.active = False
                    weapon.dx = 0
                    break
                    
    # Check for collisions between attackers and defenders
    for defender in defenders:
        for attacker in attackers:
            if attacker.is_collision(defender, 30):
                attackers.remove(attacker)
                break

    # Move
    for sprite in defenders:
        sprite.move()
        sprite.render()

    for sprite in defender_weapons:
        sprite.move()
        sprite.render()
        
    for sprite in attackers:
        sprite.move()
        sprite.render()

    
    # Update screen
    wn.update()
    
    # Check for a win
    if len(attackers) == 0:
        print("The defenders win.")
        time.sleep(3)
        exit()
    
    
    # Clear screen
    Sprite.pen.clear()

