import sys

stringList=sys.stdin.read().split()[1:]

for i in stringList:
    s=i.lower()
    if s=="yes":
        print("YES")
    else:
        print("NO")