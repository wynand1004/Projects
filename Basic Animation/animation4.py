# Basic Animation in Python 3
# Part 4: Using Images
# by Christian Thompson AKA @TokyoEdTech
import turtle
import time

wn = turtle.Screen()
wn.title("Animation Demo")
wn.bgcolor("black")

# Register shapes
wn.register_shape("invader.gif")
wn.register_shape("invader2.gif")

player = turtle.Turtle()
player.shape("invader.gif")
player.color("green")
player.frame = 0

def player_animate():
	if player.frame == 0:
		player.shape("invader2.gif")
		player.frame = 1
	elif player.frame == 1:
		player.shape("invader.gif")
		player.frame = 0
	
	# Set timer
	wn.ontimer(player_animate, 500)

player_animate()

while True:
	wn.update()
	print("Main Loop")

wn.mainloop()