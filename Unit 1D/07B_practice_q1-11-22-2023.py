def factorial(num):
    if num == 0:
        return 0
    elif num == 1:
        return num
    else:
        return num * factorial(num-1)

print(factorial(999))