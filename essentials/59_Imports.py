

import calendar   # import an existing or built-in module
import random as rand   # give an alias to the imported module
from math import pi    # import specific member from a module

# from math import *   # import all members from a module --> not suggested

from math import sin, cos   # import multiple members from a module

print("calendar.isleap(2024) : ", calendar.isleap(2024))

print()

# access the module members using the alias
print("rand.randint(0, 10) : ", rand.randint(1,10))

print()

# access the imported member directly without using module name
print("pi : ", pi)



