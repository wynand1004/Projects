# Platformer Coding using Pygame
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import pygame
import sys
import math
import random

pygame.init()
pygame.display.set_caption("Platformer Demo! by @TokyoEdtech")
clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800
GRAVITY = 1

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
        self.friction = 0.8
        
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

class Player(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self, x, y, width, height)
        self.color = GREEN
    
    def left(self):
        self.dx -= 6
        if self.dx < -12:
            self.dx = -12
    
    def right(self):
        self.dx += 6
        if self.dx > 12:
            self.dx = 12
    
    def jump(self):
        self.dy -= 24
    
    def move(self):
        self.x = self.x + self.dx
        self.y += self.dy
        self.dy += GRAVITY

# Create font

# Create sounds

# Create game objects
player = Player(600, 0, 20, 40)
blocks = [Sprite(600, 200, 400, 20), Sprite(600, 400, 600, 20), Sprite(600, 600, 1000, 20), Sprite(1000, 500, 100, 200), Sprite(200, 500, 100, 200)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_SPACE:
                for block in blocks:
                    if player.is_aabb_collision(block):
                        player.jump()
                        break

    # Move/Update objects
    player.move()

    # Check for collisions
    for block in blocks:
        if player.is_aabb_collision(block):
            # Player is to the left
            if player.x < block.x - block.width/2.0 and player.dx > 0:
                player.dx = 0
                player.x = block.x - block.width/2.0 - player.width/2.0
            # Player is to the right
            elif player.x > block.x + block.width/2.0 and player.dx < 0:
                player.dx = 0
                player.x = block.x + block.width/2.0 + player.width/2.0
            # Player is above
            elif player.y < block.y:
                player.dy = 0
                player.y = block.y - block.height/2.0 - player.height/2.0 + 1
                player.dx *= block.friction
            #Player is below
            elif player.y > block.y:
                player.dy = 0
                player.y = block.y + block.height/2.0 + player.height/2.0
                player.dx *= block.friction


    # Border check the player
    if player.y > 800:
        player.goto(600, 0)
        
    # Render (Draw stuff)
    # Fill the background color
    screen.fill(BLACK)
    
    # Render objects
    player.render()
    
    for block in blocks:
        block.render()
     
    # Flip the display
    pygame.display.flip()
    
    # Set the FPS
    clock.tick(30)
