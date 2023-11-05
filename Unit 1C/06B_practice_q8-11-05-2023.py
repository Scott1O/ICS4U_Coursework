def char_freq(text):
    text = text.lower()
    freq_dict = {}
    for item in text:
        freq_dict[item] = text.count(item)

    return freq_dict

print(char_freq("helLo"))