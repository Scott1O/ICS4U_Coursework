# Scott O'Hara
# Date: 09-27-2023
# 03B Practice Question 7

# input
month = int(input("Enter the numerical month: "))
day = int(input("Enter the numerical day of the month: "))

# processing and output
if month > 12 or month < 1:
    print("This is not a month")
elif day > 31 or day < 1:
    print("This is not a day")
else: 
    if month == 2:
        if day == 18:
            print("Special")
        elif day < 18:
            print("Before")
        else: 
            print("After")
    elif month > 2:
        print("After")
    else: 
        print("Before")