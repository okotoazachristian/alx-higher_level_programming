#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Digit = abs(number) % 10
if Digit == 0:
    print(f"Last digit of {number} is {Digit} and is 0")
elif Digit < 6 or number < 0:
    if number < 0:
        Digit = -Digit
        print(f"Last digit of {number} is {Digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {Digit} and is less than 6 and not 0")
elif last_Digit > 5:
    print(f"Last digit of {number} is {Digit} and is greater than 5")
