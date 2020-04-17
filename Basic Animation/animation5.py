# Basic Animation in Python 3
# Part 5: Using Lists
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
player.frames = ["invader.gif", "invader2.gif"]

def player_animate():
	player.frame += 1
	if player.frame >= len(player.frames):
		player.frame = 0
	player.shape(player.frames[player.frame])
	# Set timer
	wn.ontimer(player_animate, 500)

player_animate()

while True:
	wn.update()
	print("Main Loop")

wn.mainloop()