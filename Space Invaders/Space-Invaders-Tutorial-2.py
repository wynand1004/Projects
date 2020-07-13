#Space Invaders - Part 2
#Move the Player
#Python 2.7 on Mac
import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
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

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")






delay = raw_input("Press enter to finsh.")