import math

radiusCheck = False

while not radiusCheck:
    try:
        radius = float(input("Please enter the circle radius: "))
        radiusCheck = True
        area = radius ** 2 * math.pi
        print("The area of your circle is:", round(area, 2))
    except ValueError:
        print("Number is invalid")