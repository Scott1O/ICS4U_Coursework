# Scott O'Hara
# Date: 10-26-2023
# 05B Pratice Question 19

import random

def collatz(start):
    full_list = [0 for i in range(start+1)]
    full_list[0] = -1
    working_num = start
    steps = 0
    while 0 in full_list:
        working_num = random.randrange(2,start+1)
        
        steps = 0
        while working_num != 1 and full_list[working_num] == 0:
            if working_num % 2 == 0:
                working_num = (working_num * 3) + 1
                steps += 1
            else:
                working_num //= 2
                steps += 1
    
    end_result = [max(full_list), full_list.find(max(full_list))]
    return end_result


