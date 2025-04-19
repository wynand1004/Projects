import time

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def update(self, x, y):
        self.x = x
        self.y = y
        
class Sprite:
    def __init__(self, x, y, color="blue"):
        self.x = x
        self.y = y
        self.color = color
        self.shape = "square"
        self.visible = True
        self.width = 20
        self.height = 20
        self.dx = 0
        self.dy = 0
        self.heading = 0
        self.da = 0
        self.thrust = 0
        
    def render(self, pen, camera):
        pen.goto(self.x - camera.x, self.y - camera.y)
        pen.setheading(0)
        if self.visible:
            pen.color(self.color)
        else:
            pen.color("gray")
        pen.shape(self.shape)
        pen.stamp()

    def is_collision(self, other):
        a = self.x - other.x
        b = self.y - other.y
        a *= a
        b *= b
        
        if a + b < 400:
            return True
        else:
            return False
            
    def is_on_screen(self, SCREEN_WIDTH, camera):
        if self.x - camera.x < SCREEN_WIDTH / 2 and self.x - camera.x > -SCREEN_WIDTH / 2 and self.y - camera.y < SCREEN_WIDTH / 2 and self.y - camera.y > -SCREEN_WIDTH / 2:
                return True
        return False

class Ship(Sprite):
    def __init__(self, x, y, color="blue"):
        Sprite.__init__(self, x, y, color)
        self.shape = "triangle"
        self.da = 0
        self.thrust = 0.0
        self.max_thrust = 1
        self.acceleration = 2
        self.health = 100
        self.max_health = 100
        self.state = "active"
        self.radar = 200
        self.max_dx = 5
        self.max_dy = 5
        
    def update(self, dt):
      self.heading += self.da * dt
      self.dx += math.cos(math.radians(self.heading)) * self.thrust * dt
      self.dy += math.sin(math.radians(self.heading)) * self.thrust * dt
      self.x += self.dx
      self.y += self.dy

    def rotate_left(self):
      self.da = 60.0

    def rotate_right(self):
      self.da = -60.0

    def stop_rotation(self):
      self.da = 0

    def accelerate(self):
      self.thrust += self.acceleration

    def decelerate(self):
      self.thrust -= self.acceleration
      
    def fire(self):
        missile.x = player.x
        missile.y = player.y
        missile.heading = player.heading
        missile.dx = player.dx
        missile.dy = player.dy
        missile.thrust = 1.2

    def render(self, pen, camera):
        pen.goto(self.x - camera.x, self.y - camera.y)
        pen.color(self.color)
        pen.shape(self.shape)
        pen.setheading(self.heading)
        pen.shapesize(stretch_wid=0.5, stretch_len=1.0, outline=0.0)
        pen.stamp()   
        pen.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=0.0)
             

class Missile(Sprite):
    def __init__(self, x, y, color="yellow"):
        Sprite.__init__(self, x, y, color)
        self.shape = "triangle"
    
    def update(self, dt):
      self.dx += math.cos(math.radians(self.heading)) * self.thrust * dt
      self.dy += math.sin(math.radians(self.heading)) * self.thrust * dt
      self.x += self.dx
      self.y += self.dy
      
    def render(self, pen, camera):
        pen.goto(self.x - camera.x, self.y - camera.y)
        pen.color(self.color)
        pen.shape(self.shape)
        pen.setheading(self.heading)
        pen.shapesize(stretch_wid=0.25, stretch_len=0.5, outline=0.0)
        pen.stamp()  
        pen.shapesize(stretch_wid=1.0, stretch_len=1.0, outline=0.0)
        

import turtle
import random
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Asteroid Command")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.penup()
pen2.speed(0)


missile = Missile(100000, 100000, "blue")
player = Ship(0, 0, "blue")
camera = Camera(0, 0);

sprites = []
coordinates = [(0, 0)]

# Generate seeds
seeds = []
colors = ["red", "green", "blue", "orange", "white", "yellow", "purple"]

for _ in range(100):
    x = random.randrange(-1500, 1500, 20)
    y = random.randrange(-1500, 1500, 20)
    color = random.choice(colors)
    if (x, y) not in coordinates:
        coordinates.append((x, y))
        sprite = Sprite(x, y, color)
        seeds.append(sprite)
        sprites.append(sprite)

print("Seeds Generated")

# Grow
offsets = ((0, 20), (0, -20), (-20, 0), (20, 0), (20, 20), (20, -20), (-20, 20), (-20, -20))
while len(seeds) > 0:
    seed = seeds.pop(0)
    seed.render(pen, camera)
    for offset in offsets:
        x = seed.x + offset[0]
        y = seed.y + offset[1]
        if (x, y) not in coordinates:
            coordinates.append((x, y))
            sprite = Sprite(x, y, seed.color)
            sprites.append(sprite)
            
            if random.randint(0, 4) == 1:
                seeds.append(sprite)
 
print("Seeds Grown")

# Hide surrounded sprites
offsets = offsets = ((0, 20), (0, -20), (-20, 0), (20, 0))

for sprite in sprites:
    sprite.visible = False
    for offset in offsets:
        x = sprite.x + offset[0]
        y = sprite.y + offset[1]
        if (x, y) not in coordinates:
            sprite.visible = True
            break

# Keyboard
wn.listen()
wn.onkeypress(player.rotate_left, "Left")
wn.onkeypress(player.rotate_right, "Right")
wn.onkeyrelease(player.stop_rotation, "Left")
wn.onkeyrelease(player.stop_rotation, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeyrelease(player.decelerate, "Up")
wn.onkeypress(player.fire, "space")

# Main Game Loop
frame = 0

start_time = time.time()

SCREEN_WIDTH = 1000

while True:
    dt = (time.time() - start_time) * 100000;
    wn.tracer(0)

    
    # check for collision with player or missile
    for i in range(len(sprites)-1, -1, -1):
        sprite = sprites[i];
        if sprite.is_on_screen(SCREEN_WIDTH, camera):
            # Check player collision
            if player.is_collision(sprite):
                player.x -= player.dx
                player.y -= player.dy
                
                player.dx = 0
                player.dy = 0
                # print(f"{player.x} {player.y} : {sprite.x} {sprite.y} -> COLLISION")
                
            if missile.is_collision(sprite):
                missile.x -= missile.dx
                missile.y -= missile.dy
                missile.dx = 0
                missile.dy = 0
                # TODO: Implmenet Active/Not Active
                missile.x = 100000
                missile.y = 100000
                missile.dx = 0
                missile.dy = 0
                coordinates.remove((sprite.x, sprite.y))
                sprites.remove(sprite)
                
                for sprite in sprites:
                    if sprite.is_on_screen(SCREEN_WIDTH, camera):
                        sprite.visible = False
                        for offset in offsets:
                            x = sprite.x + offset[0]
                            y = sprite.y + offset[1]
                            if (x, y) not in coordinates:
                                sprite.visible = True
                                break
                    
    # render blocks every x frames
    if frame % 1 == 0:
        pen.clear()
        rendered = 0
        for sprite in sprites:
            if sprite.is_on_screen(SCREEN_WIDTH, camera):
                    sprite.render(pen, camera)
                    rendered += 1
        print(f"{rendered} / {len(sprites)} rendered")
            
    player.update(dt)
    camera.update(player.x, player.y)
    missile.update(dt)
    
    pen2.clear()
    player.render(pen2, camera)
    missile.render(pen2, camera)
    
    wn.update()
    
    start_time = time.time()
    
    # For debugging
    frame += 1
    # print(f"frame: {frame}")
wn.mainloop()
        
