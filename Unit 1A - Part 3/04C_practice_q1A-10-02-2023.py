# Scott O'Hara
# Date: 10-02-2023
# 04C Practice Problem 1 For Loop

# input
num = int(input("What number do you want to see the factorial of?: "))

# processing 
for i in range(num - 1, 1, -1):
    num *= i

# output
print(num)