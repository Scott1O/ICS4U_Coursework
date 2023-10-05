# Scott O'Hara
# Date: 10-04-2023
# 04C Practice Question 9

# input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# processings
common_factors = []

for divider in range(1, max(num1,num2)):
    if num1 % divider == 0 and num2 % divider == 0:
        common_factors.append(divider)
# end of for loop

# output
print(f"The common factors of {num1} and {num2} are:")
for runs in range(len(common_factors)):
    print(common_factors[runs])