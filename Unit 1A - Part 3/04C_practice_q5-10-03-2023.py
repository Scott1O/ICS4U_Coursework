# Scott O'Hara
# Date: 10-03-2023
# 04C Practice Question 5

# input
num = int(input("Enter a number greater than 1: "))

# processing
highest_factors = 0
num_max_factors = 0
factors = 0

for i in range (1,num+1):
    for l in range (1,i+1):
        if i % l == 0:
            factors += 1
    if factors > highest_factors:
        highest_factors = factors
        num_max_factors = i
    factors = 0

# output
print(f"The number {num_max_factors} has the most factors at {highest_factors} factors")