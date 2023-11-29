#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Digit = abs(number) % 10
if number < 0 and Digit !=0:
    Digit = -Digit
print(f"Last digit of {number} is {Digit}", end=" ")
if Digit == 0:
    print("and is 0")
elif Digit > 5:
    print("and is greater than 5")
elif Digit < 6:
    print("and is less than 6 and not 0")
