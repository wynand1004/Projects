# Slime Volleyball
import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Slime Volleyball")
wn.tracer(0)

player = turtle.Turtle()
player.shape("circle")
player.color("yellow")
player.shapesize(3.0, 3.0, 0)
player.speed(0)
player.penup()
player.dx = 0


ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(1.0, 1.0, 0)
ball.speed(0)
ball.penup()
ball.dx = 0
ball.dy = 0

GRAVITY = -0.1

player.goto(0, -200)
ball.goto(0,0)

while True:
    # Gravity
    ball.dy += GRAVITY
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    
    # Check for collision
    if ball.distance(player) < 40:

        # Calculate angle
        angle = math.atan2(ball.ycor()-player.ycor(), ball.xcor()-player.xcor()) * 57.1
        
        # Move the ball back to before collision
        ball.sety(ball.ycor() - ball.dy)
        ball.setx(ball.xcor() - ball.dx)
        
        # Update the dx and dy
        ball.dx *= -math.cos(angle)
        ball.dy *= -math.sin(angle) 
        
        print(angle, ball.dx, ball.dy)

    wn.update()
    
wn.mainloop()
