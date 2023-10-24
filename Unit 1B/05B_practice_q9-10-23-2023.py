# Scott O'Hara
# Date: 10-18-2023
# 05B Practice Question 9
from random import randrange

def rand_range(start, end, frequency):
    random_list = []
    for i in range(frequency):
        random_list.append(randrange(start, end+1))
    return random_list

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
frequency = int(input("Enter the number of random numbers you want: "))

print(f"Your random list of integers is {rand_range(start, end, frequency)}.")