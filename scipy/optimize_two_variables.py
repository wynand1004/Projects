# scipy Optimization with .minimize
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

import scipy.optimize as spo

# Function to maximize
def f(xy):
    x = xy[0]
    y = xy[1]
    area = x * y
    return -area
    
# Starting guess
xy_start = [50, 50]

# Bounds
bnds = ((1, 100), (1, 100))

# Constraints
cons =({'type':'eq', 'fun': lambda xy: (2*xy[0]) + xy[1] - 100})

# Optimizing
result = spo.minimize(f, xy_start, options={"disp": True}, constraints=cons, bounds=bnds)

# Print result
if result.success:
    print("Success!")
    xy = result.x
    x = xy[0]
    y = xy[1]
    print(f"x = {x} y = {y}")
else:
    print("Sorry, could not find a minimum.")
