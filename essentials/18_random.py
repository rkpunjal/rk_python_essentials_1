# # import the library 'random'
# import random
#
# # calling method from the library   --> library.methodName()
# print(random.randint(2,10))
#


# import the method from a library
from random import randint

print("randint(2,10) : ", randint(2,10))

print()
print("Toss Coin using randint(0,1) : ")
print("----------------------------------")
coin_value = randint(0,1)

if coin_value == 0:
    print("HEAD")
else:
    print("TAILS")
