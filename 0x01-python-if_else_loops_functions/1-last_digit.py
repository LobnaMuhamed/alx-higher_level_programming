#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
if number < 0:
    l_digit = (number * -1) % 10
    l_digit *= -1
else:
    l_digit = number % 10
if l_digit > 5:
    print(f"{str1} {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"{str1} {number} is {l_digit} and is 0")
elif l_digit < 6 and not 0:
    print(f"{str1} {number} is {l_digit} and is less than 6 and not 0")
