def word_length(string_list):
    word_dict = {}
    for word in string_list:
        word_dict[word] = len(word)

    return word_dict

print(word_length(["apple", "banana", "cherry", "date"]))