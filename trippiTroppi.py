import sys
nameList=sys.stdin.read().split("\n")[1:]
for name in nameList:
    nameSplit=name.split()
    modernName=""
    for word in nameSplit:
        modernName+=word[0]
    print(modernName)