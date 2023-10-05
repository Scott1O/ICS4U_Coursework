# Scott O'Hara
# Date: 09-20-2023
# 02A Practice Question 2

# input
cost = float(input("Enter the total cost of the service: "))
tip = int(input("What percent do you want to tip: "))

# processing
final_price = cost * (1+(tip/100))

# output
print(f"The total price is ${final_price}")