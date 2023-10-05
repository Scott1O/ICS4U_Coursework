# Scott O'Hara
# Date: 09-26-2023
# 03B Practice Question 5

# input
x_coord = int(input("What is the x-coordinate?: "))
y_coord = int(input("What is the y-coordinate?: "))

# processing and output
if x_coord > 0:
    if y_coord > 0:
       print("The point is in quadrant 1")
    else:
        print("The point is in quadrant 4")
else:
    if y_coord > 0:
        print("The point is in quadrant 2")
    else:
        print("The point is in quadrant 3")
