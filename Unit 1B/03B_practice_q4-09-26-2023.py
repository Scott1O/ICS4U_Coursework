# Scott O'Hara
# Date: 09-26-2023
# 03B Practice Question 4

# input
phone_number = input("Enter the last four numbers: ")

# processing and output
if (phone_number[0] == 8 or phone_number[0] == 9) and (phone_number[3] == 8 or phone_number[3] == 9) and (phone_number[1] == phone_number[2]):
    print("Ignore the call")
else:
    print("The call is safe")