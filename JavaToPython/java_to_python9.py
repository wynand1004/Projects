# ChristianThompson.com
# @TokyoEdTech
# Lesson 9: Functions/Methods

# Define function
def print_pi():
    print(3.14159)

def print_double(x):
    print(x * 2)

def get_pi():
    return 3.14159

def get_double(x):
    return x * 2

def get_greatest(x, y):
    if x > y:
        return x
    else:
        return y

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Call functions
print_pi()
print_double(2)

pi = get_pi()
print(pi)

y = get_double(4)
print(y)

greatest = get_greatest(42, 16)
print(greatest)

if is_even(42):
    print("Even!")
else:
    print("Odd!")









