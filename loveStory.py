import sys

stringArray=sys.stdin.read().split()[1:]
string="codeforces"

for i in stringArray:
    diff=0
    for j in range(len(i)):
        if i[j]!=string[j]:
            diff+=1
    print(diff)