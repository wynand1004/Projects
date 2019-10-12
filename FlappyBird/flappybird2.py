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
wn.bgpic("background.gif")
wn.setup(width=500, height=800)
wn.tracer(0)

# Register Shapes
wn.register_shape("bird.gif")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 250)
pen.write("0", move=False, align="left", font=("Arial", 32, "normal"))

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("bird.gif")
player.goto(-200, 0)
player.dx = 0
player.dy = 1

pipe1_top = turtle.Turtle()
pipe1_top.speed(0)
pipe1_top.penup()
pipe1_top.color("green")
pipe1_top.shape("square")
pipe1_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_top.goto(300, 250)
pipe1_top.dx = -2
pipe1_top.dy = 0
pipe1_top.value = 1

pipe1_bottom = turtle.Turtle()
pipe1_bottom.speed(0)
pipe1_bottom.penup()
pipe1_bottom.color("green")
pipe1_bottom.shape("square")
pipe1_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe1_bottom.goto(300, -250)
pipe1_bottom.dx = -2
pipe1_bottom.dy = 0

pipe2_top = turtle.Turtle()
pipe2_top.speed(0)
pipe2_top.penup()
pipe2_top.color("green")
pipe2_top.shape("square")
pipe2_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_top.goto(600, 280)
pipe2_top.dx = -2
pipe2_top.dy = 0
pipe2_top.value = 1

pipe2_bottom = turtle.Turtle()
pipe2_bottom.speed(0)
pipe2_bottom.penup()
pipe2_bottom.color("green")
pipe2_bottom.shape("square")
pipe2_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe2_bottom.goto(600, -220)
pipe2_bottom.dx = -2
pipe2_bottom.dy = 0

pipe3_top = turtle.Turtle()
pipe3_top.speed(0)
pipe3_top.penup()
pipe3_top.color("green")
pipe3_top.shape("square")
pipe3_top.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_top.goto(900, 320)
pipe3_top.dx = -2
pipe3_top.dy = 0
pipe3_top.value = 1

pipe3_bottom = turtle.Turtle()
pipe3_bottom.speed(0)
pipe3_bottom.penup()
pipe3_bottom.color("green")
pipe3_bottom.shape("square")
pipe3_bottom.shapesize(stretch_wid=18, stretch_len=3, outline=None)
pipe3_bottom.goto(900, -180)
pipe3_bottom.dx = -2
pipe3_bottom.dy = 0

gravity = -0.3

# Define function / method
def go_up():
    player.dy += 8
    
    if player.dy > 8:
        player.dy = 8

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "space")


# Initialize game variables
player.score = 0

pipes = [(pipe1_top, pipe1_bottom), (pipe2_top, pipe2_bottom), (pipe3_top, pipe3_bottom)]

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
    
    # Bottom Border
    if player.ycor() < -390:
        player.dy = 0
        player.sety(-390)


    # Iterate through pipes
    for pipe_pair in pipes:
        pipe_top = pipe_pair[0]
        pipe_bottom = pipe_pair[1]
        
        # Move Pipe 1
        x = pipe_top.xcor()
        x += pipe_top.dx
        pipe_top.setx(x) 
        
        x = pipe_bottom.xcor()
        x += pipe_bottom.dx
        pipe_bottom.setx(x)
        
        # Return pipes to start
        if pipe_top.xcor() < -350:
            pipe_top.setx(600)
            pipe_bottom.setx(600)
            pipe_top.value = 1

        # Check for collisions with pipes
        # Pipe 1
        if (player.xcor() + 10 > pipe_top.xcor() - 30) and (player.xcor() - 10 < pipe_top.xcor() + 30):
            if (player.ycor() + 10 > pipe_top.ycor() - 180) or (player.ycor() - 10 < pipe_bottom.ycor() + 180):
                pen.clear()
                pen.write("Game Over", move=False, align="center", font=("Arial", 16, "normal"))
                wn.update()
                time.sleep(3)
                # Reset score
                player.score = 0
                # Move Pipes Back
                pipe_top.setx(450)
                pipe_bottom.setx(450)
                # Move Player back
                player.goto(-200, 0)
                player.dy = 0
                # Reset the pen
                pen.clear()
                pen.write("0", move=False, align="center", font=("Arial", 16, "normal"))
                
        # Check for score        
        if pipe_top.xcor() + 30 < player.xcor() - 10:
            player.score += pipe_top.value
            pipe_top.value = 0
            pen.clear()
            pen.write(player.score, move=False, align="center", font=("Arial", 32, "normal"))


wn.mainloop()

