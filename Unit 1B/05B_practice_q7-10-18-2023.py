# Scott O'Hara
# Date: 10-18-2023
# 05B Practice Question 7

def mean(data_list):
    ''' find the mean of a list

    argument:
        data_list: a list of number inputs, list

    return:
        the mean of the list
    '''

    return sum(data_list) / len(data_list)

def median(data_list):
    ''' find the median of a list

    argument:
        data_list: a list of number inputs, list
    
    return:
        the median of the list
    '''

    data_list = sorted(data_list)

    if len(data_list) % 2 == 1:
        return data_list[len(data_list)//2]
    else:
        return (data_list[len(data_list)//2] + data_list[len(data_list)//2 + 1]) / 2

print(median([98,100,95,88,17,100]))