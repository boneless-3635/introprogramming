def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        print("It is a leap year")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("It is a leap year")
    else:
        print("It is not a leap year")


leap_year(int(input("Input year: ")))
