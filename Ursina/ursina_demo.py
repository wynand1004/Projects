# Ursina 3D Python Game Engine
# with examples in Python 3.x
# Windows, Mac, and Linux Compatible
# by @TokyoEdTech

# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/

# Topics: Installing and Figuring Out the Ursina 3D Python Game Engine

# 16-Bit Member Shoutouts: Kevin, Paul, Jan, and Mohd!

from ursina import *
import random

app = Ursina()

spheres = []

GRAVITY = -0.01

for _ in range(25):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sphere = Entity(model='sphere', color = color.rgb(r, g, b))
        
    sphere.x = random.randint(-7, 7)
    sphere.y = random.randint(0, 5)
    sphere.z = random.randint(-8, 8)
    sphere.dx = random.randint(1, 10) / 100
    sphere.dy = random.randint(1, 10) / 100
    sphere.dz = random.randint(1, 10) / 100
    
    spheres.append(sphere)

def update():   # update gets automatically called.
    for sphere in spheres:
        sphere.dy += GRAVITY
        sphere.x += sphere.dx
        sphere.y += sphere.dy
        sphere.z += sphere.dz
        
        if sphere.x > 7:
            sphere.x = 7
            sphere.dx *= -1
        if sphere.x < -7:
            sphere.x = -7
            sphere.dx *= -1
            
        if sphere.y < -4:
            sphere.y = -4
            sphere.dy *= -1

        if sphere.z > 16:
            sphere.z = 16
            sphere.dz *= -1
        if sphere.z < -8:
            sphere.z = -8
            sphere.dz *= -1
        
        sphere.rotation_y += 2
        sphere.rotation_x += 2
        sphere.rotation_z += 2
        
    # Collision checking
    for i in range(len(spheres)):
        for j in range(i+1, len(spheres)):
            sphere1 = spheres[i]
            sphere2 = spheres[j]
            x = sphere1.x - sphere2.x
            y = sphere1.y - sphere2.y
            z = sphere1.z - sphere2.z
            d = ((x**2) + (y**2) + (z**2)) ** 0.5
            if d < 1:
                sphere1.dx, sphere2.dx = sphere2.dx, sphere1.dx
                sphere1.dy, sphere2.dy = sphere2.dy, sphere1.dy
                sphere1.dz, sphere2.dz = sphere2.dz, sphere1.dz
                
app.run()   # opens a window and starts the game.
