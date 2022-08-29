
#hang man project

word = input("Enter your word: ").lower()
list = list(word)
list2 = []
list3 = [None]
counter=0
wrongCounter=0
maxWrong=10
repitition=False

for i in range (len(list)):
    if list[i] == " ":
        list2.append(" ")
        counter+=1
    else:
        list2.append("_")

print(*list2, sep=" ")
print("You have", len(list) - counter,"characters to guess")

while counter <= len(list):
    guess = input("\nEnter a character: ").lower()
    status=False
    statusMessage=False
    if len(guess)==1:
        for j in range (len(list3)):
            if list3[j] == guess:
                print("You can't enter the same character again\n")
                statusMessage=True
                repitition=True
                break
        for i in range (len(list)):
            if list[i] == guess:
                list2[i] = guess
                list3.append(guess)
                status=True
                if repitition == False:
                    counter+=1

        if status==False:
            if wrongCounter==maxWrong:
                print("You lost!!!!!!11!1")
                break
            else:
                print("Your guess is wrong, try again")
                wrongCounter += 1
                print("You have", maxWrong-wrongCounter, "tries left\n")
                statusMessage=True

        else:
            print("Please enter only 1 character")

        print (*list2, sep=" ")

        if list == list2:
            print("You have found the word")
            break
        elif statusMessage==False:
           print("You have", len(list) - counter,"characters left")


