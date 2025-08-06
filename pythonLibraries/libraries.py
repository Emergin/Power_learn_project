# a python library is a collection of pre-written code 
# that you can use to perform common tasks without having to write everything from scratch
# 1 built in libraries

import math 
print(math.sqrt(16))
print(math.pi)

# 2 importing part of a library
print("square root of 36", math.sqrt(36))
print("sine of 90 degrees", math.sin(math.radians(90)))
print("power of 2^3", math.pow(2, 3))

# 3 random 
import random
print('random number between 1 and 10', random.randint(1, 10))
print('random choice from a list: ', random.choice(['apples', 'banana', 'oranges']))

# 4 datetime  work with dates and time 
import datetime
today = datetime.date.today()
print('todays date is: ', today)
now = datetime.datetime.now()
print('current time: ', now)



