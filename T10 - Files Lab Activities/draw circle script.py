name_file = input("Please input a file name: ")
f = open(name_file+".py", "w")
f.write("import turtle\n\n\nt = turtle.Turtle()\nr = 20\nt.circle(r)\n")
f.close()