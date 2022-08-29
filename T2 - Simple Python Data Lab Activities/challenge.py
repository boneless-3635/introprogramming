number = list()
counter = [0]*100       # list for storing the steps
sameSteps = list()

for N in range(1, 101):     # go from 1 to 100
    number.append(N)        # number from 1 to 100 is put in a list
    x = N       # placeholder number for calculating
    step = 0       # steps start at 0

    if N == 1:      # number 1 has no steps
        step = 0

    while x != 1:       # prevent x from getting to 1
        if x % 2 == 0:      # even number check
            x = int(x / 2)      # perform calculation
            step += 1       # increase step after calculation
        else:
            x = 3 * x + 1       # perform calculation
            step += 1       # increase step after calculation
    counter[N - 1] = step      # record number of steps

largestStep = counter[0]        # largest step starts at beginning


for i in range(100):
    print(number[i], "\t\t", counter[i], "\n")      # print all the number and its steps
    if counter[i] > largestStep:        # finding the largest step
        largestStep = counter[i]
        largestStepNum = number[i]

    if number[i] == counter[i]:     # finding the number that is the same as its step
        sameSteps.append(number[i])

print("The number that takes the largest steps to reach 1 is:", largestStepNum, "at", largestStep)
print("Numbers that have the same number as the steps are:", sameSteps)

