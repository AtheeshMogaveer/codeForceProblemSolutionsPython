import sys

stringList=sys.stdin.read().split()[1:]
for item in stringList:
    itemReverse=item[::-1]
    itemClone=""
    for i in itemReverse:
        if i=="q":
            itemClone+="p"
        elif i=="p":
            itemClone+="q"
        else:
            itemClone+=i
    print(itemClone)