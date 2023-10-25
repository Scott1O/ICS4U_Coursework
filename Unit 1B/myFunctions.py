def factor_finder(num):
    ''' return the factors of a number

    argument:
        num: a number to find factors of, int

    return:
        a list of factors for the number
    '''
    factor_list = []
    for divider in range (1, num+1):
        if num % divider == 0:
            factor_list.append(divider)
    
    return factor_list

def prime_checker(num):
    ''' checks if the input if prime or not

    argument:
        num: a number to check whether or not its prime, int

    return: 
        true or false whether it's prime or not
    '''
    if factor_finder(num) == [1, num]:
        return True
    else:
        return False