# ChristianThompson.com
# @TokyoEdTech
# Lesson 5: Conditionals

print("Does 3 equal 3?")
if 3 == 3:
    print(True)

print()
x = 3
y = 2
print("Is {} greater than {}?".format(x, y))
if x > y:
    print(True)
else:
    print(False)

print()
x = 2
y = 3
print("Is {} greater than {}?".format(x, y))
if x > y:
    print(True)
else:
    print(False)

print()
player_a = "rock"
player_b = "rock"

if player_a == "rock" or player_b == "rock":
   print("Someone chose rock!") 

if player_a == "rock" and player_b == "scissors":
    print("Player A wins!")
elif player_a == "rock" and player_b == "paper":
    print("Player B wins!")
else:
    print("Tie!")


