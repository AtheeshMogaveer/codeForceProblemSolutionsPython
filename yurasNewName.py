import sys

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    for i in range(1, t + 1):
        s = input_data[i]
        ans = 0
        
        if s == "^":
            print(1)
            continue
            
        if s[0] == "_":
            ans += 1
            
        if s[-1] == "_":
            ans += 1
            
        for j in range(len(s) - 1):
            if s[j] == "_" and s[j+1] == "_":
                ans += 1
                
        print(ans)