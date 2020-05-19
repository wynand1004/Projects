# How to Create a Pause Function
# By TokyoEdTech
# https://www.christianthompson.com

import turtle

wn = turtle.Screen()
wn.title("Game Pause Demo")
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

while True:
    if not is_paused:
        bob.fd(1)
        bob.lt(1)
    else:
        wn.update()
