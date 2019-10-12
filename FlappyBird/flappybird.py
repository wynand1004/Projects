# http://christianthompson.com
# Twitter: @tokyoedtech

# Welcome to my live coding / Q&A Session for October 12, 2019.
# If you have any Python questions - ask in chat
# Please provide any code via pastebin.com link

# OS: Ubuntu Linux 19.04
# Programming Editor: Geany

# Live coding October 12, 2019 (Typhoon Hagibis Edition)
# Flappy Bird Using Python 3 and the Turtle Module

import turtle
import time

wn = turtle.Screen()
wn.title("Flappy Bird by @TokyoEdTech")
wn.bgcolor("blue")
wn.setup(width=500, height=800)
wn.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.shapesize(stretch_wid=3, stretch_len=3, outline=None)
player.goto(-200, 0)
player.dx = 0
player.dy = 1

pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(0, 250)
pipe1_top.dx = -2
pipe1_top.dy = 0

pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(0, -250)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0

gravity = -0.2

# Define function / method
def go_up():
    player.dy += 9

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "space")

# Main Game Loop
while True:
    # Pause
    time.sleep(0.02)
    # Update the screen
    wn.update()
    
    # Add gravity
    player.dy += gravity
    
    # Move player
    y = player.ycor()
    y += player.dy
    player.sety(y)

    # Move the pipes
    x = pipe1_top.xcor()
    x += pipe1_top.dx
    pipe1_top.setx(x) 
    
    x = pipe1_bottom.xcor()
    x += pipe1_bottom.dx
    pipe1_bottom.setx(x) 


wn.mainloop()
