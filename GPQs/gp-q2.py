from math import sqrt

def proper_factors(num):
    factors = {1}
    factor_cap = int(sqrt(num)) + 1
    for i in range(2,factor_cap):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)

    return factors

amicable_nums = set()
for l in range(1,10001):
    tmp = sum(proper_factors(l))
    if l == sum(proper_factors(tmp)) and l != tmp:
        amicable_nums.add(l)
        amicable_nums.add(tmp)

print(amicable_nums)
print(sum(amicable_nums))