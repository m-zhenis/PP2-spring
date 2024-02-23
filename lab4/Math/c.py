import math
n = int(input("Input number of sides:"))
s = int(input("Input the length of a side:"))
v = (n*s**2)/(4*math.tan(math.pi/n))
print("The area of the polygon is:",int(v))