# Scott O'Hara
# Date: 10-02-2023
# 04C Practice Question 3

# input
num = 0
while num < 1:
    num = int(input("What number do you want to check if it's prime?: "))

# processing
factors = []
for i in range(num-1, 1, -1):
    if num % i == 0:
        factors.append(i)

# output
if factors:
    print("Your number is not prime and its factors are:")
    print(1)
    for i in sorted(factors):
        print(i)
    print(num)
else:
    print("Your number is prime")