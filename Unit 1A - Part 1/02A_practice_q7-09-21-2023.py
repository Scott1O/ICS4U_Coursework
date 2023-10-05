# Scott O'Hara
# Date: 09-21-2023
# 02A Practice Question 7

# input
money_start = float(input("How much money do we have before selling cookies?: "))
cookies_bought = input("How many cookies were sold? Type 'c' for a normal cookie and 'b' for a big cookie: ")

# processing
cookies = cookies_bought.count("c")
big_cookies = cookies_bought.count("b")

profit = round((1.25*cookies - 0.5*cookies) + (2*big_cookies - 0.75*big_cookies),2)

money_after = round((money_start + profit),2)

# output
print(f"You sold {cookies+big_cookies} cookies, made ${profit} in profit and now have ${money_after}")