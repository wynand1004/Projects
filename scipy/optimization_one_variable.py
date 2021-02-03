# scipy Optimization with .minimize
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import scipy.optimize as spo

# Function to minimize
def f(x):
    y = (x**2) - (12 * x) + 20
    return y
    
# Starting guess
x_start = 2.0

# optimizing
result = spo.minimize(f, x_start, options={"disp": True})

# Print result
if result.success:
    print("Success!")
    print(f"x = {result.x} y = {result.fun}")
else:
    print("Sorry, could not find a minimum.")
