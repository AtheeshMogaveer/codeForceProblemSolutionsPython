import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])

for i in range(1, t + 1):
    s = input_data[i]
    
    first_one = s.find('1')
    last_one = s.rfind('1')
    
    if first_one == -1:
        print(0)
        continue
        
    zeros_to_remove = 0
    for j in range(first_one, last_one):
        if s[j] == '0':
            zeros_to_remove += 1
            
    print(zeros_to_remove)