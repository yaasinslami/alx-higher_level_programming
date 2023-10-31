#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_ch = str(number)[-1]
last_ch_int = int(last_ch)

if (last_ch_int > 5):
    print(f"Last digit of {number} is {last_ch_int} and is greater than 5")
elif (last_ch_int < 6 and last_ch_int != 0):
    print(f"Last digit of {number} is {last_ch_int} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_ch_int} and is 0")
