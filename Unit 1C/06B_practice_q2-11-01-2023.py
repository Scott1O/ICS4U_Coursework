def unique_chars(word_list):
    unique_char_set = set()
    for word in word_list:
        for char in word:
            unique_char_set.add(char)
    return unique_char_set

print(unique_chars(["apple", "banana", "cherry", "date"]))