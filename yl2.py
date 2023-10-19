import math

radius = float(input("Sisesta raadius: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Ringi raadius:", area)
print("Ringi ümbermõõt:", circumference)