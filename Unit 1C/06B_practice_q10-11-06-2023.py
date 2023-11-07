def fib_dict(num):
    fib_nums = {0:0, 1:1}
    for i in range (2, num+1):
        fib_nums[i] = fib_nums[i-1] + fib_nums[i-2]

    return fib_nums

print(fib_dict(10))