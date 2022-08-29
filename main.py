import math

radiusIntegrity = False
radius = input("Please input the circle radius: ")

while not radiusIntegrity:
    try:
        flRadius = float(radius)
        radiusIntegrity = True
    except ValueError:
        print("That's not a number")
        break

circumference = round(flRadius*2*math.pi, 2)
area = round(pow(flRadius, 2)*math.pi, 2)

print("Circumference is :", circumference)
print("Area is", area)