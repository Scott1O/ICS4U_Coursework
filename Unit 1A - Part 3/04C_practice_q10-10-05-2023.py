# Scott O'Hara 
# Date: 10-05-2023
# 04C Practice Question 10

# input
num = int(input("Enter a number to find it's prime factors: "))
largest = 1
num_holder = num

# processing
if num % 2 == 0:
    largest = 2
    # while loop to divide by 2 as many times
    while num % 2 == 0:
        num //= 2
# end of while loop - number should now be odd

factor = 3
while num != 1:
    if num % factor == 0:
        num //= factor
        largest = factor
    else:
        factor += 2
# end of while loop

# output
print(f"The largest prime factor of {num_holder} is {largest}.")