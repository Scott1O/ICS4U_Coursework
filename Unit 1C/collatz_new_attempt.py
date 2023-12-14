# THE ISSUE WAS WITH SETTING SIZE TO len(sequence) BEFORE THE FINAL FOR LOOP

def next_num(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num*3 + 1

def seq_maker(start, a_dict):
    if start in a_dict:
        return a_dict[start]
    else:
        sequence = [start]
        size = 1

        while sequence[-1] != 1:

            new_num = next_num(sequence[-1])

            if new_num in a_dict:
                size += a_dict[new_num]
                break
            else:
                sequence.append(new_num)
                size += 1

        for i in range(len(sequence)):
            a_dict[sequence[i]] = size - i

        return size

num_max = 0
max_key = 0
collatz_dict = {}
for L in range(1,1000001):
    new_size = seq_maker(L, collatz_dict)

for key, value in collatz_dict.items():
    if value > num_max:
        num_max = value
        max_key = key

print(f"Highest collatz sequence is {num_max} starting at {max_key}")