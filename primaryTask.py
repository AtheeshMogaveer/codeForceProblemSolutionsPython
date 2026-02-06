import sys

numArray=sys.stdin.read().split()[1:]
for num in numArray:      
    if num.startswith("10")and len(num)>=3  and  num[2]!="0" and  int(num[2::])>=2:
        print("YES")
    else:
        print("NO")
