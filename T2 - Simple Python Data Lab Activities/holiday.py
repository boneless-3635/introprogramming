daysDict = {
  0: "Sunday",
  1: "Monday",
  2: "Tuesday",
  3: "Wednesday",
  4: "Thursday",
  5: "Friday",
  6: "Saturday"
}

startDate = int(input("Enter your starting day number: "))
lengthDate = int(input("Enter length of stay in days: "))

print("The day you will return is:", daysDict[(startDate + lengthDate) % 7])
