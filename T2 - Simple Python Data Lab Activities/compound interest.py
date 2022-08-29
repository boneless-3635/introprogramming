pAmount = float(input("Enter the Principal amount: "))
years = int(input("Enter the number of years: "))

n = 12
r = 0.08

finalAmount = pAmount * ((1 + (r/n)) ** (n*years))

print("Your final amount is:", round(finalAmount, 2))