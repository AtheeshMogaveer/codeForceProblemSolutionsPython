import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
pointer = 1

for _ in range(t):
    keyboard = input_data[pointer]
    word = input_data[pointer + 1]
    pointer += 2
    
    pos = {char: i for i, char in enumerate(keyboard)}
    
    total_time = 0
    for j in range(1, len(word)):
        current_pos = pos[word[j]]
        previous_pos = pos[word[j-1]]
        total_time += abs(current_pos - previous_pos)
        
    print(total_time)