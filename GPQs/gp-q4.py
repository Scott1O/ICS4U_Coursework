def odd_freq_finder(num_list):
    num_set = set(num_list)
    for num in num_set:
        if num_list.count(num) % 2 == 1:
            return num
    return "No odd numbers"

print(odd_freq_finder([7]))
print(odd_freq_finder([0]))
print(odd_freq_finder([1,1,2]))
print(odd_freq_finder([0,1,0,1,0]))
print(odd_freq_finder([1,2,2,3,3,3,4,3,3,3,2,2,1]))