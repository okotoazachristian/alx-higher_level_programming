#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_Digit = abs(number) % 10
if last_Digit == 0:
    print(f"Last digit of {number} is {last_Digit} and is 0")
elif last_Digit < 6 or number < 0:
    if number < 0:
        last_Digit = -last_Digit
        print(f"Last digit of {number} is {last_Digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last_Digit} and is less than 6 and not 0")
elif last_Digit > 5:
    print(f"Last digit of {number} is {last_Digit} and is greater than 5")
