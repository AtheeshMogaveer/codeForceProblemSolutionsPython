import sys

strArray=sys.stdin.read().split()[1:]
listArray = [int(element) for element in strArray]
i=0
while i < len(listArray):
    cloneArray=listArray[i:i+listArray[i]+3]
    print(cloneArray)
    tot=0
    if cloneArray[1]==sum(cloneArray[3:])  or cloneArray[1]==sum(cloneArray[3:])+cloneArray[2]: 
        cloneArray[len(cloneArray)-1]=cloneArray[2]
        print("YES")
    else:
        print("NO")
    i=i+listArray[i]+3

        
