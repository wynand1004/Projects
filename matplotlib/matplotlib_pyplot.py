# Getting Started with matplotlib.pyplot
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

# pip3 install matplotlib

import matplotlib.pyplot as plt

temperatures = [7, 8, 12, 15, 10, 9, 9]
labels = ["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]

plt.plot(labels, temperatures, "o:g", label = "Tokyo Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature C.")
plt.ylim([0, 50])
plt.legend()

plt.savefig("figure1.png")
plt.show()
