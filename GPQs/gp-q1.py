# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

factors = {2:1, 3:1, 5:1, 7:1, 11:1, 13:1, 17:1, 19:1}

for i in range(4,21):
    tmp = i
    for key, value in factors.items():
        if tmp == 1:
            break
        ctr = 0
        while tmp != 1 and tmp % key == 0:
            if value == 0:
                tmp //= key
                ctr += 1
            else:
                tmp //= key
                value -= 1
        factors[key] += ctr

print(factors)
answer = 1
for key, value in factors.items():
    answer *= key ** value 

print(answer)
