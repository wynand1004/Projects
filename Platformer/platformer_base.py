# Platformer Game Intro Using Pygame
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import pygame
import sys
import math
import random

pygame.init()
pygame.display.set_caption("Platformer Game Intro by @TokyoEdtech")
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create classes
class Sprite():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height
        self.color = WHITE
        self.friction = 0.9
        
    def goto(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 

    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

# Create font

# Create sounds

# Create game objects

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_SPACE:
                pass

    # Move/Update objects

    # Check for collisions

    # Border check the player
        
    # Render (Draw stuff)
    # Fill the background color
    screen.fill(BLACK)
    
    # Render objects
     
    # Flip the display
    pygame.display.flip()
    
    # Set the FPS
    clock.tick(30)
