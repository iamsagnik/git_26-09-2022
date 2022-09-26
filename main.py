import math

print("Hare Krishna !")

def circumf(r):
    return (math.pi * r * 2)

def area(r):
    return (math.pi * r * r)


r = float(input("Enter radius :"))
print("C = ", circumf(r))
print("Area =", area(r))



