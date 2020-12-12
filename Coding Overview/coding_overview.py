# How Do I Learn To Code?
# with examples in Python 3.x
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdTech

# Blog: https://www.christianthompson.com
# YouTube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg/

# Topics: Data and Data Types, Input, Output, Control Structures
# Functions, Data Structures, Classes and Objects
# Terminal, Graphics, and GUI
# Algorithms and Complexity

# 16-Bit Member Shoutouts: Kevin, Paul, and Jan

import os
os.system("clear")

# Variables and Data Types
print("Variables and Data Types")
the_answer = 42
gigawatts = 1.21
name = "Prince"
is_sleepy = True

# Input / Output
print("\n\nInput and Output")
print(f"The answer to Life, the Universe, and Everything is {the_answer}.")
guess = input("Please guess my favorite color. > ")
print("You guessed: " + guess)

delay = input("Press ENTER to continue.")

# Control Structures
print("\n\nControl Structures")
# Conditionals
print("Conditionals")
if guess == "green":
    print("Yes, that is correct")
elif guess == "black":
    print("Close...")
else:
    print("Wrong!")

delay = input("Press ENTER to continue.")

# Loops
print("\n\nLoops")
print("for loop")
for x in range(0, 5):
    print(f"5 x {x} = {5 * x}")

print("while loop")
x = 5
while x > 0:
    print(f"10 x {x} = {10 * x}")
    x -= 1

delay = input("Press ENTER to continue.")

# Functions
print("\n\nFunctions")
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

print(is_even(42))
print(is_even(43))

delay = input("Press ENTER to continue.")

# Data Structures
print("\n\nData Structures")
# Lists
print("Lists")
names = ["Greg", "Grant", "Bob"]
print(names)
print(names[1])
# Dictionaries
print("Dictionaries")
capitals = {"Japan":"Tokyo", "South Korea":"Seoul", "Romania":"Bucharest"}
print(capitals)
print(capitals["Japan"])

delay = input("Press ENTER to continue.")

# Classes and Objects
print("\n\nClasses and Objects")
class Dog():
    def __init__(self, name):
        self.name = name
        print(f"Dog {self.name} created.")
        
    def bark(self):
        print(f"{self.name} says 'woof'!")
        
lucky = Dog("Lucky")
bella = Dog("Bella")

lucky.bark()
bella.bark()

delay = input("Press ENTER to continue.")

# Terminal Graphics and GUI

# Algorithms and Complexity
print("\n\nAlgorithms and Complexity")
print(names)
print(f"Bob index: {names.index('Bob')}")
names.sort()
print(names)
print(f"Bob index: {names.index('Bob')}")

# And Beyond

print("\nTHE END")
