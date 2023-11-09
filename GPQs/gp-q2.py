def factors(num):
    factors_list = []
    for i in range (1,num):
        if num % i == 0:
            factors_list.append(i)

    return factors_list

amicable_pairs = {}
for i in range(1, 10001):
    for l in range(1,10001):
        suml = sum(factors(l))
        sumi = sum(factors(i))
        if sumi == suml:
            amicable_pairs[i] = l 

print(amicable_pairs)