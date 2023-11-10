def factors(num):
    factors_list = []
    for i in range (1,num):
        if num % i == 0:
            factors_list.append(i)

    return factors_list

amicable_pairs = {}
for i in range(2, 10001):
    for l in range(2,10001):
        suml = sum(factors(l))
        sumi = sum(factors(i))
        if sumi == l and suml == i and i != l and (i not in amicable_pairs and l not in amicable_pairs):
            amicable_pairs[i] = l 

print(amicable_pairs)
print((sum(amicable_pairs.values()) + sum(amicable_pairs.keys())))