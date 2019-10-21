# https://christianthompson.com
# Twitter: @tokyoedtech

# Welcome to my live coding stream for October 21, 2019.
# If you have any Python questions - ask in chat
# Please provide any code via pastebin.com link

# OS: Ubuntu Linux 19.04
# Programming Editor: Geany

# Live coding October 21, 2019 
# Space Station Defense Game Using Python 3 and the Turtle Module

import turtle
import math
import random

wn = turtle.Screen()
wn.setup(width=800, height=800)
wn.title("Space Station Defense Game by @TokyoEdTech")
wn.bgcolor("black")
# Stop screen updates
wn.tracer(0)

# Register Shapes
player_vertices = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
wn.register_shape("player", player_vertices)

class Sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        # Maximum animation speed
        self.speed(0)
        self.penup()
        
        
def get_heading_to(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    heading = math.atan2(y1 - y2, x1 - x2)
    heading = heading * 180.0 / 3.14159
    
    return heading
    
player = Sprite()
player.color("white")
player.shape("player")
player.score = 0

missile = Sprite()
missile.color("red")
missile.shape("arrow")
missile.speed = 0.4
missile.state = "ready"
missile.hideturtle()

pen = Sprite()
pen.color("white")
pen.hideturtle()
pen.goto(0, 350)
pen.write("Score: 0", False, align = "center", font = ("Arial", 24, "normal"))

asteroids = []

for _ in range(5):   
    asteroid = Sprite()
    asteroid.color("brown")
    asteroid.shape("circle")
    asteroid.speed = random.randint(2, 10) / 100
    asteroid.goto(0, 0)
    heading = random.randint(0, 360)
    distance = random.randint(400, 600)
    asteroid.setheading(heading)
    asteroid.fd(distance)
    asteroid.setheading(get_heading_to(player, asteroid))
    asteroids.append(asteroid)
    
def rotate_left():
    player.lt(10)
    
def rotate_right():
    player.rt(10)
    
def fire_missile():
    if missile.state == "ready":
        missile.goto(0, 0)
        missile.showturtle()
        missile.setheading(player.heading())
        missile.state = "fire"

# Keyboard binding
wn.listen()
wn.onkey(rotate_left, "Left")
wn.onkey(rotate_right, "Right")
wn.onkey(fire_missile, "space")

# Start main game loop
while True:
    # Do screen update
    wn.update()
    player.goto(0, 0)
    
    # Move the missile
    if missile.state == "fire":
        missile.fd(missile.speed)
        
    # Border checking
    if missile.xcor() > 400 or missile.xcor() < -400 or missile.ycor() > 400 or missile.ycor() < -400:
        missile.hideturtle()
        missile.state = "ready"

    # Iterate through asteroids
    for asteroid in asteroids:    
        # Move the asteroid
        asteroid.fd(asteroid.speed)
        
        # Check for collisions
        # Asteroid and Missile
        if asteroid.distance(missile) < 20:
            # Reset Asteroid
            heading = random.randint(0, 360)
            distance = random.randint(800, 1000)
            asteroid.setheading(heading)
            asteroid.fd(distance)
            asteroid.setheading(get_heading_to(player, asteroid))
            asteroid.speed += 0.01
            
            # Reset Missile
            missile.goto(1000, 1000)
            missile.hideturtle()
            missile.state = "ready"
            
            # Increase score
            player.score += 10
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))

        # Asteroid and Player
        if asteroid.distance(player) < 20:
            # Reset Asteroid
            heading = random.randint(0, 360)
            distance = random.randint(800, 1000)
            asteroid.setheading(heading)
            asteroid.fd(distance)
            asteroid.setheading(get_heading_to(player, asteroid))
            asteroid.speed += 0.01
            print("Player killed!")
            player.score -= 50
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align = "center", font = ("Arial", 24, "normal"))

wn.mainloop()
