# Scott O'Hara
# Date: 10-26-2023
# 05B Practice Question 18

def possible_sum(int_list, target):
    for num in int_list[::-1]:
        if num > target:
            continue
        else: 
            for rev_num in range(1,num):
                if num + rev_num == target and rev_num in int_list:
                    return True
    
    return False


print(possible_sum([1, 3, 5, 9, 11, 13, 22], 13))