#program that invoke square root function after specific milliseconds

import math
import time

def square_num(number, miliseconds):
    time.sleep(miliseconds / 1000)
    nn = math.sqrt(number)
    return nn

n_square = int(input())
n_time = int(input())
result = square_num(n_square, n_time)
print("Square root of 25100 after 2123 miliseconds is", result)


