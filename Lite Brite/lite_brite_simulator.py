# Lite-Brite Simulator
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech
import turtle

WIDTH = 820
HEIGHT = 140

wn = turtle.Screen()
wn.title("Lite-Brite Simulator by @TokyoEdtech")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)

color_codes = {
    "r":"red",
    "o":"orange",
    "y":"yellow",
    "g":"green",
    "b":"blue",
    "v":"purple",
    "w":"white",
    "p":"pink",
    " ":"black"
}

pen = turtle.Turtle()
pen.penup()
pen.color("black")
pen.shape("circle")

def draw_circle(x, y, pen):
    screen_x = -(WIDTH/2.0) + 20 + x * 20
    screen_y = (HEIGHT/2.0) - 20 - y * 20
    pen.goto(screen_x, screen_y)
    pen.stamp()

picture = [
"r   ooo yyy bbb     gg  ppp ooo yyy bbb",
"r    o   y  b       g g p p  o   y  b",
"r    o   y  bb  www gg  ppp  o   y  bb",
"r    o   y  b       g g pp   o   y  b",
"rrr ooo  y  bbb     gg  p p ooo  y  bbb",
]

# Draw picture
for y in range(len(picture)):
    row = picture[y]
    for x in range(len(row)):
        color = picture[y][x]
        pen.color(color_codes[color])
        draw_circle(x, y, pen)
    
wn.mainloop()
