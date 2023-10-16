# Scott O'Hara
# Date: 10-16-2023
# 05B Practice Question 3

def consonant_counter(user_input, consonants = True):
    '''
    counts the number of consonants or vowels in a given user input

    arguments:
        user_input: the string that the function checks, string
        consonants: optional input to count vowels instead of consonants, boolean

    return:
        the number of consonants or vowels in the user's input
    '''
    consonant_count = 0
    vowel_count = 0
    for i in range(len(user_input)):
        if user_input[i].isalpha():
            if user_input[i] in "aeiou":
                vowel_count += 1
            else:
                consonant_count += 1
    # end of for loop
    final_count = 0

    if consonants:
        final_count = consonant_count
    else:
        final_count = vowel_count

    return final_count
# end of function

user_input = input("Enter a string: ")
cons_or_vowel = input("Enter \"True\" for consonants or \"False\" for vowels: ")

if cons_or_vowel == "False":
    cons_or_vowel = False
else:
    cons_or_vowel = True

if cons_or_vowel:
    print(f"The number of consonants in your string is {consonant_counter(user_input, cons_or_vowel)}")
else: 
    print(f"The number of vowels in your string is {consonant_counter(user_input, cons_or_vowel)}")
