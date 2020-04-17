# Basic Animation in Python 3
# Part 2: Using Functions
# by Christian Thompson AKA @TokyoEdTech
import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.color("green")

def player_animate():
	player.shape("square")
	time.sleep(0.5)
	player.shape("circle")
	time.sleep(0.5)
	

while True:
	print("Main Loop")
	player_animate()
	
wn.mainloop()