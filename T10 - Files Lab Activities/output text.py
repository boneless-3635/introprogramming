# 1.
msg = input("Input message pls: ")
f = open("message.txt", "w")
for i in range(100):
    f.write(msg+"\n")
f.close()
