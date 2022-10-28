# Missile Command Clone by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL
# Part 3: Move the player missile toward the targeted location

# Import SPGL
import spgl

# Create Classes
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
        self.speed = 3

    def set_target(self, target_x, target_y):
        self.dx = self.xcor() - target_x
        self.dy = self.ycor() - target_y
        self.m = self.dy/self.dx     

    def tick(self):
        self.setx(self.xcor() + (1 / self.m) * self.speed)
        self.sety(self.ycor() + self.speed)

class EnemyMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.dx = 0
        self.dy = 0
        self.speed = 2

    def set_target(self, target):
        self.dx = self.xcor() - target.xcor()
        self.dy = self.ycor() - target.ycor()
        self.m = self.dy/self.dx
        print(self.dx, self.dy, self.m)

    def tick(self):
        self.setx(self.xcor() - (1 / self.m) * self.speed)
        self.sety(self.ycor() - self.speed)



# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Missile Command by /u/wynand1004 AKA @TokyoEdTech", 0)

# Create Sprites
city = City("square", "green", -200, -250)

silo = Silo("square", "blue", 0, -200)

player_missile = PlayerMissile("circle", "white", 0, -250)
player_missile.set_target(300, 300)

enemy_missile = EnemyMissile("circle", "red", 0, 250)
enemy_missile.set_target(city)

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()
