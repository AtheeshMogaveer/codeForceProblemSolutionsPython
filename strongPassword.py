import sys
passList=sys.stdin.read().split()[1:]

for item in passList:
    newItem=""
    for i in range(len(item)):
        if len(item)==1:
             newItem=item
             break
        if i<len(item)-1 and item[i]==item[i+1]:
                val="a" if item[i]!="a" else "b"
                newItem=newItem+item[i]+val+item[i+1:]
                break
        else:
             newItem=newItem+item[i]
    if item==newItem:
         val="a" if newItem[len(newItem)-1]!="a" else "b"
         newItem=newItem+val
    print(newItem)
