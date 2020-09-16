# TokyoEdTech
# Side Scrolling Shooter
# Geany IDE
# Python 3.8 and Pygame
# Linux
# Live Coding Demo: 

import pygame
import sys
import random

pygame.init()
pygame.display.set_caption("Sidescrolling Shooter by @TokyoEdTech and Viewers")
clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# icon = pygame.image.load("enemy.png").convert()
# icon = pygame.transform.scale(icon , (64, 64))
# pygame.display.set_icon(icon)

# Create the classes
class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dy = 0
        self.dx = 0
        self.surface = pygame.image.load('player.png').convert()
        self.score = 0
        
    def up(self):
        self.dy = -6
        
    def down(self):
        self.dy = 6
    
    def left(self):
        self.dx = -6
    
    def right(self):
        self.dx = 6
    
    def move(self):
        self.y = self.y + self.dy
        self.x = self.x + self.dx
        
        # Check for border collision
        if self.y < 0:
            self.y = 0
            self.dy = 0
            
        elif self.y > 550 :
            self.y = 550    
            self.dy = 0
            
        if self.x < 0:
            self.x = 0
            self.dx = 0
        
        elif self.x > 200:
            self.x = 200
            self.dx = 0

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
            
    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))

class Missile():
    def __init__(self):
        self.x = 0
        self.y = 1000
        self.dx = 0
        self.surface = pygame.image.load('missile.png').convert()
        self.state = "ready"
    
    def fire(self):
        self.state = "firing"
        self.x = player.x + 25
        self.y = player.y + 16
        self.dx = 10
    
    def move(self):
        if self.state == "firing":
            self.x = self.x + self.dx 
            
        if self.x > 800:
            self.state = "ready"
            self.y = 1000

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))

class Enemy():
    def __init__(self):
        self.x = 800
        self.y = random.randint(0, 550)
        self.dx = random.randint(10, 50) / -10
        self.surface = pygame.image.load('enemy.png')
        self.health = random.randint(5, 15)

    def move(self):
        self.x = self.x + self.dx
        
        # Border check
        if self.x < 0:
            self.x = random.randint(800, 900)
            self.y = random.randint(0, 550)        

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))

class Star():
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 550)
        self.dx = random.randint(10, 50) / -30
        images = ["yellow_star.png", "red_star.png", "white_star.png"]
        self.surface = pygame.image.load(random.choice(images))

    def move(self):
        self.x = self.x + self.dx
        
        # Border check
        if self.x < 0:
            self.x = random.randint(800, 900)
            self.y = random.randint(0, 550)        

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def render(self):
        screen.blit(self.surface, (int(self.x), int(self.y)))


# Create sounds
missile_sound = pygame.mixer.Sound("missile.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

# Create font
font = pygame.font.SysFont("comicsansms", 24)

# Create objects        
player = Player()
missiles = [Missile(), Missile(), Missile()]

enemies = []
for _ in range(5):
    enemies.append(Enemy())
    
stars = []
for _ in range(30):
    stars.append(Star())

def fire_missile():
    # Is the missile ready
    for missile in missiles:
        if missile.state == "ready":
            missile.fire()
            missile_sound.play()
            break

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
            
        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_SPACE:
                fire_missile()

    # Update objects
    player.move()
    
    for missile in missiles:
        missile.move()
    
    for star in stars:
        star.move()
    
    for enemy in enemies:
        enemy.move()

        # Check for collision
        for missile in missiles:
            if enemy.distance(missile) < 20:
                enemy.health -= 4
                if enemy.health <= 0:
                    explosion_sound.play()
                    enemy.x = random.randint(800, 900)
                    enemy.y = random.randint(0, 550)
                else:
                    enemy.x += 20

                # Reset missile
                missile.dx = 0
                missile.x = 0
                missile.y = 1000
                missile.state = "ready"
                
                # Add to score
                player.score += 10
        
        # Check for collision
        if enemy.distance(player) < 20:
            explosion_sound.play()
            print("Game over!")
            pygame.quit()
            exit()    

    # Render (Draw stuff)
    # Fill the background color
    screen.fill(BLACK)
     
    # Render stars
    for star in stars:
        star.render()
    
    # Render objects
    player.render()
    
    for missile in missiles: 
        missile.render()
    
    for enemy in enemies:
        enemy.render()  

    # Ammo counter
    ammo = 0
    for missile in missiles:
        if missile.state == "ready":
            ammo += 1
    
    for x in range(ammo):
        screen.blit(missile.surface, (700 + 30 * x, 20))
    
    # Render the score
    score_surface = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_surface, (400, 20))
    
    pygame.display.flip()
    
    clock.tick(30)
