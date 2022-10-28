# Missile Command Clone by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Part 5: Player and Enemy missile explosion

# Import SPGL
import spgl
import math

# Create Classes
class MissileCommand(spgl.Game):
    def __init__(self, screen_width, screen_height, background_color, title, splash_time):
       spgl.Game.__init__(self, screen_width, screen_height, background_color, title, splash_time)

    def click(self, x, y):
        player_missile.set_target(x, y)

class City(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

    def tick(self):
        pass

class Silo(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

    def tick(self):
        pass

class PlayerMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 5
        self.state = "ready"
        self.target_x = 0
        self.target_y = 0
        self.shapesize(0.2, 0.2, 0)
        self.frame = 0.0

    def set_target(self, target_x, target_y):
        if self.state == "ready":
            self.target_x = target_x
            self.target_y = target_y
            
            self.dx = self.xcor() - self.target_x
            self.dy = self.ycor() - self.target_y
            self.m = self.dy/self.dx     
            
            self.state = "launched"

    def explode(self):
        self.frame += 1.0
        if self.frame < 30.0:
            self.shapesize((self.frame / 10), (self.frame / 10), 0)
        elif self.frame < 55.0:
            self.shapesize((60 - self.frame)/10, (60 - self.frame)/10, 0)
        else:
            self.clear()
            self.penup()
            self.goto(2000, 2000)
            self.state = None

    def tick(self):
        if self.state == "launched":
            self.pendown()
            self.setx(self.xcor() + (1 / self.m) * self.speed)
            self.sety(self.ycor() + self.speed)

            # Check for reaching target
            a=self.xcor()-self.target_x
            b=self.ycor()-self.target_y
            distance = math.sqrt((a**2) + (b**2))

            if distance < 5:
                self.state = "explode"

        if self.state == "explode":
            self.explode()

class EnemyMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.dx = 0
        self.dy = 0
        self.speed = 2
        self.shapesize(0.2, 0.2, 0)
        self.pendown()
        self.state = "ready"
        self.target_x = 0
        self.target_y = 0
        self.frame = 2

    def set_target(self, target):
        self.target_x = target.xcor()
        self.target_y = target.ycor()

        self.dx = self.xcor() - target.xcor()
        self.dy = self.ycor() - target.ycor()
        self.m = self.dy/self.dx

    def explode(self):
        self.frame += 1.0
        if self.frame < 30.0:
            self.shapesize((self.frame / 10), (self.frame / 10), 0)
        elif self.frame < 55.0:
            self.shapesize((60 - self.frame)/10, (60 - self.frame)/10, 0)
        else:
            self.clear()
            self.penup()
            self.goto(2000, 2000)
            self.state = None

    def tick(self):
        if self.state == "launched":
            self.setx(self.xcor() - (1 / self.m) * self.speed)
            self.sety(self.ycor() - self.speed)

            # Check for reaching target
            a=self.xcor()-self.target_x
            b=self.ycor()-self.target_y
            distance = math.sqrt((a**2) + (b**2))

            if distance < 5:
                self.state = "explode"

        if self.state == "explode":
            self.explode()

# Create Functions

# Initial Game setup
game = MissileCommand(800, 600, "black", "Missile Command by /u/wynand1004 AKA @TokyoEdTech", 0)

# Create Sprites
city = City("square", "green", -200, -250)

silo = Silo("square", "blue", 0, -200)

player_missile = PlayerMissile("circle", "white", 0, -250)
#player_missile.set_target(300, 300)

enemy_missile = EnemyMissile("circle", "red", 0, 250)
enemy_missile.set_target(city)
enemy_missile.state = "launched"

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()


