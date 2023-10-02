# Scott O'Hara
# Date: 09-25-2023
# 03B Practice Question 2

counter = 1
wins = 0
losses = 0

# input and processing
while counter <= 6:
    result = input("What was the result of the game?: ")

    if result == "W" or result == "Win":
        wins += 1
    else:
        losses += 1
    
    counter += 1

# output and processing
if wins >= 5:
    print("You are in Group 1")
elif wins == 3 or wins == 4:
    print("You are in Group 2")
elif wins == 1 or wins == 2:
    print("You are in Group 3")
else:
    print("You are elminated from the tournament")