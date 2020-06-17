# Game State Demo (Splash Screen, Game, End Screen)
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/

# Import modules
import turtle
# import math
# import random
# import time

# Create classes


# Create functions
def start_game():
    global game_state
    game_state = "game"
    
    # RESET THE GAME
    # Set score to 0
    # Move the player back to the starting position


# Define constants
SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600


# Game Setup
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Game State Demo by TokyoEdTech")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

# Keyboard Bindings
wn.listen()
wn.onkeypress(start_game, "s")

game_state = "gameover"

# Main Game Loop
while True:
        
    # Clear the screen
    pen.clear()
    
    # Game code here
    if game_state == "splash":
        wn.bgpic("splash.gif")
        
    elif game_state == "game":
        wn.bgpic("main.gif")
        
    elif game_state == "gameover":
        wn.bgpic("game_over.gif")

    # Update the screen
    wn.update()

