# Scott O'Hara
# Date: 10-18-2023
# 05B Practice Question 8

def csv_to_list(num_csv):
    csv_split = list(map(int,num_csv.split(",")))

    return csv_split

data = input("Enter a list of numbers: ")
print(csv_to_list(data))