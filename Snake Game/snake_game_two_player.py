# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

# Live Coding Update: Add Multiple Snakes (2-Player Mode)

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(-100,0)
head.direction = "stop"

# Snake head 2
head2 = turtle.Turtle()
head2.speed(0)
head2.shape("square")
head2.color("blue")
head2.penup()
head2.goto(100,0)
head2.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []
segments2 = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up2():
    if head2.direction != "down":
        head2.direction = "up"

def go_down2():
    if head2.direction != "up":
        head2.direction = "down"

def go_left2():
    if head2.direction != "right":
        head2.direction = "left"

def go_right2():
    if head2.direction != "left":
        head2.direction = "right"

def move2():
    if head2.direction == "up":
        y = head2.ycor()
        head2.sety(y + 20)

    if head2.direction == "down":
        y = head2.ycor()
        head2.sety(y - 20)

    if head2.direction == "left":
        x = head2.xcor()
        head2.setx(x - 20)

    if head2.direction == "right":
        x = head2.xcor()
        head2.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

wn.onkeypress(go_up2, "i")
wn.onkeypress(go_down2, "k")
wn.onkeypress(go_left2, "j")
wn.onkeypress(go_right2, "l")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(-100,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Check for a collision with the border
    if head2.xcor()>290 or head2.xcor()<-290 or head2.ycor()>290 or head2.ycor()<-290:
        time.sleep(1)
        head2.goto(100,0)
        head2.direction = "stop"

        # Hide the segments
        for segment2 in segments2:
            segment2.goto(1000, 1000)
        
        # Clear the segments list
        segments2.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Check for a collision with the food
    if head2.distance(food) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments2.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
   # Move the end segments first in reverse order
    for index in range(len(segments2)-1, 0, -1):
        x = segments2[index-1].xcor()
        y = segments2[index-1].ycor()
        segments2[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    # Move segment 0 to where the head is
    if len(segments2) > 0:
        x = head2.xcor()
        y = head2.ycor()
        segments2[0].goto(x,y)

    move()    
    move2()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(-100,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for head collision with the body segments
    for segment2 in segments2:
        if segment2.distance(head) < 20:
            time.sleep(1)
            head2.goto(100,0)
            head2.direction = "stop"
        
            # Hide the segments
            for segment2 in segments2:
                segment2.goto(1000, 1000)
        
            # Clear the segments list
            segments2.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
