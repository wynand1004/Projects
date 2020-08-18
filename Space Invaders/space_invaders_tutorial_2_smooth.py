# Space Invaders - Part 2 Smooth Motion Update
# Move the Player
# Python 3.8 on Mac
import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 0

# Move the player left and right
def move_left():
	global playerspeed
	playerspeed = -3
	
def move_right():
	global playerspeed
	playerspeed = 3

def stop_player():
	global playerspeed
	playerspeed = 0

# Create keyboard bindings
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# wn.onkeyrelease(stop_player, "Left")
# wn.onkeyrelease(stop_player, "Right")


while True:
	
	# Move the player
	player.setx(player.xcor() + playerspeed)

	# Check borders
	if player.xcor() > 285:
		player.setx(285)
		playerspeed = 0

	elif player.xcor() < -285:
		player.setx(-285)
		playerspeed = 0	
	



wn.mainloop()
