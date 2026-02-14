import sys

data = sys.stdin.read().split()
if data:
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx])
        h = int(data[idx + 1])
        l = int(data[idx + 2])
        idx += 3
        
        a = [int(x) for x in data[idx:idx + n]]
        idx += n
        
        r_only = 0
        c_only = 0
        both = 0
        
        for v in a:
            if v <= h and v <= l:
                both += 1
            elif v <= h:
                r_only += 1
            elif v <= l:
                c_only += 1
        
        ans = 0
        for k in range(n // 2, -1, -1):
            nr = max(0, k - r_only)
            nc = max(0, k - c_only)
            
            if (nr + nc) <= both:
                ans = k
                break
                
        out.append(str(ans))

    sys.stdout.write("\n".join(out) + "\n")