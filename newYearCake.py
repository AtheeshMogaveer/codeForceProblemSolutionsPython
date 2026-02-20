import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
pointer = 1

for _ in range(t):
    a = int(input_data[pointer])
    b = int(input_data[pointer + 1])
    pointer += 2
    
    max_layers = 0
    for L in range(1, 25):
        s_odd = 0
        s_even = 0
        for i in range(L):
            size = 1 << i # This is 2^i
            if i % 2 == 0:
                s_odd += size
            else:
                s_even += size
        
        if (s_odd <= a and s_even <= b) or (s_odd <= b and s_even <= a):
            max_layers = L
        else:
            break
            
    print(max_layers)