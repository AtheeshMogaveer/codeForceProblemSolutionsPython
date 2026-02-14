import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

t = int(input_data[0])
pointer = 1

for _ in range(t):
    n = int(input_data[pointer])
    s = input_data[pointer + 1].lower()
    pointer += 2
    
    result = ""
    if n > 0:
        result = s[0]
        for i in range(1, n):
            if s[i] != s[i-1]:
                result += s[i]
    
    if result == "meow":
        print("YES")
    else:
        print("NO")