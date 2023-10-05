# Scott O'Hara
# Date: 09-26-2023
# 03B Practice Question 6

# input
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))

# processing and output
if (angle1+angle2+angle3) != 180:
    print("Error, not a triangle")
else: 
    if angle1 == angle2 == angle3:
        print("Equilateral triangle")
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        print("Isosceles triangle")
    else:
        print("Scalene Triangle")
