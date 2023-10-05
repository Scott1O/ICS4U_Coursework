# Scott O'Hara
# Date: 10-04-2023
# 04C Practice Question 7

# input
inputting = True
all_grades = []

while inputting:
    grade = input("Enter a mark or type \"Exit\" to stop: ")
    if grade == "Exit":
        break
    grade = int(grade)
    if grade > 100 or grade < 0:
        print("Please enter a mark between 0 and 100")
        continue
    else:
        all_grades.append(grade)
# end of while loop

# processing
grade_sum = 0
average = 0
divider = 0

for divider, adding_grade in enumerate(all_grades):
    grade_sum += adding_grade
# end of for loop

average = grade_sum / (divider+1)
average = round(average)

# output
print(f"The average for your grades is {average}")