import sys

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    for i in range(1, t + 1):
        b = input_data[i]
        
        a = b[0:2]
        for j in range(3, len(b), 2):
            a += b[j]
            
        print(a)