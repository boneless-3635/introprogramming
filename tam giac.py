triSide1 = input("Input the first triangle side: ")
triSide2 = input("Input the second triangle side: ")
triSide3 = input("Input the third triangle side: ")
if triSide1 == triSide2 == triSide3:
    print("This is an equilateral triangle.")
elif triSide1 != triSide2 != triSide3:
    print("This is a scalene triangle.")
else:
    print("This is an isoceles triangle")