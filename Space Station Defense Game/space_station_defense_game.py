# https://christianthompson.com
# Twitter: @tokyoedtech

# Welcome to my live coding stream for October 21, 2019.
# If you have any Python questions - ask in chat
# Please provide any code via pastebin.com link

# OS: Ubuntu Linux 19.04
# Programming Editor: Geany

# Live coding October 21, 2019 
# Space Station Defense Game Using Python 3 and the Turtle Module

import turtle
import math

wn = turtle.Screen()
wn.title("Space Station Defense Game by @TokyoEdTech")
wn.bgcolor("black")
# Stop screen updates
wn.tracer(0)

# Register Shapes
player_vertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
wn.register_shape("player", player_vertices)

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        
player = Sprite()
player.color("white")
player.shape("player")
player.speed(0)

def rotate_left():
    player.lt(30)
    
def rotate_right():
    player.rt(30)

# Keyboard binding
wn.listen()
wn.onkey(rotate_left, "Left")
wn.onkey(rotate_right, "Right")

# Start main game loop
while True:
    # Do screen update
    wn.update()
    player.goto(0, 0)


wn.mainloop()
