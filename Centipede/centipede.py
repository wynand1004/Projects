import turtle
import time
import random
import math

# Classes
class Sprite:
    def __init__(self, x, y, color="white", shape="square"):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.color = color
        self.shape = shape
        
    def goto(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def is_collision(self, other):
        a = self.x - other.x
        b = self.y - other.y
        d = math.sqrt(a**2 + b**2)
        
        if d<20:
            return True
        else:
            return False
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.color(self.color)
        pen.shape(self.shape)
        pen.stamp()

class Segment(Sprite):
    def __init__(self, x, y, color="green"):
        super().__init__(x, y, color, "circle")
                
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
        
    def spawn(self, segment):
        i = self.body.index(segment)
        new_centipede = self.body[i+1:]
        self.body = self.body[:i-1]
        segment = None
        
        if len(new_centipede) > 0:
            return new_centipede
        else:
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
            if head.is_collision(mushroom):
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
            
        if head.y < -380:
            head.y -= dy
            self.direction = "up"
            
        if head.y > 380:
            head.y -+ dy
            self.direction = "down"
       
    def goto(self, x, y):
        for segment in self.body:
            segment.goto(x, y)
        
    def render(self, pen):
        for segment in self.body:
            segment.render(pen)

class Mushroom(Sprite):
    def __init__(self, x, y, color="white", shape="square"):
        super().__init__(x, y, color, shape)
        self.health = 4
        self.colors = ("black", "red", "orange", "yellow", "white")
        
    def register_hit(self):
        self.health -= 1
        if self.health < 0:
            self.health = 0
        self.color = self.colors[self.health]
        
    def rejuvenate(self):
        self.health = 4
        self.color = self.colors[self.health]
        

class Player(Sprite):
    def __init__(self, x, y, color="yellow", shape="arrow"):
        super().__init__(x, y, color, shape)
        self.lives = 3
        self.speed = 2.5
        self.score = 0
        
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

class Weapon(Sprite):
    def __init__(self, x, y, color="yellow", shape="arrow"):
        super().__init__(x, y, color, shape)
        self.dy = 10
    
    def fire(self):
        if self.y > 400:
            self.goto(player.x, player.y)
                
# Set up the screen
wn = turtle.Screen()
wn.title("Centipede by @TokyoEdtech")
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

# Create pen (for drawing text)
text_pen = turtle.Turtle()
text_pen.speed(0)
text_pen.shape("square")
text_pen.color("white")
text_pen.lt(90)
text_pen.penup()
text_pen.hideturtle()



# Create centipede(s)
centipedes = [Centipede(-280, 380, [], "green", 10)]

# Create mushroom(s)
mushrooms = []
for _ in range(25):
    x = random.randrange(-300, 300, 20)
    y = random.randrange(-100, 380, 20)
    mushrooms.append(Mushroom(x, y, "white"))
    print(x, y)

# Create player
player = Player(0, -300, "yellow", "arrow")

# Create weapon
weapon = Weapon(0, 1000, "yellow", "arrow")

# Game variables
delay = 0

# Keyboard bindings
wn.listen()
wn.onkeypress(player.go_up, "Up")
wn.onkeypress(player.go_down, "Down")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_up, "w")
wn.onkeypress(player.go_down, "s")
wn.onkeypress(player.go_left, "a")
wn.onkeypress(player.go_right, "d")
wn.onkeypress(weapon.fire, "space")

# Draw the score
text_pen.goto(-280, 360)
text_pen.color("white")
text_pen.write(f"Score: {player.score}  Lives: {player.lives}", move=False, align='left', font=('Courier New', 24, 'normal')) 


# Main game loop
frame = 0
max_frames = 10
level = 1

while True:
    wn.update()
    pen.clear()
    
    if player.lives == 0:
        text_pen.clear()
        text_pen.goto(-280, 360)
        text_pen.color("white")
        text_pen.write(f"Score: {player.score}  Lives: {player.lives}", move=False, align='left', font=('Courier New', 24, 'normal')) 
        text_pen.goto(-50, 0)
        text_pen.color("RED")
        text_pen.write(f"GAME OVER")
        continue

    # Move centipedes based on frames
    if frame == 0:
        for centipede in centipedes:
            centipede.move(mushrooms)
            
    frame += 1
    if frame == max_frames:
        frame = 0
    
    # Render game objects
    game_objects = centipedes + mushrooms + [player, weapon]
    
    for game_object in game_objects:
        game_object.render(pen)
    
    # Move player and weapon
    player.move()
    weapon.move()
    
    # Check for weapon collisions with mushrooms
    for i in range(len(mushrooms)-1, -1, -1):
        mushroom = mushrooms[i]
        if weapon.is_collision(mushroom):
            mushroom.register_hit()
            weapon.y = 1000
            
            if mushroom.health == 0:
                mushrooms.remove(mushroom)
                player.score += 1
                
        if player.is_collision(mushroom):
            player.x -= player.dx
            player.y -= player.dy
            player.dx = 0
            player.dy = 0
        
    # Check for collisions with segments
    for i in range(len(centipedes)-1, -1, -1):
        centipede = centipedes[i]
        for segment in centipede.body:
            if weapon.is_collision(segment):
                # Check if it is the head
                if centipede.body.index(segment) == 0:
                    centipede.body.pop(0)
                    mushrooms.append(Mushroom(segment.x, segment.y))
                    if len(centipede.body) > 0:
                        centipede.body[0].color = "red"
                    else:
                        centipedes.remove(centipede)
                    player.score += 100
                else:
                    # segment.color = "red"
                    weapon.y = 1000
                    mushrooms.append(Mushroom(segment.x, segment.y))

                    segments = centipede.spawn(segment)
                    if segments != None and len(segments) > 0:
                        x = segments[0].x
                        y = segments[0].y
                        centipedes.append(Centipede(x, y, segments))
                    player.score += 10
                    
                # Draw the score
                text_pen.clear()
                text_pen.goto(-280, 360)
                text_pen.color("white")
                text_pen.write(f"Score: {player.score}  Lives: {player.lives}", move=False, align='left', font=('Courier New', 24, 'normal')) 

    
    # Check for collision with player
    for centipede in centipedes:
        for segment in centipede.body:
            if(segment.is_collision(player)):
                player.lives -= 1
                player.goto(0, -300)
                player.dx = 0
                player.dy = 0
                centipedes.clear()
                for _ in range(level):
                    x = random.randrange(-280, 280, 20)
                    size = random.randint(10, 10 + level * 2)
                    centipedes.append(Centipede(x, 380, [], "green", size))
    
    # Remove empty centipedes
    for i in range(len(centipedes)-1, -1, -1):
        if len(centipedes[i].body) == 0:
            centipedes.remove(centipedes[i])
    
    # End of level
    if(len(centipedes)==0):
        # 5 points for damaged mushrooms
        # Rejuvenate mushrooms
        for mushroom in mushrooms:
            if mushroom.health < 4:
                player.score += 5
                mushroom.rejuvenate()
                
        # Draw the score
        text_pen.clear()
        text_pen.goto(-280, 360)
        text_pen.color("white")
        text_pen.write(f"Score: {player.score}  Lives: {player.lives}", move=False, align='left', font=('Courier New', 24, 'normal')) 

        # Start new centipede(s)
        level += 1
        centipedes.clear()
        for _ in range(level):
            x = random.randrange(-280, 280, 20)
            size = random.randint(10, 10 + level * 2)
            centipedes.append(Centipede(x, 380, [], "green", size))
    
    
    # Debug
    # print(f"# of centipedes: {len(centipedes)}")
