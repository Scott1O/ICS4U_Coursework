# Scott O'Hara
# Date: 10-25-2023
# 05B Practice Question 17

def scrabble_word(word):
    score = 0
    word = word.upper()
    for character in word:
        if character in "EAIONRTLSU":
            score += 1
        elif character in "DG":
            score += 2
        elif character in "BCMP":
            score += 3
        elif character in "FHVWY":
            score += 4
        elif character in "K":
            score += 5
        elif character in "JX":
            score += 8
        elif character in "QZ":
            score += 10
    # end of for loop
    return score

def scrabble_list(text_list):
    highest_score = ["", 0]
    for item in text_list:
        word_score = scrabble_word(item)
        if word_score > highest_score[1]:
            highest_score[0] = item
            highest_score[1] = word_score
    # end of for loop
    return highest_score

input_list = input("Enter a list of words seperated by only a comma: ")
input_list = list(map(str,input_list.split(",")))

print(f"The highest scoring word and it's score is: {scrabble_list(input_list)}")