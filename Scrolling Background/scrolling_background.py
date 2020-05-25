# How to Make a Scrolling Background
# By TokyoEdTech
# https://www.christianthompson.com

import turtle

wn = turtle.Screen()
wn.title("How to Make a Scrolling Background")
wn.bgcolor("blue")
wn.setup(height=320, width=800)
wn.tracer(0)

wn.register_shape("background.gif")

# Draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("white")
pen.penup()

def left():
    global camera_dx
    camera_dx = 3
    
def right():
    global camera_dx
    camera_dx = -3

camera_x = 0
camera_dx = 0
    
wn.listen()
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
    
    camera_x += camera_dx
    pen.setx(camera_x)
    camera_x %= 800

    pen.goto(camera_x, 0)
    pen.shape("background.gif")
    pen.stamp()

    pen.goto(camera_x - 800, 0)
    pen.stamp()
    
    pen.goto(camera_x + 800, 0)
    pen.stamp()
    
    wn.update()
    
    pen.clear()
