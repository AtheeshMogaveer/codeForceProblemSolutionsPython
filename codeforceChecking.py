import sys

stringList=sys.stdin.read().split()[1:]
for i in stringList:
    if i in "codeforces":
        print("YES")
    else:
        print("NO")