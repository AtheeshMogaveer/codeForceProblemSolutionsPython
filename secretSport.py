import sys

stringArray=sys.stdin.read().split()[1:]

for i in range(1,len(stringArray),2):
    print(stringArray[i][-1])


    