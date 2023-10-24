# Scott O'Hara
# Date: 10-24-2023
# 05B Practice Question 13

def string_compressor(text):
    ''' compress a string to show the character and the number of times it appears in
        the string

        arguments:
            text: a string
        
        return:
            a compressed list with the character and the number of times it appears or the
            original string if the compressed list is longer than the original
    '''

    compressed_string = ""
    ctr = 1
    for i in range(len(text)):
        if i < len(text) - 1:
            if text[i] == text[i+1]:
                ctr += 1
            else:
                compressed_string += text[i] + str(ctr)
                ctr = 1
        else:
                compressed_string += text[i] + str(ctr)
    
    if len(compressed_string) >= len(text):
        return text
    else:
        return compressed_string
# end of function

input_text = input("Enter a string of text: ")
print(string_compressor(input_text))