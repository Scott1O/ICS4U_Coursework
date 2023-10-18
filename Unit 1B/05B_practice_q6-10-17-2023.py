# Scott O'Hara
# Date: 10-17-2023
# 05B Practice Question 6

def dupe_finder(word1, word2):
    common_list = []
    smaller = ""
    bigger = ""

    if len(word1) > len(word2):
        smaller = word2
        bigger = word1
    else:
        smaller = word1
        bigger = word2
    
    for i in range(len(smaller)):
        if smaller[i] in bigger and smaller[i] not in common_list:
            common_list.append(smaller[i])
    
    return sorted(common_list)
# end of function

input1 = input("Enter a word: ")
input2 = input("Enter another word: ")

print(f"The common characters of \"{input1}\" and \"{input2}\" are {dupe_finder(input1,input2)}")
