# Scott O'Hara
# Date: 10-24-2023
# 05B Practice Question 14

palindrome_list = []

for num1 in range (999, 99, -1):
    for num2 in range (999, 99, -1):
        if str(num1*num2) == str(num1*num2)[::-1]:
            palindrome_list.append(num1*num2)

print(max(palindrome_list))