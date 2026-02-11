import sys

stringArray=sys.stdin.read().split()[1:]

for i in range(0,len(stringArray),2):
    mCondition=False
    eCondition=False
    oCondition=False
    wCondition=False
    lower=stringArray[i+1].lower()
    for j in lower:
        if j=="m":
            mCondition=True
        if j=="e" and mCondition:
            eCondition=True
        if j=="o" and eCondition:
            oCondition=True
        if j=="w" and oCondition:
            wCondition=True
        if j!="m" and j!="e" and j!="o" and j!="w": 
            wCondition=False
            break
    if wCondition:
        print("YES")
    else:
        print("NO")