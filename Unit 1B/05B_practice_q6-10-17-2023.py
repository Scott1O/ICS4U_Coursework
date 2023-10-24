# Scott O'Hara
# Date: 10-17-2023
# 05B Practice Question 6

def dupe_finder(word1, word2):
    common_list = []
    
    for character in word1:
        if character in word2 and character not in common_list:
            common_list.append(character)
    
    return sorted(common_list)
# end of function

input1 = input("Enter a word: ")
input2 = input("Enter another word: ")

print(f"The common characters of \"{input1}\" and \"{input2}\" are {dupe_finder(input1,input2)}")
