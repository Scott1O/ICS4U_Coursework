def key_swapper(input_dict):
    new_dict = {}
    for key, value in input_dict.items():
        new_dict[value] = key
    return new_dict

print(key_swapper({'a': 1, 'b': 2, 'c': 3})) 
