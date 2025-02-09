import math 

def area_of_trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input())
base2 = float(input())
height = float(input())
area = float(area_of_trapezoid(base1, base2, height))
print(area)