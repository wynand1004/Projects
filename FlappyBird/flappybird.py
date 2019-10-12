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

wn = turtle.Screen()
wn.title("Flappy Bird by @TokyoEdTech")
wn.bgcolor("blue")
wn.setup(width=500, height=800)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color("yellow")
player.shape("turtle")
player.shapesize(stretch_wid=3, stretch_len=3, outline=None)
player.goto(-200, 0)
player.dx = 0
player.dy = 1



# Main Game Loop
while True:
    # Move player
    y = player.ycor()
    y += player.dy
    player.sety(y)

    


wn.mainloop()
