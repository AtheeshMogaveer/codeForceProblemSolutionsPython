import sys
listArray=sys.stdin.read().split()[1:]

for i in range(0,len(listArray)-1,2):
    total=0
    unique="".join(dict.fromkeys(listArray[i+1]))
    for j in unique:
        apearance=listArray[i+1].count(j)
        lettervalue= ord(j)-ord("A")+1
        if apearance>=lettervalue:
            total+=1
    print(total)





