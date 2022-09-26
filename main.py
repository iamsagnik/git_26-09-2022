import math

print("Hello World !")

def circumf(r):
    p = math.pi
    c = 2 * p * r
    return c

def area(r):
    p = math.pi
    area = p * r * r
    return area


r = float(input("Enter radius :"))
print("C = ", circumf(r))
print("Area =", area(r))



