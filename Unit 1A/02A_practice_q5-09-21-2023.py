# Scott O'Hara
# Date: 09-21-2023
# 02A Practice Question 4

import random

# input
difficulty_class = int(input("Enter the difficulty class: "))

# processing
d20 = random.randrange(1,21)

# output
if d20 >= difficulty_class:
    print(f"You rolled a {d20} and your action succeeded")
else:
    print(f"You rolled a {d20} and your action failed")