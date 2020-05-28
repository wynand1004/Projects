# ChristianThompson.com
# @TokyoEdTech
# Lesson 11: Classes

from animal import Animal

print("Animals (Three Different Ones)")

lucky = Animal("Lucky")
gizmo = Animal("Gizmo")
bella = Animal("Bella")

lucky.set_weight(20.5);
gizmo.set_weight(6.2);
bella.set_weight(5.1);

print("\nNumber of Animals: {}".format(Animal.number_of_animals))

print(lucky)
print(gizmo)
print(bella)

Animal.increment_number_of_animals()
print("\nNumber of Animals: {}".format(Animal.number_of_animals))
