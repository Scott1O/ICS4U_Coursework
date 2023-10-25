# Scott O'Hara
# Date: 10-25-2023
# 05B Practice Question 16

from myFunctions import prime_checker

def primes_under_n(num):
    primes = []
    for i in range(2,num):
        if prime_checker(i):
            primes.append(i)
    
    return primes

num_n = int(input("Enter a number: "))
print(primes_under_n(num_n))