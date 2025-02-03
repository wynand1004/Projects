import turtle
import time
import random
import math

# Classes
class Segment:
    def __init__(self, x, y, color="white"):
        self.x = x
        self.y = y
        self.color = color
        self.shape = "circle"
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.color(self.color)
        pen.shape(self.shape)
        pen.stamp()

class Centipede:
    def __init__(self, x, y, segments = [], color="green", size = 1):
        self.x = x
        self.y = y
        self.speed = 20
        self.size = size
        self.body = segments
        for i in range(size):
            self.body.append(Segment(x, y, color))
        
        self.body[0].color = "red"
        
        self.direction = "right"
        
    def spawn(self):
        for i in range(1, len(self.body)):
            segment = self.body[i]
            if segment.color == "red":
                new_centipede = self.body[i+1:]
                self.body = self.body[:i-1]
                segment = None
                return new_centipede
        
        return None
        
    def move(self, mushrooms = [], left_border = -280, right_border = 280):
        
        head = self.body[0]
        
        dx = 0
        dy = 0
        
        if self.direction == "right":
            dx = self.speed
            dy = 0
        
        if self.direction == "left":
            dx = -self.speed
            dy = 0
            
        if self.direction == "down":
            dx = 0
            dy = -self.speed
            
        if self.direction == "up":
            dx = 0
            dy = self.speed
        
        # Check for mushroom collision
        for mushroom in mushrooms:
            if head.x + dx == mushroom.x and head.y + dy == mushroom.y:
                if self.direction == "left" or self.direction == "right":
                    self.direction = "down"
                    return None
                    
        # Move body
        if len(self.body) > 1:
            for i in range(len(self.body)-1, 0, -1):
                segment1 = self.body[i]
                segment2 = self.body[i-1]
                # Check to see if they are on top of each other
                # If so, wait
                if((segment1.x != segment2.x) or (segment1.y != segment2.y)):
                    segment1.x = segment2.x
                    segment1.y = segment2.y
        
        # Move head
        head.x += dx
        head.y += dy
        
        if self.direction == "down":
            if random.randint(0, 1) == 0:
                self.direction = "left"
            else:
                self.direction = "right"
                
        
        # Check for border collision
        if head.x > right_border or head.x < left_border:
            head.x -= dx
            self.direction = "down"
       
    def render(self, pen):
        for segment in self.body:
            segment.render(pen)

class Mushroom:
    def __init__(self, x, y, color="white"):
        self.x = x
        self.y = y
        self.health = 3
        self.colors = ("black", "red", "yellow", "white")
        self.shape = "square"
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.color(self.colors[self.health])
        pen.shape(self.shape)
        pen.stamp()
        
class Player:
    def __init__(self, x, y, color="yellow"):
        self.x = x
        self.y = y
        self.lives = 3
        self.color = color
        self.dx = 0
        self.dy = 0
        self.speed = 2.5
        self.shape = "arrow"
        
    def go_up(self):
        self.dy = self.speed
        
    def go_down(self):
        self.dy = -self.speed
    
    def go_left(self):
        self.dx = -self.speed
        
    def go_right(self):
        self.dx = self.speed
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        if self.x < -280:
            self.x = -280
            self.dx = 0
            
        if self.x > 280:
            self.x = 280
            self.dx = 0
            
        if self.y < -380:
            self.y = -380
            self.dy = 0
            
        if self.y > -100:
            self.y = -100
            self.dy = 0
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.color(self.color)
        pen.shape(self.shape)
        pen.stamp()

class Weapon():
    def __init__(self, x, y, color="yellow"):
        self.x = x
        self.y = y
        self.color = color
        self.dy = 10
    
    def fire(self):
        self.goto(player.x, player.y)
    
    def goto(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        self.y += self.dy
        
    def is_collision(self, other):
        a = self.x - other.x
        b = self.y - other.y
        a *= a
        b *= b
        d = math.sqrt(a + b)
        
        if d<20:
            return True
        else:
            return False
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.color(self.color)
        pen.stamp()    

# Set up the screen
wn = turtle.Screen()
wn.title("Centipede by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

# Create pen (for drawing graphics)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.lt(90)
pen.penup()
pen.hideturtle()

# Create centipede(s)
centipedes = [Centipede(-280, 380, [], "green", 20)]

# Create mushroom(s)
mushrooms = []
for _ in range(50):
    x = random.randrange(-300, 300, 20)
    y = random.randrange(-100, 380, 20)
    mushrooms.append(Mushroom(x, y, "white"))
    print(x, y)

# Create player
player = Player(0, -300)

# Create weapon
weapon = Weapon(0, 1000)

# Game variables
delay = 0

# Keyboard bindings
wn.listen()
wn.onkeypress(player.go_up, "Up")
wn.onkeypress(player.go_down, "Down")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(weapon.fire, "space")

# Main game loop
frame = 0
max_frames = 10

while True:
    wn.update()
    pen.clear()
    
    if frame == 0:
        for centipede in centipedes:
            centipede.move(mushrooms)
    frame += 1
    if frame == max_frames:
        frame = 0
    
    for centipede in centipedes:
        centipede.render(pen)

    for mushroom in mushrooms:
        mushroom.render(pen)
    
    player.move()
    player.render(pen)
    
    weapon.move()
    weapon.render(pen)
    
    # Check for weapon collisions with mushrooms
    to_be_deleted = []
    
    for mushroom in mushrooms:
        if weapon.is_collision(mushroom):
            mushroom.health -= 1
            weapon.y = 1000
            
            if mushroom.health == 0:
                to_be_deleted.append(mushroom)
    
    for mushroom in to_be_deleted:
        mushrooms.remove(mushroom)
        
    # Check for collisions with segments
    for centipede in centipedes:
        for segment in centipede.body:
            if weapon.is_collision(segment):
                segment.color = "red"
                weapon.y = 1000

    for centipede in centipedes:
        segments = centipede.spawn()
        if segments != None and len(segments) > 0:
            x = segments[0].x
            y = segments[0].y
            centipedes.append(Centipede(x, y, segments))
