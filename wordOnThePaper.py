import sys

stringArray=sys.stdin.read().split()[1:]

for i in range(0,len(stringArray),8):
    string="".join(stringArray[i:i+8])
    for i in string:
        if i.isalpha():
            print(i,end="")
    print()

