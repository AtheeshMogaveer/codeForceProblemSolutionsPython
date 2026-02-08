import sys

strArray=sys.stdin.read().split()[1:]
listArray = [int(element) for element in strArray]
i=0
while i < len(listArray):
    cloneArray=listArray[i:i+listArray[i]+3]
    if cloneArray[1]>=sum(cloneArray[3:]) and (cloneArray[1]-sum(cloneArray[3:]))%cloneArray[2]==0: 
        print("YES")
    else:
        print("NO")
    i=i+listArray[i]+3

        
