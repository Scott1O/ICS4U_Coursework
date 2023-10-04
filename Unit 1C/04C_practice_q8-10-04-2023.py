# Scott O'Hara
# Date: 10-04-2023
# 04C Practice Question 8

# input 
inputting = True
longest_name = [""]
long_name_len = 0

while inputting:
    name = input("Enter a name or \"X\" to exit: ")
    if name == "X":
        break
    elif len(name) >= long_name_len:
        if len(longest_name[0]) < len(name):
            longest_name = []
            longest_name.append(name)
            long_name_len = len(name)
            # Clearing list if the name is shorter
        else:
            longest_name.append(name)
            long_name_len = len(name)
            print(len(name))
            # adding to the list with the longer name
# end of while loop

# output
if long_name_len == 0:
    print("You did not enter any names.")
else:
    print("The longest name(s) are:")
    for long_name in range(len(longest_name)):
        print(f"{longest_name[long_name]} with {long_name_len} characters")