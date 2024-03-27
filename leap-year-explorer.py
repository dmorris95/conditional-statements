#Task 1

year = int(input("Please input a year: "))
leap_year = False

if year % 4 == 0:
    if year % 100 != 0:
        leap_year = True
    elif year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

if leap_year == False:
    print("The year you input is not a leap year.")
else:
    print("The year you input is a leap year.")