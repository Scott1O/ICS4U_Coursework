def rgb_to_hex(rgb1, rgb2, rgb3):
    rgb_list = [rgb1, rgb2, rgb3]
    hex_value = ""
    for rgb in rgb_list:
        if rgb > 255:
            hex_value += "FF"
            continue
        elif rgb < 0:
            hex_value += "00"
        tmp = [rgb//16, rgb%16]
        for num in tmp:
            if num <= 9:
                hex_value += str(num)
            elif num == 10:
                hex_value += "A"
            elif num == 11:
                hex_value += "B"
            elif num == 12:
                hex_value += "C"
            elif num == 13:
                hex_value += "D"
            elif num == 14:
                hex_value += "E"
            else:
                hex_value += "F"
    return hex_value

print(rgb_to_hex(255, 255, 255))
print(rgb_to_hex(255, 255, 300))
print(rgb_to_hex(0, 0, 0))
print(rgb_to_hex(148, 0, 211))

