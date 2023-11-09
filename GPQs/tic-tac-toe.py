def board(pos_dict):
    l = 0
    for i in range(1,4):
        print("| --- | --- | --- |")
        print(f"|  {pos_dict[i+l]}  |  {pos_dict[i+l+1]}  |  {pos_dict[i+l+2]}  |")
        l += 2
    print("| --- | --- | --- |")

pos_dict = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
ctr = 1
x_spots = set()
o_spots = set()
x_win = False
o_win = False
win_con = [{1,2,3}, {1,4,7}, {1,5,9}, {2,5,8}, {3,6,9}, {3,5,7}, {4,5,6}, {7,8,9}]
while not x_win and not o_win and ctr < 10:
    board(pos_dict)
    if ctr % 2 == 1:
        print("X's turn. Enter a position to play in: ")
        place = int(input())
        if pos_dict[place] != "X" and pos_dict[place] != "O":
            pos_dict[place] = "X"
            x_spots.add(place)
            ctr += 1
        else:
            print("Invalid spot. Please try again.")
    else:
        print("O's turn. Enter a position to play in: ")
        place = int(input())
        if pos_dict[place] != "X" and pos_dict[place] != "O":
            pos_dict[place] = "O"
            o_spots.add(place)
            ctr += 1
        else:
            print("Invalid spot. Please try again.")

    for win in win_con:
        if win <= x_spots:
            print("X's have won.")
            x_win = True
        elif win <= o_spots:
            print("O's have won.")
            o_win = True

if not x_win and not o_win:
    print("Neither player has won")