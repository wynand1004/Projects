# I am making a similar game except 
# I want when the key is held, the character should immediately 
# go to left/right. For some reason, the character does not move at all

# Debugging by @TokyoEdTech
# Original comment on my YouTube channel here:
# https://www.youtube.com/watch?v=g3EA-QMZ-dM&list=PLlEgNdBJEO-kqEqgLXTVLloAFemDusfPK

import turtle
import random
import math
import time
numofapples = 20

wn = turtle.Screen()

wn.bgcolor("white")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)

wn.register_shape("head",((-30,0),(-30,30),(-20,0),(20,0),(30,30),(30,0),(20,-20),(-20,-20)))

border = turtle.Turtle()
border.ht()
border.speed(0)
border.color("black")
border.pu()
border.goto(-300,300)
border.pd()

for i in range(4):
    border.fd(600)
    border.rt(90)
border.pu()
border.ht()

class Sprite(turtle.Turtle):
    def __init__( self ,spriteshape,color,startx,starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx,starty)
        self.speed= 1
        
    def collision(t1,t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        
        if distance < 30:
            return True
        else:
            return False
            
    def catch(head,apple):
        if apple.ycor()<-220 and apple.ycor()>-250 and apple.xcor()>head.xcor()-30 and apple.xcor()<head.xcor()+30:
            return True
        else:
            return False
        
class P1(Sprite):
    def __init__(  self ,spriteshape,color,startx,starty):
        Sprite.__init__( self ,spriteshape,color,startx,starty)
        self.pu()
        self.setheading(90)
        self.leftt = False
        self.rightt = False
        self.color(color)
        self.goto(startx,starty)
        self.speed= 10
    
    def left(self):
        self.leftt = True
	
    def right(self):
        self.rightt = True
			
    def lefty(self):
        self.leftt = False
    
    def righty(self):
        self.rightt = False
        
    def move(self):
        x = self.xcor()
		
        if self.leftt==True:
            x-=5
            self.setposition(x,self.ycor())
            # Check for left border
            if self.xcor()<-250:
                self.setx(-250)	
                
        if self.rightt==True:
            x+=5
            self.setposition(x,self.ycor())
            # Check for right border
            if self.xcor()>250:
                self.setx(250)	
        
class Apple(Sprite):
     def __init__(self,spriteshape,color,startx,starty):
        Sprite.__init__(self,spriteshape,color,startx,starty)
        self.pu()
        self.color(color)
        self.goto(startx,starty)
        self.speed= 3
        
     def move(self):
        self.setheading(270)
        self.fd(self.speed)
        if self.ycor()<-300:
            self.setposition(random.randint(-250,250),random.randint(350,1000))
        if Sprite.catch(p1, apple):
            self.setposition(random.randint(-250,250),random.randint(350,1000))
        
apples = []
for i in range(numofapples):
    apples.append(Apple("circle","red",random.randint(-250,250),random.randint(350,1000)))
    
p1 = P1("head","brown",0,-250)

turtle.listen()
turtle.onkeypress(p1.left,"Left")
turtle.onkeypress(p1.right,"Right")
turtle.onkeyrelease(p1.lefty,"Left")
turtle.onkeyrelease(p1.righty,"Right")

while True:
    turtle.update()
    
    for apple in apples:
        apple.move()
    
    p1.move()
