import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])

for i in range(1, t + 1):
    s = input_data[i]
    n = len(s)
    
    if n % 2 != 0:
        print("NO")
    else:
        mid = n // 2
        first_half = s[:mid]
        second_half = s[mid:]
        
        if first_half == second_half:
            print("YES")
        else:
            print("NO")