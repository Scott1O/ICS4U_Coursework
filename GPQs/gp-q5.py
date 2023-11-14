def zeros_to_end(a_list):
    zeros_list = []
    for element in a_list:
        tmp = str(element)
        if tmp == '0':
            zeros_list.append(element)
            a_list.remove(element)
    
    return a_list + zeros_list

print(zeros_to_end([1,0,1,2,0,1,3,"a"]))