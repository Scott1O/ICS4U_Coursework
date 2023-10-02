# Scott O'Hara
# Date: 09-21-2023
# 02A Practice Question 6

# input
length1 = len(input("Input the length of section one by using F: "))
length2 = len(input("Input the length of section two by using F: "))
length3 = len(input("Input the length of section three by using F: "))

# processing
total_cans = length1 + length2 + length3
cans_left = total_cans % 12

if cans_left == 0:
    dozens_bought = total_cans / 12
else:
    dozens_bought = (total_cans // 12) + 1

total_cost = round((dozens_bought * 14.95),2)

# output
print(f"You need {total_cans} cans with {dozens_bought} dozens bought for ${total_cost} with {cans_left} cans left")
