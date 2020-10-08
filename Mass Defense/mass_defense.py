# Mass Defense Game
# By @TokyoEdtech
# Python 3.8 using the Geany editor
# Ubuntu Linux

import turtle
import random

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
    
    def __init__(self, x, y, shape, color, unit):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.unit = unit
        self.active = True
        
    def render(self):
        if self.unit == "defender-weapon":
            Sprite.pen.shapesize(0.2, 0.2, 0)
        else:
            Sprite.pen.shapesize(1, 1, 0)
            
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # Border checks
        if self.unit == "defender-weapon" and self.x > 600:
                self.x = -1000
                self.active = False
                
        if self.unit == "attacker":
            if self.y > 300 or self.y < -300:
                self.dy *= -1
        
    def is_collision(self, other, tolerance):
        d = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        if d < tolerance:
            return True
        else:
            return False

sprites = []

defenders = []
defender_weapons = []

attackers = []
attacker_weapons = []

# Defenders
for _ in range(10):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    defenders.append(Sprite(x, y, "circle", "blue", "defender"))

# Attackers
for _ in range(100):
    x = random.randint(300, 500)
    y = random.randint(-300, 300)
    attackers.append(Sprite(x, y, "circle", "red", "attacker"))
    attackers[-1].heading = 180 # left
    attackers[-1].dx = -2.8
    attackers[-1].dy = random.randint(-20, 20) / 20.0

# Weapons
for _ in range(50):
    x = -1000
    y = - 1000
    defender_weapons.append(Sprite(x, y, "circle", "lightblue", "defender-weapon"))
    defender_weapons[-1].active = False
    defender_weapons[-1].dy = random.randint(-10, 10) / 20.0
    
# Main game loop
while True:
    # Assign weapon to sprite
    for defender in defenders:
        for weapon in defender_weapons:
            if weapon.active == False and random.randint(0, 100) > 95:
                weapon.x = defender.x
                weapon.y = defender.y
                weapon.dx = 10
                weapon.active = True
                break
    
    # Check for collisions between enemy and weapons
    for weapon in defender_weapons:
        if weapon.active == True:
            for attacker in attackers:
                if attacker.is_collision(weapon, 12):
                    attacker.x += 1200
                    attacker.y = random.randint(-300, 300)
                    weapon.x = -1000
                    weapon.active = False
                    weapon.dx = 0
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
    
    # Clear screen
    Sprite.pen.clear()

