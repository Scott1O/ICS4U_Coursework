def dict_combine(dict1, dict2):
    new_dict = {}
    for key, value in dict1.items():
        if key in dict2 and key not in new_dict:
            larger = max(dict1[key], dict2[key])
            new_dict[key] = larger
        else:
            new_dict[key] = value
    
    for key, value in dict2.items():
        if key not in new_dict:
            new_dict[key] = value
    
    return new_dict

print(dict_combine({'a': 1, 'b': 2, 'c': 100}, {'b': 3, 'c': 4}))