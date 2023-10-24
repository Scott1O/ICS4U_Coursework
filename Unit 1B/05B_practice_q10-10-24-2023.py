# Scott O'Hara
# Date: 10-24-2023
# 05B Practice Question 10

def dupe_remover(letter_list):
    clean_list = []

    for letter in letter_list:
        if letter not in clean_list:
            clean_list.append(letter)
    
    return clean_list

print(dupe_remover(["a", "b", "c", "c", "b", "c", "a", "a", "d"]))