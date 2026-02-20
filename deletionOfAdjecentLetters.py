import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
pointer = 1

for _ in range(t):
    s = input_data[pointer]
    c = input_data[pointer + 1]
    pointer += 2
    
    possible = False
    for i in range(len(s)):
        if s[i] == c and i % 2 == 0:
            possible = True
            break
            
    if possible:
        print("YES")
    else:
        print("NO")     