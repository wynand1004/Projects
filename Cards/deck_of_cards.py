# Deck of Cards Simulator (Live Coding)
# Create a simple deck of cards and draw them on the screen
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Deck of Cards Simulator by @TokyoEdtech")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


# Create classes
class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
        
    def print_card(self):
        print(f"{self.name}{self.symbols[self.suit]}")
        
    def render(self, x, y, pen):
        # Draw border
        pen.penup()
        pen.goto(x, y)
        pen.color("blue")
        pen.goto(x-50, y+75)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x+50, y+75)
        pen.goto(x+50, y-75)
        pen.goto(x-50, y-75)
        pen.goto(x-50, y+75)
        pen.end_fill()
        pen.penup()
        
        if self.name != "":
            # Draw suit in the middle
            pen.color("white")
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            
            # Draw top left 
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            
class Deck():
    def __init__(self):
        self.cards = []
        
        names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")
        
        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        card = self.cards.pop()
        return card
        
    def reset(self):
        self.cards = []
        
        names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
        suits = ("D", "C", "H", "S")
        
        for name in names:
            for suit in suits:
                card = Card(name, suit)
                self.cards.append(card)
        
        self.shuffle()
        
# Create deck                
deck = Deck()

# Shuffle deck
deck.reset()

# Render 5 cards (back) in a row
start_x = -250
for x in range(5):
    card = Card("", "")
    card.render(start_x + x * 125, 0, pen)

time.sleep(5)

# Render 5 cards in a row
start_x = -250
for x in range(5):
    card = deck.get_card()
    card.render(start_x + x * 125, 0, pen)

wn.mainloop()
