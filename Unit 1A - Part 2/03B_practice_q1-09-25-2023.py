# Scott O'Hara 
# Date: 09-25-2023
# 03B Practice Question 1

# input
num = int(input("Enter a non-negative number: "))

# processing and output
if ((num+2) % 10) == 0 or ((num-2) % 10) == 0:
    print("Your number is 2 away from a multiple of 10")
else: 
    print("Your number is not 2 away from a multiple of 10")