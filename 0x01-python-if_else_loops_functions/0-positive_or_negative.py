#!/usr/bin/python3
import random

number = random.randint(-50, 50)
print("The number is:", number)
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
