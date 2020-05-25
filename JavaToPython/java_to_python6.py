# ChristianThompson.com
# @TokyoEdTech
# Lesson 6: Loops

for x in range(0, 10):
    print(x)

print()
for x in range(0, 10, 2):
    print(x)

for x in range(10, -1, -1):
    print(x)

print()
title = "Pictures of You"
for i in range(0, len(title)):
    print(title[i])

for letter in title:
    print(letter, end='')

i = 0
while(i < len(title)):
    print(title[i], end='')
    i += 1

