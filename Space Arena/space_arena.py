# Space Arena!
# Python 3.x Compatible
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
wn.setup(width = SCREEN_WIDTH + 220, height = SCREEN_HEIGHT + 20)
wn.title("Space Arena! by #TokyoEdTech")
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

radar_pen = turtle.Turtle()
radar_pen.speed(0)
radar_pen.shape("square")
radar_pen.color("white")
radar_pen.penup()
radar_pen.hideturtle()

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
time.sleep(0)

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame = 0
        self.show_radar = False
        
    def toggle_radar(self):
        self.show_radar = not self.show_radar
        
    def render_info(self, pen, score, active_enemies):
        pen.color("#222255")
        pen.penup()
        pen.goto(400, 0)
        pen.shape("square")
        pen.setheading(90)
        pen.shapesize(stretch_wid=10, stretch_len=32, outline=None)
        pen.stamp()
        
        pen.color("white")
        pen.width(3)
        pen.goto(300, 400)
        pen.pendown()
        pen.goto(300, -400)
        
        pen.penup() 
        pen.color("white")
        pen.goto(400, 250)
        pen.write("Score: {}".format(score), align="center", font=("Courier", 18, "normal"))
        pen.goto(400, 230)
        pen.write("Enemies: {}".format(active_enemies), align="center", font=("Courier", 18, "normal"))
    
    def render_border(self, pen, x_offset, y_offset, screen_width, screen_height):
        pen.color("white")
        pen.width(3)
        pen.penup()
        left = -self.width/2.0 - x_offset
        right = self.width/2.0 - x_offset
        top = self.height/2.0 - y_offset
        bottom = -self.height/2.0 - y_offset
        
        pen.goto(left, top)
        pen.pendown()
        pen.goto(right, top)
        pen.goto(right, bottom)
        pen.goto(left, bottom)
        pen.goto(left, top)
        pen.penup()

class Sprite():
    
    @staticmethod
    def is_collision(sprite1, sprite2, threshold):
        d = math.sqrt((sprite1.x-sprite2.x)**2 + (sprite1.y-sprite2.y)**2)
        if d < threshold:
            return True
        else:
            return False
    
    @staticmethod
    def is_on_screen(sprite, screen_width, screen_height, x_offset, y_offset):
        if sprite.x + 120 - x_offset < screen_width / 2 and sprite.x - x_offset > -screen_width / 2\
            and sprite.y - y_offset < screen_height /2 and sprite.y - y_offset > - screen_height / 2:    
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
        if self.x > game.width / 2.0 - 10.0:
            self.x = game.width / 2.0 - 10.0
            self.dx *= -1.0
        elif self.x < -game.width / 2.0 + 10.0:
            self.x = -game.width / 2.0 + 10.0
            self.dx *= -1.0
            
        if self.y > game.height / 2.0 - 10.0:
            self.y = game.height / 2.0 - 10.0
            self.dy *= -1.0
        elif self.y < -game.height / 2.0 + 10.0:
            self.y = -game.height / 2.0 + 10.0
            self.dy *= -1.0       
        
    def render(self, pen, x_offset = 0, y_offset = 0):
        # Check if active
        if self.state == "active":
            # Check if it is on the screen
            screen_x = self.x - x_offset
            screen_y = self.y - y_offset
            
            if(screen_x > -game.width/2.0 and screen_x < game.width/2.0 and screen_y > -game.height/2.0 and screen_y < game.width/2.0):
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
        self.max_health = 40
        self.health = self.max_health
        self.sensor_range = 500
        
    def rotate_left(self):
        self.da = 10.0
        
    def rotate_right(self):
        self.da = -10.0
        
    def stop_rotation(self):
        self.da = 0.0
        
    def accelerate(self):
        self.thrust += 0.2
        
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
        
    def render(self, pen, x_offset = 0, y_offset = 0):
        pen.shapesize(stretch_wid=0.5, stretch_len=1, outline=None) 
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.setheading(self.heading)
        pen.stamp()
        
        # Draw health
        pen.goto(self.x - x_offset - 10.0, self.y - y_offset + 20.0)
        pen.width(3.0)
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
            
class Enemy(Sprite):
    def __init__(self, x, y, shape = "square", color = "red"):
        Sprite.__init__(self, x, y, shape, color)
        self.max_health = random.randint(10, 30)
        self.health = self.max_health
        self.type = random.choice(["hunter", "mine", "surveillance"])
        self.max_dx = 3.0
        self.max_dy = 3.0
        self.sensor_range = random.randint(40, 60)
        
        if self.type == "hunter":
            self.color = "red"
            self.sensor_range = random.randint(100, 200)
            
        elif self.type == "mine":
            self.color = "orange"
            self.sensor_range = random.randint(100, 200)

        elif self.type == "surveillance":
            self.color = "pink"
            self.sensor_range = random.randint(200, 400)

    def update(self):
        
        if self.health <= 0:
            self.state = "inactive"
                    
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
                    self.dx += 0.05
                else: 
                    self.dx -= 0.05

                if self.y < player.y:
                    self.dy += 0.05
                else: 
                    self.dy -= 0.05
            
        elif self.type == "mine":
            self.dx = 0.0
            self.dy = 0.0
            
            if Sprite.is_collision(player, self, self.sensor_range):
                self.type = "hunter"
                self.color = "red"
            
        elif self.type == "surveillance":
            if Sprite.is_collision(player, self, self.sensor_range):
                if self.x > player.x:
                    self.dx += 0.03
                else: 
                    self.dx -= 0.03

                if self.y > player.y:
                    self.dy += 0.03
                else: 
                    self.dy -= 0.03
        
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
        if self.state == "active":
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
        self.thrust = 5.0
        self.max_fuel = 200.0
        self.fuel = 200.0
        self.damage = 5.0

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
        self.width = 0.5 / self.distance

    def render(self, pen, x_offset = 0, y_offset = 0):
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
        self.dx = random.randint(-30, 30) / 10.0
        self.dy = random.randint(-30, 30) / 10.0

class Particle(Sprite):
    def __init__(self, x, y, shape = "triangle", color = "red"):
        Sprite.__init__(self, x, y, shape, color)
        self.dx = random.randint(-6, 6)
        self.dy = random.randint(-6, 6)
        self.frame = random.randint(10, 20)
        self.color = random.choice(["red", "orange", "yellow"])
        self.shape = "triangle"
        self.state = "inactive"
        
    def render(self, pen, x_offset = 0, y_offset = 0):
        self.frame -= 1
        self.dx *= 0.85
        self.dy *= 0.85
        if self.frame <= 0:
            self.frame = random.randint(10, 20)
            self.state = "inactive"
        pen.shapesize(stretch_wid=0.05, stretch_len=0.05, outline=None) 
        pen.goto(self.x - x_offset, self.y - y_offset)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()       

class Explosion():
    def __init__(self, number_of_particles):
        self.particles = []
        for _ in range(number_of_particles):
            self.particles.append(Particle(0,0))
            
    def explode(self, x, y, dx_offset = 0, dy_offset = 0):
        for particle in self.particles:
            if particle.state == "inactive":
                particle.x = x
                particle.y = y
                particle.dx = random.randint(-12, 12)
                particle.dy = random.randint(-12, 12)
                particle.dx += dx_offset * 2
                particle.dy += dy_offset * 2
                particle.state = "active"
                
    def render(self, pen, x_offset = 0, y_offset = 0):
        for particle in self.particles:
            if particle.state == "active":
                particle.update()
                particle.render(pen, x_offset, y_offset) 

class Radar():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def render(self, pen, sprites, render):         
        # Draw radar border
        pen.color("white")
        pen.penup()
        
        # Draw opaque background
        # pen.goto(self.x, self.y)
        # pen.shape("square")
        # pen.setheading(0)
        
        # pen.color("white")
        # pen.shapesize(stretch_wid=self.width/20, stretch_len=self.height/20, outline=None)
        # pen.stamp()
        
        # pen.color("#111111")
        # pen.shapesize(stretch_wid=self.width/21, stretch_len=self.height/21, outline=None)
        # pen.stamp()
        if render:
            # Draw sprite radar images
            for sprite in sprites:
                if sprite.state == "active" and Sprite.is_collision(player, sprite, player.sensor_range):
                    radar_x = self.x + (sprite.x - player.x) * (self.width / game.width)
                    radar_y = self.y + (sprite.y - player.y) * (self.height / game.height)
                    pen.goto(radar_x, radar_y)
                    pen.color(sprite.color)
                    pen.shape(sprite.shape)
                    pen.setheading(sprite.heading)
                    if isinstance(sprite, Player):
                        pen.shapesize(stretch_wid=0.1, stretch_len=0.2, outline=None) 
                    elif isinstance(sprite, Missile):
                        pen.shapesize(stretch_wid=0.05, stretch_len=0.5, outline=None)
                    else:
                        pen.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)   
                    pen.stamp()
            pen.setheading(90)
            pen.goto(self.x + 100, self.y)
            pen.pendown()
            pen.circle(100)
            pen.penup()
        else:
            pen.goto(self.x, self.y)
            pen.write("Radar OFF", align="center", font=("Courier", 15, "normal"))
            pen.goto(self.x, self.y - 20)
            pen.write("Press r to Enable", align="center", font=("Courier", 15, "normal"))


# Set up the game
game = Game(1600, 1200)

radar = Radar(400, -200, 200, 200)

# Create the player
player = Player()

missiles = []
for _ in range(3):
    missiles.append(Missile(0.0, 0.0))

# Create enemies
enemies = []
for _ in range(10):
    enemies.append(Enemy(0.0, 0.0))
    
for enemy in enemies:
    x = random.randint(-game.width/2.0, game.width/2.0)
    y = random.randint(-game.height/2.0, game.height/2.0)
    dx = random.randint(0, 10) / 20.0
    dy = random.randint(0, 10) / 20.0
    enemy.x = x
    enemy.y = y
    enemy.dx = dx
    enemy.dy = dy

stars = []    
for _ in range(10):
    x = random.randint(int(-game.width/4.0), int(game.width/4.0))
    y = random.randint(int(-game.height/4.0), int(game.height/4.0))
    stars.append(Star(x, y))

powerups = []
for _ in range(5):
    x = random.randint(-game.width/2.0, game.width/2.0)
    y = random.randint(-game.height/2.0, game.height/2.0)
    powerups.append(Powerup(x, y))

explosion = Explosion(30)

# Create sprites list
sprites = []

background_sprites = []

for star in stars:
    background_sprites.append(star)
    
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

# Game settings
wn.onkeypress(game.toggle_radar, "r")

def timer(game=game):
    print(game.frame)
    game.frame = 0
    turtle.ontimer(timer, 1000)
    

turtle.ontimer(timer, 1000)

while True:
    game.frame += 1
    
    # Render explosions
    explosion.render(pen, player.x, player.y)
    
    for sprite in background_sprites:
        sprite.update()
        if Sprite.is_on_screen(sprite, SCREEN_WIDTH, SCREEN_HEIGHT, player.x, player.y):
            sprite.render(pen, player.x+100, player.y)
    
    # Move and render the sprites
    for sprite in sprites:
        if sprite.state == "active":
            sprite.update()
            if Sprite.is_on_screen(sprite, SCREEN_WIDTH, SCREEN_HEIGHT, player.x, player.y):
                sprite.render(pen, player.x+100, player.y)
    
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
                    center_x = (player.x + sprite.x) / 2.0
                    center_y = (player.y + sprite.y) / 2.0
                    explosion.explode(center_x-100, center_y) 
                    
                    # Swap momentum for bounce                           
                    temp_dx = player.dx
                    temp_dy = player.dy
                    
                    player.dx = sprite.dx
                    player.dy = sprite.dy
                    
                    sprite.dx = temp_dx
                    sprite.dy = temp_dy
                    
                    # Check for player death
                    if player.health <= 0:
                        player.reset()
                    else:
                        if sprite.health > 0:
                            player.health -= random.randint(0, int(sprite.health))
                        if player.health > 0:
                            sprite.health -= random.randint(0, int(player.health))
                        if sprite.health <= 0:
                            sprite.state = "inactive"

                # Missile collides with enemy
                for missile in missiles:
                    if missile.state == "active":
                        if Sprite.is_collision(missile, sprite, 13.0):
                            sprite.health -= missile.damage
                            sprite.dx += missile.dx / 3.0
                            sprite.dy += missile.dy / 3.0
                            if sprite.health <= 0:
                                sprite.state = "inactive"
                                player.score += 10
                            
                            explosion.explode(missile.x-100, missile.y, -missile.dx, -missile.dy) 
                            
                            missile.reset()

            # Powerup collides with missile
            if isinstance(sprite, Powerup):
            # Missile collides with enemy
                for missile in missiles:
                    if missile.state == "active":
                        if Sprite.is_collision(missile, sprite, 13):
                            sprite.state = "inactive"
                            player.score -= 50
                            
                            explosion.explode(missile.x-100, missile.y, -missile.dx, -missile.dy)
                            
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
    
    # Render the game border
    game.render_border(pen, player.x+100, player.y, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Render the score and game attributes
    game.render_info(pen, player.score, active_enemies)
    
    # Render the radar
    radar.render(pen, sprites, game.show_radar)
    
    # Update the screen
    wn.update()
    
    # Clear everything
    pen.clear()

# wn.mainloop()
