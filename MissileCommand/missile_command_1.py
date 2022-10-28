# Missile Command Clone by /u/wynand1004 AKA @TokyoEdTech
# Requires SPGL Version 0.8 or Above
# SPGL Documentation on Github: https://wynand1004.github.io/SPGL

# Import SPGL
import spgl

# Create Classes
class City(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

class Silo(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

class PlayerMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

class EnemyMissile(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)

# Create Functions

# Initial Game setup
game = spgl.Game(800, 600, "black", "Missile Command by /u/wynand1004 AKA @TokyoEdTech", 0)

# Create Sprites
city = City("square", "green", -100, -250)

silo = Silo("square", "blue", 0, -200)

player_missile = PlayerMissile("circle", "white", 0, -250)

enemy_missile = EnemyMissile("circle", "red", 0, 250)

# Create Labels

# Create Buttons

# Set Keyboard Bindings

while True:
    # Call the game tick method
    game.tick()
