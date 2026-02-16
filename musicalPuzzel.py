import sys

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    pointer = 1
    for _ in range(t):
        n = int(input_data[pointer])
        s = input_data[pointer + 1]
        pointer += 2
        
        unique_pairs = set()
        for i in range(n - 1):
            pair = s[i] + s[i+1]
            unique_pairs.add(pair)
            
        print(len(unique_pairs))