# Basic Animation in Python 3
# Part 3: Using the ontimer Method
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
	if player.shape() == "square":
		player.shape("circle")
	elif player.shape() == "circle":
		player.shape("square")
	
	# Set timer
	wn.ontimer(player_animate, 500)

player_animate()

while True:
	wn.update()
	print("Main Loop")
	
wn.mainloop()