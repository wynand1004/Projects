# How to Make a Scrolling Background
# By TokyoEdTech
# https://www.christianthompson.com

import turtle

wn = turtle.Screen()
wn.title("How to Make a Scrolling Background")
wn.bgcolor("blue")
wn.setup(height=320, width=800)
wn.tracer(0)

# Draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

player = turtle.Turtle()
player.speed(0)
player.shape("turtle")
player.color("yellow")
player.shapesize(2, 2)
player.setheading(0)
player.penup()
player.goto(0,-120)

def left():
    player.setheading(180)
    
def right():
    player.setheading(0)
    
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
    
    wn.update()
    
    

    
    
    
