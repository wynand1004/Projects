# Basic Collision Detection
# by @TokyoEdtech

# Topics: Collision Detection, Overlapping Coordinates,
# Distance Checking, Axis-Aligned Bounding Box

# Shoutouts:
# 16-Bit Members Kevin, Paul, and Jan

import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Collision Detection by @TokyoEdtech")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

shapes = ["wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]

for shape in shapes:
    wn.register_shape(shape)
    
# Create Sprite Class
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
    
    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
            
    def is_distance_collision(self, other):
        distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False
        
    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
        
wizard = Sprite(-128, 200, 128, 128, "wizard.gif")
goblin = Sprite(128, 200, 108, 128, "goblin.gif")

pacman = Sprite(-128, 0, 128, 128, "pacman.gif")
cherry = Sprite(128, 0, 128, 128, "cherry.gif")

bar = Sprite(0, -400, 128, 24, "bar.gif")
ball = Sprite(0,-200, 32, 32, "ball.gif")

sprites = [wizard, goblin, pacman, cherry, bar, ball]

def move_goblin():
    goblin.x -= 64

def move_pacman():
    pacman.x += 30
    
def move_ball():
    ball.y -= 24

wn.listen()
wn.onkeypress(move_goblin, "Left")
wn.onkeypress(move_pacman, "Right")
wn.onkeypress(move_ball, "Down")

while True:
    
    for sprite in sprites:
        sprite.render(pen)
        
    # Collision detection
    if wizard.is_overlapping_collision(goblin):
        wizard.image = "x.gif"
        
    if pacman.is_overlapping_collision(cherry):
        cherry.image = "x.gif"
        
    if bar.is_overlapping_collision(ball):
        ball.image = "x.gif"
        
    wn.update()
    pen.clear()
