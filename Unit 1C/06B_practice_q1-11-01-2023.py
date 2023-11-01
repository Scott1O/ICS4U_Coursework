def dupe_remover_list(a_list):
    clean_list = []
    for item in a_list:
        if item not in clean_list:
            clean_list.append(item)

    return clean_list

def dupe_remover_set(a_list):
    clean_list = list(set(a_list))
    return clean_list

print(dupe_remover_list([1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4]))
print(dupe_remover_set([1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4]))