# ChristianThompson.com
# @TokyoEdTech
# Lesson 8: Dictionaries

capitals = {}

capitals["Japan"] = "Tokyo"
capitals["China"] = "Beijing"
capitals["South Korea"] = "Seoul"

capital = capitals["Japan"]
print("Japan: {}".format(capital))

print()
country = "South Korea"

if country in capitals:
    capital = capitals[country]
    print("{}: {}".format(country, capital))
else:
    print("Sorry, that country does not exist.")

print()
for key in capitals:
    value = capitals[key]
    print("{}: {}".format(key, value))





