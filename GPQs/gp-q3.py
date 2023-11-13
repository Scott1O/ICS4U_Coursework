def word_spin(text):
    text_split = text.split(" ")
    spun_text = ""
    for word in text_split:
        if len(word) >= 5:
            word = word[::-1]
        spun_text += f"{word} "
    return spun_text

print(word_spin("This is another test"))