# Scott O'Hara
# Date: 09-25-2023
# 03B Practice Question 3

# input
player_1_input = input("What is Player 1's move?: ")
player_2_input = input("What is Player 2's move?: ")

# processing and output
if player_1_input == player_2_input:
    print("Tie game.")
elif player_1_input == "Rock":
    if player_2_input == "Paper":
        print("Player 2 Wins.")
    elif player_2_input == "Scissors":
        print("Player 1 Wins.")
elif player_1_input == "Paper":
    if player_2_input == "Scissors":
        print("Player 2 Wins.")
    elif player_2_input == "Rock":
        print("Player 1 Wins.")
elif player_1_input == "Scissors":
    if player_2_input == "Rock":
        print("Player 2 Wins.")
    elif player_2_input == "Paper":
        print("Player 1 Wins.")
else:
    print("One or more players had an invalid input.")
