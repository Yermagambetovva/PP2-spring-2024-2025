from math import pi

def volumeOfSphere(R):
    return round(4/3 * pi * (R**3), 3)  # Округляет число x до 3 знаков после запятой  

print(volumeOfSphere(int(input('enter a radius: '))))