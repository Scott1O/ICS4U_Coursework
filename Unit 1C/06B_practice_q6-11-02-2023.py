def dict_filter(input_dict, target=0):
    filtered_dict = {}
    for key, value in input_dict.items():
        if value >= target:
            filtered_dict[key] = value
    return filtered_dict

print(dict_filter({'a': 10, 'b': 5, 'c': 20, 'd': 15}, 10))