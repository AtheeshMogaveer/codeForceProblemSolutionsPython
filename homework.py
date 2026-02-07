import sys

listArray= sys.stdin.read().split()[1:]
j=0
for i in range(1,len(listArray)+1):
    if i%5==0:
        newArray=listArray[i-5:i]
        resultString=newArray[j+1]
        secondClone=newArray[j+3]
        for s in newArray[j+4]:
            if s=="D":
                resultString=resultString+secondClone[0]
            else:
                resultString=secondClone[0]+resultString
            secondClone=secondClone[1:]
        print(resultString)
        
