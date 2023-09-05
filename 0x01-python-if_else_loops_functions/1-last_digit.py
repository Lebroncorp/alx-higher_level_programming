#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10 * (1 if number > 0 else -1)

print(f"Last digit of {number} is", end=' ')
if a > 5:
    print(f"{a} and is greater than 5")
elif a == 0:
    print(f"{a} and is 0")
else:
    print(f"{a} and is less than 6 and not 0")
