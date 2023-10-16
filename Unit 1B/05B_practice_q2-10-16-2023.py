# Scott O'Hara
# Date: 10-16-2023
# 05B Practice Question 2

def palindrome_checker(user_input):
    '''
    checks if an inputted string is a palindrome or not
    argument:
        user_input: takes the users input, string
    
    return:
        True or False whether or not the input is a palindrome
    '''
    reversed_input = ""
    for letter in reversed(user_input):
        reversed_input += letter
    palindrome = bool(user_input == reversed_input)

    return palindrome
# end of function

word = input("Enter a word: ")
print(f"Your word, {word}, is a palindrome: {palindrome_checker(word)}")