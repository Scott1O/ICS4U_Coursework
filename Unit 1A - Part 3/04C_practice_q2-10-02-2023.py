# Scott O'Hara
# Date: 10-02-2023
# 04C Practice Question 2

# input
num = int(input("What number do you want to find factors of?: "))
factors = []

# processing
for i in range(num, 0, -1):
    if num % i == 0:
        factors.append(i)

# output
for i in sorted(factors):
    print(i)