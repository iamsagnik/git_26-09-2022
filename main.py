import math

print("Hello World !")

def circumf(r):
    p = math.pi
    c = 2 * p * r
    return c

r = float(input("Enter radius :"))
print("C = ", circumf(r))



