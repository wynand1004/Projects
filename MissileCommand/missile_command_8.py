# Missile Command Clone by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Part 8: Player Missile Count / Scoring

# Import SPGL
import spgl
import math
import random

# Create Classes
class MissileCommand(spgl.Game):
    def __init__(self, screen_width, screen_height, background_coor, title, splash_time):
       spgl.Game.__init__(self, screen_width, screen_height, background_coor, title, splash_time)
       self.level = 1

    def click(self, x, y):
        # Find the closest missile
        closest_missile = None
        closest_missile_distance = 10000
        for player_missile in player_missiles:
            if player_missile.state == "ready":               
                a=player_missile.xcor()-x
                b=player_missile.ycor()-y
                distance = math.sqrt((a**2) + (b**2))
                if distance < closest_missile_distance:
                    closest_missile = player_missile
                    closest_missile_distance = distance
        if closest_missile:
            closest_missile.set_target(x, y)

class City(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

    def destroy(self):
        self.clear()
        self.penup()
        self.goto(0, 2000)
        self.state = None 

    def tick(self):
        pass

class Silo(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

    def destroy(self):
        self.clear()
        self.penup()
        self.goto(0, 2000)
        self.state = None 
        silos.remove(self)

    def tick(self):
        pass

class PlayerMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 5
        self.state = "ready"
        self.target_x = 0
        self.target_y = 0
        self.size = 0.2
        self.shapesize(self.size, self.size, 0)
        self.frame = 0.0
        

    def set_target(self, target_x, target_y):
        if self.state == "ready":
            self.target_x = target_x
            self.target_y = target_y
            
            self.dx = self.xcor() - self.target_x
            # Avoid divide by 0 error
            if self.dx == 0:  
                self.dx = 0.01
            self.dy = self.ycor() - self.target_y
            self.m = self.dy/self.dx     
            
            self.state = "launched"

    def explode(self):
        self.frame += 1.0
        if self.frame < 30.0:
            self.size = self.frame / 10
            self.shapesize(self.size, self.size, 0)
        elif self.frame < 55.0:
            self.size = (60 - self.frame)/10
            self.shapesize(self.size, self.size, 0)
        else:
            self.destroy()

    def tick(self):
        if self.state == "launched":
            self.pendown()
            self.setx(self.xcor() + (1 / self.m) * self.speed)
            self.sety(self.ycor() + self.speed)

            # Check for reaching target
            a=self.xcor()-self.target_x
            b=self.ycor()-self.target_y
            distance = math.sqrt((a**2) + (b**2))

            if distance < 10:
                self.state = "explode"

            # Border Checking
            if (self.xcor()< -420) or (self.xcor() > 420):
                self.state = "explode"

        if self.state == "explode":
            self.explode()

    def destroy(self):
        self.clear()
        self.penup()
        self.goto(0, 2000)
        self.state = None 
        player_missiles.remove(self)  

class EnemyMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.dx = 0
        self.dy = 0
        self.speed = 2
        self.size = 0.2
        self.shapesize(self.size, self.size, 0)
        self.pendown()
        self.state = "ready"
        self.target_x = 0
        self.target_y = 0
        self.frame = 2

    def set_target(self, target):
        self.target_x = target.xcor()
        self.target_y = target.ycor()

        self.dx = self.xcor() - target.xcor()
        # Avoid divide by 0 error
        if self.dx == 0:  
            self.dx = 0.01
        self.dy = self.ycor() - target.ycor()
        self.m = self.dy/self.dx

        self.state = "launched"

    def explode(self):
        self.frame += 1.0
        if self.frame < 30.0:
            self.size = self.frame / 10
            self.shapesize(self.size, self.size, 0)
        elif self.frame < 55.0:
            self.size = (60 - self.frame)/10
            self.shapesize(self.size, self.size, 0)
        else:
            self.destroy()

    def destroy(self):
        self.clear()
        self.penup()
        self.goto(2000, 2000)
        self.state = None    
        enemy_missiles.remove(self)    

    def tick(self):
        if self.state == "launched":
            self.setx(self.xcor() - (1 / self.m) * self.speed)
            self.sety(self.ycor() - self.speed)

            # Check for reaching target
            a=self.xcor()-self.target_x
            b=self.ycor()-self.target_y
            distance = math.sqrt((a**2) + (b**2))

            if distance < 10:
                self.state = "explode"

        if self.state == "explode":
            self.explode()

# Create Functions

# Initial Game setup
game = MissileCommand(800, 600, "black", "Missile Command by /u/wynand1004 AKA @TokyoEdTech", 0)
game.score = 0

# Create Sprites
cities = []
silos = []
player_missiles = []
enemy_missiles = []

for i in range(6):
    cities.append(City("square", "green", -250 + (i * 100), -250))

for i in range(3):
    silos.append(Silo("square", "blue", -350 + (i * 350), -225))

for i in range(30):
    if i <10:
        x = -350
    elif i < 20:
        x = 0
    else:
        x = 350

    player_missiles.append(PlayerMissile("circle", "white", x, -225))

for i in range(30):
    enemy_missiles.append(EnemyMissile("circle", "red", random.randint(-450, 450), random.randint(400, 800)))

for enemy_missile in enemy_missiles:
    if random.randint(0, 10) > 5:
        enemy_missile.set_target(random.choice(cities + silos))

# Create Labels
status_label = spgl.Label("Score: {}  Cities: {}  Silos: {}  Missiles: {}", "white", -300, 280)

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()

    # Check to see if the player missile collides with the enemy missiles
    for player_missile in player_missiles:
        for enemy_missile in enemy_missiles:
            # Check if the player missile is exploding
            if player_missile.state == "explode":
                radius = (player_missile.size * 20) / 2
                a=player_missile.xcor()-enemy_missile.xcor()
                b=player_missile.ycor()-enemy_missile.ycor()
                distance = math.sqrt((a**2) + (b**2))
                if distance < radius:
                    enemy_missile.destroy()  
                    game.score += 10         

    # Check to see if the enemy missile collides with the player cities or silos (destroy the missiles there as well)
    for enemy_missile in enemy_missiles:
        for city in cities:
            if enemy_missile.state == "explode":
                radius = (enemy_missile.size * 20) / 2
                a=enemy_missile.xcor()-city.xcor()
                b=enemy_missile.ycor()-city.ycor()
                distance = math.sqrt((a**2) + (b**2))
                if distance < radius:
                    city.destroy()    
                    cities.remove(city)   

        for silo in silos:
            if enemy_missile.state == "explode":
                radius = (enemy_missile.size * 20) / 2
                a=enemy_missile.xcor()-silo.xcor()
                b=enemy_missile.ycor()-silo.ycor()
                distance = math.sqrt((a**2) + (b**2))
                if distance < radius:
                    silo.destroy()

                for player_missile in player_missiles:
                    a=enemy_missile.xcor()-player_missile.xcor()
                    b=enemy_missile.ycor()-player_missile.ycor()
                    distance = math.sqrt((a**2) + (b**2))
                    if distance < radius:
                        player_missile.destroy()



    # Update status label
    status_label.update("Score: {}  Cities: {}  Silos: {}  Missiles: {}".format(game.score, len(cities), len(silos), len(player_missiles)))                     