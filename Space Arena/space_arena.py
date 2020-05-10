# Space Arena!
# Python 2 & 3 Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech
# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/

import turtle
import math
import random
import time

SCREEN_WIDTH = 800  
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
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
pen.goto(0, 200)
pen.write("SPACE ARENA!", align="center", font=("Courier", 30, "normal"))
pen.goto(0, 150)
pen.write("Kill the red enemies with your missiles. You have 3 to begin with.", align="center", font=("Courier", 15, "normal"))
pen.goto(0, 100)
pen.write("Collect the blue powerups to increase the number, power,", align="center", font=("Courier", 15, "normal"))
pen.goto(0, 50)
pen.write("speed, and range of your missiles.", align="center", font=("Courier", 15, "normal"))
pen.goto(0, 0)
pen.write("Use the arrows to rotate and accelerate. Space to fire.", align="center", font=("Courier", 15, "normal"))
wn.update()
time.sleep(5)

class World():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def render_info(self, pen, score, active_enemies):
        pen.goto(0, 280)
        pen.write(f"Score: {score} Enemies Remaining: {active_enemies}", align="center", font=("Courier", 18, "normal"))
    
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
        self.width = 20.0
        self.height = 20.0
        self.heading = 0.0
        self.dx = 0.0
        self.dy = 0.0
        self.da = 0.0
        self.thrust = 0.0
        self.max_d = 2.0
        self.x = x
        self.y = y
        self.state = "active"

    def update(self):        
        self.heading += self.da
        self.heading %= 360.0
        
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
        self.x += self.dx
        self.y += self.dy
        
        self.border_check()
            
    def border_check(self):
        if self.x > world.width / 2.0 - 10.0:
            self.x = world.width / 2.0 - 10.0
            self.dx *= -1.0
        elif self.x < -world.width / 2.0 + 10.0:
            self.x = -world.width / 2.0 + 10.0
            self.dx *= -1.0
            
        if self.y > world.height / 2.0 - 10.0:
            self.y = world.height / 2.0 - 10.0
            self.dy *= -1.0
        elif self.y < -world.height / 2.0 + 10.0:
            self.y = -world.height / 2.0 + 10.0
            self.dy *= -1.0       
        
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
        Sprite.__init__(self, 0.0, 0.0, "triangle")
        self.da = 0.0
        self.heading = 90.0
        self.score = 0
        self.max_health = 100.0
        self.health = 100.0
        
    def rotate_left(self):
        self.da = 10.0
        
    def rotate_right(self):
        self.da = -10.0
        
    def stop_rotation(self):
        self.da = 0.0
        
    def accelerate(self):
        self.thrust += 0.1
        
    def decelerate(self):
        self.thrust = 0.0
        
    def fire(self):
        for missile in missiles:
            if missile.state == "ready":
                missile.x = player.x
                missile.y = player.y
                missile.dx = player.dx
                missile.dy = player.dy
                missile.heading = player.heading
                missile.dx += math.cos(math.radians(self.heading)) * missile.thrust
                missile.dy += math.sin(math.radians(self.heading)) * missile.thrust
                missile.state = "active"
                
                self.dx -= missile.dx * 0.05
                self.dy -= missile.dy * 0.05
                break

    def reset(self):
        self.x = 0.0
        self.y = 0.0
        self.dx = 0.0
        self.dy = 0.0
        self.heading = 90.0
        self.health = self.max_health
        
    def render(self, pen, x_offset, y_offset):
        pen.shapesize(stretch_wid=0.5, stretch_len=1, outline=None) 
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.setheading(self.heading)
        pen.stamp()
        
        # Draw health
        pen.goto(self.x - x_offset - 10.0, self.y - y_offset + 20.0)
        pen.width(2.0)
        pen.pendown()
        pen.setheading(0.0)
        try:
            if self.health/self.max_health < 0.3:
                pen.color("red")
            elif self.health/self.max_health < 0.7:
                pen.color("yellow")
            else:
                pen.color("green")
            pen.fd(20.0 * (self.health/100.0))
            pen.color("grey")
            pen.fd(20.0 * ((100.0-self.health)/100.0))
        except:
            pass
            
        pen.penup()
            
class Enemy(Sprite):
    def __init__(self, x, y, shape = "square", color = "red"):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = random.randint(10, 30)
        self.health = self.max_health
        self.type = random.choice(["hunter", "mine", "surveillance"])
        self.max_dx = 1.0
        self.max_dy = 1.0
        self.sensor_range = random.randint(40, 60)
        
        if self.type == "hunter":
            self.color = "red"
            self.sensor_range = random.randint(200, 400)
            
        elif self.type == "mine":
            self.color = "orange"
            self.sensor_range = random.randint(100, 200)

        elif self.type == "surveillance":
            self.color = "pink"
            self.sensor_range = random.randint(300, 500)

    def update(self):        
        self.heading += self.da
        self.heading %= 360.0
        
        self.dx += math.cos(math.radians(self.heading)) * self.thrust
        self.dy += math.sin(math.radians(self.heading)) * self.thrust
        
        self.x += self.dx
        self.y += self.dy
        
        # Change movement based on type
        if self.type == "hunter":
            if Sprite.is_collision(player, self, self.sensor_range):
                if self.x < player.x:
                    self.dx += 0.01
                else: 
                    self.dx -= 0.01

                if self.y < player.y:
                    self.dy += 0.01
                else: 
                    self.dy -= 0.01
            
        elif self.type == "mine":
            self.dx = 0.0
            self.dy = 0.0
            
            if Sprite.is_collision(player, self, self.sensor_range):
                self.type = "hunter"
                self.color = "red"
            
        elif self.type == "surveillance":
            if Sprite.is_collision(player, self, self.sensor_range):
                if self.x > player.x:
                    self.dx += 0.01
                else: 
                    self.dx -= 0.01

                if self.y > player.y:
                    self.dy += 0.01
                else: 
                    self.dy -= 0.01
        
        # Check max velocity
        if self.dx > self.max_dx:
            self.dx = self.max_dx
        elif self.dx < -self.max_dx:
            self.dx = -self.max_dx
            
        if self.dy > self.max_dy:
            self.dy = self.max_dy
        elif self.dy < -self.max_dy:
            self.dy = -self.max_dy
        
        self.border_check()

    def render(self, pen, x_offset, y_offset):
        pen.shapesize(stretch_wid=1, stretch_len=1, outline=None) 
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.setheading(self.heading)
        pen.stamp()
        
        # Draw health
        pen.goto(self.x - x_offset - 10.0, self.y - y_offset + 20.0)
        pen.width(2)
        pen.pendown()
        pen.setheading(0.0)
        try:
            if self.health/self.max_health < 0.3:
                pen.color("red")
            elif self.health/self.max_health < 0.7:
                pen.color("yellow")
            else:
                pen.color("green")
            pen.fd(20.0 * (self.health/self.max_health))
            pen.color("grey")
            pen.fd(20.0 * ((self.max_health-self.health)/self.max_health))
        except:
            pass
            
        pen.penup()

class Missile(Sprite):
    def __init__(self, x, y, shape = "triangle", color = "yellow"):
        Sprite.__init__(self, x, y, shape, color)
        self.state = "ready"
        self.thrust = 3.0
        self.max_fuel = 200.0
        self.fuel = 200.0
        self.damage = 10.0

    def update(self):        
        self.heading += self.da
        self.heading %= 360.0
        
        self.x += self.dx
        self.y += self.dy
        
        self.border_check()
        
        self.fuel -= self.thrust
        if self.fuel < 0:
            self.state = "ready"
            self.fuel = self.max_fuel

    def border_check(self):
        if self.x > world.width / 2.0 - 10.0:
            self.state = "ready"
            self.fuel = self.max_fuel
        elif self.x < -world.width / 2.0 + 10.0:
            self.state = "ready"
            self.fuel = self.max_fuel
            
        if self.y > world.height / 2.0 - 10.0:
            self.state = "ready"
            self.fuel = self.max_fuel
            
        elif self.y < -world.height / 2.0 + 10.0:
            self.state = "ready"
            self.fuel = self.max_fuel
            
    def reset(self):
        self.state = "ready"
        self.fuel = self.max_fuel

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
        self.distance = random.randint(2, 6)
        self.color = random.choice(["white", "yellow", "orange", "red"])

    def render(self, pen, x_offset, y_offset):
        if self.state == "active":
            pen.shapesize(stretch_wid=0.5/self.distance, stretch_len=0.5/self.distance, outline=None) 
            pen.goto(self.x - x_offset/self.distance, self.y - y_offset/self.distance)
            pen.shape(self.shape)
            pen.color(self.color)
            pen.setheading(self.heading)
            pen.stamp()

class Powerup(Sprite):
    def __init__(self, x, y, shape = "circle", color = "blue"):
        Sprite.__init__(self, x, y, shape, color)
        self.dx = random.randint(-20, 20) / 10.0
        self.dy = random.randint(-20, 20) / 10.0

class Particle(Sprite):
    def __init__(self, x, y, shape = "triangle", color = "red"):
        Sprite.__init__(self, x, y, shape, color)
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        self.frame = random.randint(10, 20)
        self.color = random.choice(["red", "orange", "yellow"])
        self.shape = "triangle"
        self.state = "inactive"
        
    def render(self, pen, x_offset, y_offset):
        self.frame -= 1
        self.dx *= 0.85
        self.dy *= 0.85
        if self.frame <= 0:
            self.frame = random.randint(10, 20)
            self.state = "inactive"
        pen.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None) 
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()       
                          
# Set up the game
world = World(1600, 1200)

# Create the player
player = Player()

missiles = []
for _ in range(3):
    missiles.append(Missile(0.0, 0.0))

# Create enemies
enemies = []
for _ in range(30):
    enemies.append(Enemy(0.0, 0.0))
    
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
for _ in range(20):
    x = random.randint(int(-world.width/4.0), int(world.width/4.0))
    y = random.randint(int(-world.height/4.0), int(world.height/4.0))
    stars.append(Star(x, y))

powerups = []
for _ in range(5):
    x = random.randint(-world.width/2.0, world.width/2.0)
    y = random.randint(-world.height/2.0, world.height/2.0)
    powerups.append(Powerup(x, y))

particles = []
for _ in range(30):
    particles.append(Particle(0, 0))

# Create sprites list
sprites = []

for star in stars:
    sprites.append(star)
    
for particle in particles:
    sprites.append(particle)
    
for powerup in powerups:
    sprites.append(powerup)

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
    
    active_enemies = 0
        
    # Check for collisions
    for sprite in sprites:
        # Check if sprite is active
        if sprite.state == "active":
            # Check if it is an enemy
            if isinstance(sprite, Enemy):
                # Count as active
                active_enemies += 1
                # Player collides with enemy
                if Sprite.is_collision(player, sprite, 18.0):
                    for particle in particles:
                        if random.random() < 0.5 and particle.state == "inactive":
                            particle.x = (player.x + sprite.x) / 2
                            particle.y = (player.y + sprite.y) / 2
                            
                            particle.dx = random.randint(-5, 5)
                            particle.dy = random.randint(-5, 5)
                            
                            particle.state = "active"
                            
                            temp_dx = player.dx
                            temp_dy = player.dy
                            
                            player.dx = sprite.dx
                            player.dy = sprite.dy
                            
                            sprite.dx = temp_dx
                            sprite.dy = temp_dy
                            
                    player.health -= random.randint(0, sprite.health+1)
                    sprite.health -= random.randint(0, player.health+15)
                    sprite.health -= random.randint(0, player.health+1)
                    if player.health <= 0:
                        player.reset()
                    
                # Missile collides with enemy
                for missile in missiles:
                    if missile.state == "active":
                        if Sprite.is_collision(missile, sprite, 13.0):
                            sprite.health -= missile.damage
                            sprite.dx += missile.dx / 6.0
                            sprite.dy += missile.dy / 6.0
                            if sprite.health <= 0:
                                sprite.state = "inactive"
                                player.score += 10

                            for particle in particles:
                                if random.random() < 0.5 and particle.state == "inactive":
                                    particle.x = missile.x
                                    particle.y = missile.y
                                    particle.dx = random.randint(-5, 5)
                                    particle.dy = random.randint(-5, 5)
                                    particle.dx -= missile.dx 
                                    particle.dy -= missile.dy 
                                    particle.state = "active"
                            
                            missile.reset()

            # Powerup collides with missile
            if isinstance(sprite, Powerup):
            # Missile collides with enemy
                for missile in missiles:
                    if missile.state == "active":
                        if Sprite.is_collision(missile, sprite, 13):
                            sprite.state = "inactive"
                            player.score -= 50
                            
                            for particle in particles:
                                if random.random() < 0.3 and particle.state == "inactive":
                                    particle.x = missile.x
                                    particle.y = missile.y
                                    particle.dx = random.randint(-5, 5)
                                    particle.dy = random.randint(-5, 5)
                                    particle.dx -= missile.dx 
                                    particle.dy -= missile.dy 
                                    particle.state = "active"
                            
                            missile.reset()
                        
            # Check if it is a powerup and collides with player
            if isinstance(sprite, Powerup):
                if Sprite.is_collision(player, sprite, 18):
                    sprite.state = "inactive"
                    missiles.append(Missile(0, 0))
                    missiles[-1].max_fuel = missiles[0].max_fuel
                    missiles[-1].thrust = missiles[0].thrust
                    sprites.append(missiles[-1])
                    for missile in missiles:
                        missile.max_fuel *= 1.1
                        missile.thrust *= 1.05
                        missile.damage *= 1.1
    
    # Render the world border
    world.render_border(pen, player.x, player.y)
    
    # Render the score and game attributes
    world.render_info(pen, player.score, active_enemies)
    
    # Update the screen
    wn.update()
    
    # Clear everything
    pen.clear()

# wn.mainloop()
