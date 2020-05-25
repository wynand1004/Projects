# ChristianThompson.com
# @TokyoEdTech
# Lesson 7: Lists

scores = []

scores.append(85)
scores.append(90)
scores.append(100)

print()
for i in range(0, len(scores)):
    print("Score {}: {}".format(i, scores[i]))

average_score = (scores[0] + scores[1] + scores[2]) / 3.0
print("Average Score: {}".format(average_score))

heights = [150, 160, 170, 180, 190]

print()
for i in range(0, len(heights)):
    print("Height {}: {}".format(i, heights[i]))

for height in heights:
    print(height)

total = 0
for height in heights:
    total += height
average_height = total/len(heights)
print("Average Height: {}".format(average_height))

stuff = [0, 2.2, "Bob", True]
for thing in stuff:
    print(thing)

