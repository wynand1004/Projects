# Falling Skies in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os
import random
import time

# Set up the screen
wn = turtle.Screen()
wn.title("Falling Down by @TokyoEdTech")
wn.bgcolor("black")
wn.bgpic("background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("deer_left.gif")
wn.register_shape("deer_right.gif")
wn.register_shape("hunter.gif")
wn.register_shape("nut.gif")

# Score
score = 0

# Health
lives = 3

# Player
player = turtle.Turtle()
player.speed(0)
player.shape("deer_left.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"

# Good things
good_things = []

for _ in range(20):
    good_thing = turtle.Turtle()
    good_thing.speed(0)
    good_thing.shape("nut.gif")
    good_thing.color("green")
    good_thing.penup()
    good_thing.goto(-100, 250)
    good_thing.speed = random.randint(2, 5)

    good_things.append(good_thing)

# Bad things
bad_things = []

for _ in range(20):
    bad_thing = turtle.Turtle()
    bad_thing.speed(0)
    bad_thing.shape("hunter.gif")
    bad_thing.color("red")
    bad_thing.penup()
    bad_thing.goto(100, 250)
    bad_thing.speed = random.randint(2, 5)

    bad_things.append(bad_thing)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))

# Functions
def go_left():
    player.direction = "left"
    player.shape("deer_left.gif")
    
def go_right():
    player.direction = "right"
    player.shape("deer_right.gif")

    
# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()
    
    # Move the player
    if player.direction == "left":
        player.setx(player.xcor() - 3)
    
    if player.direction == "right":
        player.setx(player.xcor() + 3)
        
    # Check for border collisions
    if player.xcor() < -390:
        player.setx(-390)
        
    elif player.xcor() > 390:
        player.setx(390)
        
    for good_thing in good_things:
        # Move the good things
        good_thing.sety(good_thing.ycor() - good_thing.speed)
    
        # Check if good things are off the screen
        if good_thing.ycor() < -300:
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))

        # Check for collisions
        if player.distance(good_thing) < 40:
            # Score increases
            score += 10
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        
            # Move the good thing back to the top
            good_thing.goto(random.randint(-300, 300), random.randint(400, 800))



    for bad_thing in bad_things:    
        # Move the bad things
        bad_thing.sety(bad_thing.ycor() - bad_thing.speed)
    
        if bad_thing.ycor() < -300:
            bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))
    
        
        if player.distance(bad_thing) < 40:
            # Score increases
            score -= 10
            lives -= 1
        
            # Show the score
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
            
            time.sleep(1)
            # Move the bad things back to the top
            for bad_thing in bad_things:
                bad_thing.goto(random.randint(-300, 300), random.randint(400, 800))
        
        
    # Check for game over
    if lives == 0:
        pen.clear()
        pen.write("Game Over! Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        wn.update()
        time.sleep(5)
        score = 0
        lives = 3
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
        
        
        
        
        
        
        
