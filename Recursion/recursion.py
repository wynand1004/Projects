# Intro to Recursion
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

# Channel Members
# Snake Shoutouts: Kevin, Paul, & Jan
# Invader Shoutouts: Mohd, Kim-Siong, Finnesz, Peter, Uli, Bogdan, Ezra, and Erik

# Countdown Loop
print("Countdown Loop")
x = 10
while x >= 0:
    print(x)
    x -= 1

# Recursion
print("\n\nCountdown Recursion")
def countdown(x):
    # Base case
    if x < 0:
        return None
    else:
        print(x)
        countdown(x-1)

countdown(10)

print("\n\nLinear Search with a Loop")
# Linear Search
scores = [12, 22, 24, 35, 36, 47, 48, 50, 51, 53, 64, 65, 76, 77, 84, 86, 93, 95, 97]

target_score = 50

for index in range(0, len(scores)):
    if scores[index]== target_score:
        print(index)
        break

# Recursive Linear Search
print("\n\nRecursive Linear Search")
def linear_search(index, items, target):
    # Base case
    if index == len(items):
        return None
    elif items[index] == target:
        return index
    else:
        return linear_search(index+1, items, target)
        
print(linear_search(0, scores, target_score))

print("\n\nRecursion Limit")
import sys
print(sys.getrecursionlimit())
