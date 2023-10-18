# Scott O'Hara
# Date: 10-17-2023
# 05B Practice Question 4

def binary_pattern(num):
    ''' creates a pattern of 1's and 0's based on user input

    argument: 
        num: the N num to determine pattern length, int

    return:
        a pattern of 1010...
    '''

    pattern = ""

    for i in range(1, num+1):
        if i % 2 == 1:
            pattern += "1"
        else:
            pattern += "0"
        
        print(pattern)
# end of function

user_input = int(input("Enter a number: "))

binary_pattern(user_input)