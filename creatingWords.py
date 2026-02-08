import sys

strList=sys.stdin.read().split("\n")[1:-1]

for strings in strList:
    stringList=strings.split()
    if stringList[1][0]==stringList[0][0]:
        print(stringList[0]+" "+stringList[1])
        continue
    print(stringList[1][0]+stringList[0][1:],end=" ")
    print(stringList[0][0]+stringList[1][1:])