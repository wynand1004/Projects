# How to Create a Game Timer
# By TokyoEdTech
# https://www.christianthompson.com

import turtle
import time

wn = turtle.Screen()
wn.title("Game Timer Demo")
wn.bgcolor("black")

bob = turtle.Turtle()
bob.speed(0)
bob.color("yellow")
bob.shape("triangle")
bob.penup()

is_paused = False

def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True
        
wn.listen()
wn.onkeypress(toggle_pause, "p")

time_limit = 5
start_time = time.time()

while True:
    if not is_paused:
        bob.fd(1)
        bob.lt(1)
        
        # Timer
        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            print("GAME OVER")
            exit()
    else:
        start_time = time.time() - elapsed_time
        wn.update()
