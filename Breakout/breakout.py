# Breakout Live Coding using Pygame
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

# Snake Shoutouts: Kevin & Paul
# Invader Shoutouts: Jan, Mohd, Kim-Siong, and Finnesz

import pygame
import sys
import math
import random

pygame.init()
pygame.display.set_caption("Breakout! by @TokyoEdtech")
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
class Paddle():
    def __init__(self):
        self.x = WIDTH/2.0
        self.y = 700
        self.dx = 0
        self.width = 200
        self.height = 25
        self.score = 0

    def left(self):
        self.dx = -12
    
    def right(self):
        self.dx = 12
    
    def move(self):
        self.x = self.x + self.dx
        
        # Check for border collision
        if self.x < 0 + self.width/2.0:
            self.x = 0 + self.width/2.0
            self.dx = 0
        
        elif self.x > WIDTH - self.width/2.0:
            self.x = WIDTH - self.width/2.0
            self.dx = 0
        
    def render(self):
        pygame.draw.rect(screen, WHITE, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 

class Ball():
    def __init__(self):
        self.x = WIDTH/2.0
        self.y = HEIGHT/2.0
        self.dx = 6
        self.dy = -6
        self.width = 20
        self.height = 20
    
    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        
        # Check for border collision
        if self.x < 0 + self.width/2.0:
            self.x = 0 + self.width/2.0
            self.dx *= -1
        
        elif self.x > WIDTH - self.width/2.0:
            self.x = WIDTH - self.width/2.0
            self.dx *= -1
            
        if self.y < 0 + self.height/2.0:
            self.y = 0 + self.height/2.0
            self.dy *= -1
        
        elif self.y > HEIGHT - self.height/2.0:
            self.y = HEIGHT - self.height/2.0
            self.x = WIDTH / 2.0
            self.y = HEIGHT / 2.0
            
        
    def render(self):
        pygame.draw.rect(screen, WHITE, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 

    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)

class Brick():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 25
        self.color = random.choice([WHITE, GREEN, RED, BLUE])
        
    def render(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(int(self.x-self.width/2.0), int(self.y-self.height/2.0), self.width, self.height)) 

# Create font
font = pygame.font.SysFont("comicsansms", 48)

# Create sounds
bounce_sound = pygame.mixer.Sound("bounce.wav")

# Create game objects
paddle = Paddle()
ball = Ball()

bricks = []
for y in range(100, 375, 25):
    color = random.choice([WHITE, RED, GREEN, BLUE])
    for x in range(25, 1200, 50):
        bricks.append(Brick(x, y))
        bricks[-1].color = color

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.left()
            elif event.key == pygame.K_RIGHT:
                paddle.right()

    # Update objects
    paddle.move()
    ball.move()
    
    # Check for collisions
    if ball.is_aabb_collision(paddle):
        ball.dy *= -1
        bounce_sound.play()
    
    
    dead_bricks = []
    for brick in bricks:
        if ball.is_aabb_collision(brick):
            ball.dy *= -1
            dead_bricks.append(brick)
            paddle.score += 10
            bounce_sound.play()
            
    for brick in dead_bricks:
        bricks.remove(brick)
        
    if len(bricks) <= 0:
        print("GAME OVER")
        

    # Render (Draw stuff)
    # Fill the background color
    screen.fill(BLACK)
    
    # Render objects
    paddle.render()
    ball.render()
    
    for brick in bricks:
        brick.render()
     
    # Render the score
    # Render the score
    score_surface = font.render(f"Score: {paddle.score}", True, WHITE)
    screen.blit(score_surface, (WIDTH/2.0 - 75, 20))
    
    # Flip the display
    pygame.display.flip()
    
    # Set the FPS
    clock.tick(30)
