# Scott O'Hara
# Date: 10-02-2023
# 04C Practice Question 0

# processing and output
num = 1
while num <= 50:
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else: 
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    num += 1


