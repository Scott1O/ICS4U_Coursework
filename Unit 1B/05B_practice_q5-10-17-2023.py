# Scott O'Hara
# Date: 10-17-2023
# 05B Practice Question 5

def anagram_checker(word1, word2):
    ''' checks if the two strings are anagrams

    arguments: 
        word1: the first word to compare, string
        word2: the second word to compare, string
    
    return:
        True of False depending on whether or not it's an anagram
    '''

    anagram = False

    if sorted(word1) == sorted(word2):
        anagram = True
    
    return anagram
# end of function

input1 = input("Enter a word: ")
input2 = input("Enter another word: ")

print(f"{input1} and {input2} are anagrams: {anagram_checker(input1,input2)}")