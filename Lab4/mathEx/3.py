import math

def area_of_regularpolygon(numsides, length):
    #formula: (n * s^2) / (4 * tan(π/n))
    area = (numsides * (length**2)) / (4 * math.tan(math.pi / numsides))
    return area 

numsides = int(input())
length = float(input())
area = area_of_regularpolygon(numsides, length)
print(f"{area:.0f}")
