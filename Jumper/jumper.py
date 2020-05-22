# How to Make a Jumping Character
# By TokyoEdTech
# https://www.christianthompson.com

import turtle

wn = turtle.Screen()
wn.title("How to Make a Jumping Character")
wn.bgcolor("blue")
wn.setup(height=320, width=800)
wn.tracer(0)

GROUND_LEVEL = -40

# Draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("white")
pen.penup()

# Draw line
pen.goto(-400, GROUND_LEVEL)
pen.pendown()
pen.goto(400, GROUND_LEVEL)
pen.penup()

jumper = turtle.Turtle()
jumper.speed(0)
jumper.shape("square")
jumper.color("green")
jumper.penup()
jumper.width = 20
jumper.height = 20
jumper.dy = 0
jumper.dx = 0
jumper.state = "ready"
jumper.goto(-200, GROUND_LEVEL + jumper.height / 2)

GRAVITY = -0.8

def jump():
    if jumper.state == "ready":
        jumper.dy = 12
        jumper.state = "jumping"
    
wn.listen()
wn.onkeypress(jump, "space")

while True:
    
    # Gravity
    jumper.dy += GRAVITY
    
    # Move the jumper
    y = jumper.ycor()
    y += jumper.dy
    jumper.sety(y)
    
    # Deal with the ground
    if jumper.ycor() < GROUND_LEVEL + jumper.height / 2:
        jumper.sety(GROUND_LEVEL + jumper.height / 2)
        jumper.dy = 0
        jumper.state = "ready"
        
    wn.update()
