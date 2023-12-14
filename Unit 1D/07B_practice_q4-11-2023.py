def string_reversal(text, index = 0):
    rev_text = ""
    if index == -(len(text)):
        return text[-len(text)]
    else:
        rev_text = string_reversal(text,index-1)
        return rev_text

print(string_reversal("Hello"))