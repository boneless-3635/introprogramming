name_file = input("Please enter the file name: ")
fr = open(name_file, "r")
f_new = name_file + "_new"
fw = open(f_new, "w")

lines = fr.readlines()
count = 1
for i in lines:
    fw.write(str(count) + " " + i)
    count += 1

fw.close()
fr.close()
