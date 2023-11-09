# DP: Dynamic Programming
# Memoization

def next_value(num):
    if num % 2 == 0:
        return num//2
    else:
        return num*3 + 1

        

