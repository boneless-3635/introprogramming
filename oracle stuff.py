array = input("Array: ")
list_int = [str(x) for x in array.split(",")]

for i in list_int:
    print("\'"+i+"\'", end=",")
