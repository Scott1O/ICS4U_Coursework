def palindrome(text, index = 0):
    if index > len(text)//2:
        return True
    elif text[index] != text[-(index+1)]:
        return False
    else:
        return palindrome(text, index+1)

print(palindrome('tacocat'))