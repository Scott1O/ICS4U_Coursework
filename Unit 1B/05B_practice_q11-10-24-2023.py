# Scott O'Hara
# Date: 10-24-2023
# 05B Practice Question 11

def factor_finder(num):
    factor_list = []
    for divider in range (1, num+1):
        if num % divider == 0:
            factor_list.append(divider)
    
    return factor_list

def prime_checker(num):
    if factor_finder(num) == [1, num]:
        return True
    else:
        return False

num = int(input("Enter a number to check it's factors: "))
print(factor_finder(num))
print(f"Prime: {prime_checker(num)}")