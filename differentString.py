import sys

strList=sys.stdin.read().split()[1:]

for item in strList:
    flag="NO"
    if len(item)==1:
        print("NO")
        continue
    strList=list(item)
    newList=[]
    for i in range(len(strList)-1):
        if strList[i]!=strList[i+1]:
            newList=strList[:i]+list(strList[i+1])+list(strList[i])+strList[i+2:]
            flag="YES"
            break
    print(flag)
    if flag=="YES":
        print("".join(newList))
    

        
            
        
    
