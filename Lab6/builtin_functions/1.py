#program with builtin function to multiply all the numbers in a list

import math

def multiply_list(numbers):
    return math.prod(numbers)

nums = [1, 2, 5]
result = multiply_list(nums)
print(result)
