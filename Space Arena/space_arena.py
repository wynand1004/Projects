# Space Arena!
# by @TokyoEdTech
import turtle
import math
import random

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(width = 800, height = 600)
wn.title("Space Arena! by #TokyoEdTech")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

# Splash screen
wn.update()

class World():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def render_border(self, pen, x_offset, y_offset):
        pen.color("white")
        pen.width(5)
        pen.penup()
        pen.goto(-self.width/2.0 - x_offset, self.height/2.0 - y_offset)
        pen.pendown()
        pen.goto(self.width/2.0 - x_offset, self.height/2.0 - y_offset)
        pen.goto(self.width/2.0 - x_offset, -self.height/2.0 - y_offset)
        pen.goto(-self.width/2.0 - x_offset, -self.height/2.0 - y_offset)
        pen.goto(-self.width/2.0 - x_offset, self.height/2.0 - y_offset)
        pen.penup()

        
class Sprite():
    
    @staticmethod
    def is_collision(sprite1, sprite2, threshold):
        d = math.sqrt((sprite1.x-sprite2.x)**2 + (sprite1.y-sprite2.y)**2)
        if d < threshold:
            return True
        else:
            return False
            
    def __init__(self, x, y, shape="square", color = "white"):
        self.shape = shape
        self.color = color
        self.width = 20
        self.height = 20
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.da = 0
        self.thrust = 0
        self.max_d = 2
        self.x = x
        self.y = y
        self.state = "active"

    def update(self):        
        self.heading += self.da
        self.heading %= 360
        
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
        self.x += self.dx
        self.y += self.dy
        
        self.border_check()
            
    def border_check(self):
        if self.x > world.width / 2.0 - 10:
            self.x = world.width / 2.0 - 10
            self.dx *= -1
        elif self.x < -world.width / 2.0 + 10:
            self.x = -world.width / 2.0 + 10
            self.dx *= -1
            
        if self.y > world.height / 2.0 - 10:
            self.y = world.height / 2.0 - 10
            self.dy *= -1
        elif self.y < -world.height / 2.0 + 10:
            self.y = -world.height / 2.0 + 10
            self.dy *= -1         
        
    def render(self, pen, x_offset, y_offset):
        # Check if active
        if self.state == "active":
            # Check if it is on the screen
            screen_x = self.x - x_offset
            screen_y = self.y - y_offset
            
            if(screen_x > -world.width/2.0 and screen_x < world.width/2.0 and screen_y > -world.height/2.0 and screen_y < world.width/2.0):
                pen.goto(self.x - x_offset, self.y - y_offset)
                pen.shape(self.shape)
                pen.color(self.color)
                pen.shapesize(stretch_wid=1, stretch_len=1, outline=None)
                pen.setheading(self.heading)
                pen.stamp()
        
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self, 0, 0, "triangle")
        self.da = 0
        
    def rotate_left(self):
        self.da = 10
        
    def rotate_right(self):
        self.da = -10
        
    def stop_rotation(self):
        self.da = 0
        
    def accelerate(self):
        self.thrust += 0.1
        
    def decelerate(self):
        self.thrust = 0
        
    def fire(self):
        for missile in missiles:
            if missile.state == "ready":
                missile.x = player.x
                missile.y = player.y
                missile.dx = player.dx
                missile.dy = player.dy
                missile.heading = player.heading
                missile.dx = math.cos(math.radians(self.heading)) * missile.thrust
                missile.dy = math.sin(math.radians(self.heading)) * missile.thrust
                missile.state = "active"
                break

    def render(self, pen, x_offset, y_offset):
        pen.shapesize(stretch_wid=0.5, stretch_len=1, outline=None) 
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.setheading(self.heading)
        pen.stamp()
        
class Enemy(Sprite):
    def __init__(self, x, y, shape = "square", color = "red"):
        Sprite.__init__(self, x, y, shape, color)

class Missile(Sprite):
    def __init__(self, x, y, shape = "triangle", color = "yellow"):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 5
        self.max_fuel = 300
        self.fuel = 300

    def update(self):        
        self.heading += self.da
        self.heading %= 360
        
        self.x += self.dx
        self.y += self.dy
        
        self.border_check()
        
        self.fuel -= self.thrust
        if self.fuel < 0:
            self.state = "ready"
            self.fuel = self.max_fuel

    def border_check(self):
        if self.x > world.width / 2.0 - 10:
            self.state = "ready"
        elif self.x < -world.width / 2.0 + 10:
            self.state = "ready"
            
        if self.y > world.height / 2.0 - 10:
            self.state = "ready"
        elif self.y < -world.height / 2.0 + 10:

            self.state = "ready"

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None) 
            pen.goto(self.x - x_offset, self.y - y_offset)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.setheading(self.heading)
            pen.stamp()

class Star(Sprite):
    def __init__(self, x, y, shape = "circle", color = "yellow"):
        Sprite.__init__(self, x, y, shape, color)
        self.distance = random.randint(5, 10)
        self.color = random.choice(["white", "yellow", "orange", "red"])

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(stretch_wid=0.5/self.distance, stretch_len=0.5/self.distance, outline=None) 
            pen.goto(self.x - x_offset/self.distance, self.y - y_offset/self.distance)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.setheading(self.heading)
            pen.stamp()
                          
# Set up the game
world = World(1600, 1200)

# Create the player
player = Player()

missiles = []
for _ in range(10):
    missiles.append(Missile(0, 0))

# Create enemies
enemies = []
for _ in range(50):
    enemies.append(Enemy(0, 0))
    
for enemy in enemies:
    x = random.randint(-world.width/2.0, world.width/2.0)
    y = random.randint(-world.height/2.0, world.height/2.0)
    dx = random.randint(0, 10) / 20.0
    dy = random.randint(0, 10) / 20.0
    enemy.x = x
    enemy.y = y
    enemy.dx = dx
    enemy.dy = dy

stars = []    
for _ in range(50):
    x = random.randint(-world.width/2.0, world.width/2.0)
    y = random.randint(-world.height/2.0, world.height/2.0)
    stars.append(Star(x, y))

# Create sprites list
sprites = []

for star in stars:
    sprites.append(star)

for missile in missiles:
    sprites.append(missile)

for enemy in enemies:
    sprites.append(enemy)
    
sprites.append(player)

# Keyboard binding
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeyrelease(player.stop_rotation, "Left")

wn.onkeypress(player.rotate_right, "Right")
wn.onkeyrelease(player.stop_rotation, "Right")

wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")

wn.onkeypress(player.fire, "space")

while True:
    # Move and render the sprites
    for sprite in sprites:
        if sprite.state == "active":
            sprite.update()
            sprite.render(pen, player.x, player.y)
        
    # Check for collisions
    for sprite in sprites:
        if sprite.state == "active":
            # Player collides with enemy
            if Sprite.is_collision(player, sprite, 18):
                if isinstance(sprite, Enemy):
                    print("Player Dies")
            # Missile collides with enemy
            for missile in missiles:
                if missile.state == "active" and isinstance(sprite, Enemy) and Sprite.is_collision(missile, sprite, 13) :
                    sprite.state = "inactive"
                    missile.state = "ready"
    
    # Render the world border
    world.render_border(pen, player.x, player.y)
    
    # Update the screen
    wn.update()
    
    # Clear everything
    pen.clear()

# wn.mainloop()
