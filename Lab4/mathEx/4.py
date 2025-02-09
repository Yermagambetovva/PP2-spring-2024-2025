import math

def area_of_parallelogram(length, height):
    #formula: base length * height
    area = length * height
    return area

length = float(input())
height = float(input())
area = area_of_parallelogram(length, height)
print(area)