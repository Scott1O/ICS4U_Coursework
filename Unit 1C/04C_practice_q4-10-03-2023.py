# Scott O'Hara
# Date: 10-03-2023
# 04C Practice Question 4

# processing
total_sum = 0
factor_sum = 0
for num in range (1,10001):
    for i in range(1, num):
        if num % i == 0:
            factor_sum += i

    if num == factor_sum:
        print(factor_sum)
        total_sum += factor_sum

    factor_sum = 0

# output
print(f"The sum of all perfect numbers from 1 to 10,000 is {total_sum}")
