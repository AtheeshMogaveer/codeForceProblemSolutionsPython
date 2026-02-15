import sys

t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    pattern = "Yes" * 20
    
    for _ in range(t):
        s = sys.stdin.readline().strip()
        if s in pattern:
            print("YES")
        else:
            print("NO")