# Scott O'Hara
# Date: 10-02-2023
# 04C Practice Problem 1 While Loop

# input
num = int(input("What number do you want to see the factorial of?: "))
i = num - 1

# processing
while i > 0:
    num *= i
    i -= 1

# output
print(num)