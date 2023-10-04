# Scott O'Hara 
# Date: 10-03-2023
# 04C Practice Question 6

# input
invalid = True
while invalid:
    nth_fib = int(input("Enter the Nth fibonacci number you want to find: "))
    if nth_fib >= 0:
        invalid = False
# end of input while loop

# processing
fib_num = 1
fib_prev = 0

for runs in range (1, nth_fib+1):
    # fibonacci increasing
    fib_num += fib_prev
    fib_prev = fib_num - fib_prev

# output
print(fib_prev)