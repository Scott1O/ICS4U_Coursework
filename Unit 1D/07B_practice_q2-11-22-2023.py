def exponention(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * (exponention(base, exponent-1))

print(exponention(2,4))
# non tail recursion ^

# tail recursion
# tails means an extra argument that you don't actually need
def tail_exponention(base, exponent, answer = 1):
    if exponent == 0:
        return answer
    else:
        return tail_exponention(base, exponent-1, answer * base)

print(tail_exponention(3,4))

# why is a tail recursion alogirthm faster than a non-tail recursion algorithm
# because it does not have to do the math and remember the calculation every time

# it is true that bubble, insertion, selection sort are at worst case N^2
# which of them is the best at their best or average case scenario

