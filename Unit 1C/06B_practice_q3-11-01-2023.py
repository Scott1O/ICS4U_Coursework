def common_num(set_list):
    common_set = set_list[1]
    for a_set in set_list:
        common_set = common_set & a_set

    return len(common_set)

print(common_num([ {1, 2, 3, 4, 5}, {3, 4, 5, 6, 7},{5, 6, 7, 8, 9} ]))