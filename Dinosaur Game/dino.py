# How to Make a Dinosaur Game
# By TokyoEdTech
# https://www.christianthompson.com

import turtle
import random
import time

wn = turtle.Screen()
wn.title("Dinosaur Game by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(height=320, width=800)
wn.bgpic("background.gif")
wn.tracer(0)

wn.register_shape("dinosaur.gif")
wn.register_shape("cactus_small.gif")

LINE_HEIGHT = -40

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("white")
pen.penup()

# Draw line
pen.goto(-400, LINE_HEIGHT)
pen.pendown()
pen.goto(400, LINE_HEIGHT)
pen.penup()

jumper = turtle.Turtle()
jumper.speed(0)
jumper.shape("dinosaur.gif")
jumper.color("green")
jumper.penup()
jumper.dy = 0
jumper.dx = 0
jumper.state = "ready"
jumper.height = 50
jumper.width = 40
jumper.goto(-200, LINE_HEIGHT + jumper.height/2)

gravity = -0.8

obstacle = turtle.Turtle()
obstacle.speed(0)
obstacle.shape("cactus_small.gif")
obstacle.color("red")
obstacle.penup()
obstacle.dx = -3
obstacle.height = 30
obstacle.width = 17
obstacle.goto(200, LINE_HEIGHT + obstacle.height/2)

def jump():
    if jumper.state == "ready":
        jumper.dy = 12
        jumper.state = "jumping"
    
wn.listen()
wn.onkeypress(jump, "space")

while True:
    # Check for landing
    if jumper.ycor() < LINE_HEIGHT + jumper.height/2:
        jumper.sety(LINE_HEIGHT + jumper.height/2)
        jumper.dy = 0
        jumper.state = "ready"

    if jumper.ycor() != LINE_HEIGHT + jumper.height/2 and jumper.state == "jumping":
        # Gravity (Affects dy)
        jumper.dy += gravity
    
    # Add dy to y
    y = jumper.ycor()
    y += jumper.dy
    jumper.sety(y)
    
    # Move the obstacle
    x = obstacle.xcor()
    x += obstacle.dx
    obstacle.setx(x)
    
    # Check for off the screen
    if obstacle.xcor() < -400:
        x = random.randint(400, 600)
        obstacle.setx(x)
        obstacle.dx *= 1.05
        print(obstacle.dx)
    
    # Check for collision
    obstacle_left = obstacle.xcor() - obstacle.width/2
    obstacle_right = obstacle.xcor() + obstacle.width/2
    obstacle_top = obstacle.ycor() + obstacle.height/2
    
    jumper_left = jumper.xcor() - jumper.width/2
    jumper_right = jumper.xcor() + jumper.width/2
    jumper_bottom = jumper.ycor() - jumper.height/2
    
    # 3 Conditions
    if(obstacle_left > jumper_left and obstacle_left < jumper_right and obstacle_top > jumper_bottom):
        print("GAME OVER")
        time.sleep(3)
        obstacle.goto(450, LINE_HEIGHT + obstacle.height/2)
        obstacle.dx = -3
    
    if(obstacle_right > jumper_left and obstacle_right < jumper_right and obstacle_top > jumper_bottom):
        print("GAME OVER")
        obstacle.goto(450, LINE_HEIGHT + obstacle.height/2)
        obstacle.dx = -3
    
    wn.update()
