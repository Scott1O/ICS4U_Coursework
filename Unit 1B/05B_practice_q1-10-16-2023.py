# Scott O'Hara
# Date: 10-16-2023
# 05B Practice Question 1

def stringcleaner (unclean_string):
    ''' 
    removes non-alphabetical characters from an unclean string and returns
    it as a lowercase version of the clean string
    argument:
        unclean_string: takes the unclean string from the user input, string
    return:
        a clean string
    '''
    clean_string = unclean_string.lower()

    for i in range(0,10):
        clean_string = clean_string.replace(str(i), "")

        l = 0
    while l <= len(clean_string):
        if not clean_string[l].isalpha():
            clean_string = clean_string.replace(clean_string[l], "")
        l += 1

    return clean_string
# end of function

unclean_string = input("Enter a string: ")

print(f"The cleaned string is {stringcleaner(unclean_string)}")