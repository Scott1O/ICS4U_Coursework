# Scott O'Hara
# Date: 10-25-2023
# 05B Practice Question 15

def gcd(num1, num2):
    common_factors = []
    for i in range(1, min(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
    
    return max(common_factors)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(gcd(num1,num2))