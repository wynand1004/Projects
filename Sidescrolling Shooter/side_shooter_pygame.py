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
    
    def fire(self):
        self.x = player.x + 25
        self.y = player.y + 16
        self.dx = 10
    
    def move(self):
        self.x = self.x + self.dx 

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

# Create objects        
player = Player()
missile = Missile()

enemies = []
for _ in range(5):
    enemies.append(Enemy())

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
                missile.fire()

    # Update objects
    player.move()
    missile.move()
    
    for enemy in enemies:
        enemy.move()

        # Check for collision
        if enemy.distance(missile) < 20:
            enemy.x = random.randint(800, 900)
            enemy.y = random.randint(0, 550)
            missile.dx = 0
            missile.x = 0
            missile.y = 1000
        
        # Check for collision
        if enemy.distance(player) < 20:
            print("Game over!")
            pygame.quit()
            exit()    

    # Render (Draw stuff)
    # Fill the background color
    screen.fill(BLACK)
    
    # Render objects
    player.render()
    missile.render()
    for enemy in enemies:
        enemy.render()  
    
    pygame.display.flip()
    
    clock.tick(30)
