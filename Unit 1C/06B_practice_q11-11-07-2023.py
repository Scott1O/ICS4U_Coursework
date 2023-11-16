# DP: Dynamic Programming
# Memoization

def next_value(num):
    if num % 2 == 0:
        return num//2
    else:
        return num*3 + 1

def sequence_maker(start, table):
    if start in table:
        return table[start]
    else:
        sequence = [start]
        size = 1

        while sequence[-1] != 1 and sequence[-1] not in table:
            new_num = next_value(sequence[-1])
            if new_num in table:
                size += table[new_num]
                break
            else:
                sequence.append(new_num)
                size += 1
    
    for i in range(len(sequence)):
        table[sequence[i]] = size - i

    return size

starting_table = {1:1, 2:2}
print(sequence_maker(13, starting_table))

for i in range(3,1000001):
    sequence_maker(i, starting_table)

answer = 0
steps = 0
for key, value in starting_table.items():
    if value > steps:
        answer = key
        steps = value

print(f"Largest size: {steps} for number {answer}")