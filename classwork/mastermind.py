import random
compNum = str(random.randint(1000,10000))
print(compNum)
righPosCount = 0
inpNum = input("Enter a 4 digit number ")
while righPosCount != 4:
    wrongPosCount = 0
    righPosCount = 0
    valCount = 0    
    for i in range(0,4):
        if inpNum[i] in compNum:
            valCount = valCount + 1
            indexVal = compNum.index(inpNum[i])
            if i == indexVal:
                righPosCount = righPosCount + 1
            else:
                wrongPosCount = wrongPosCount + 1
    print(wrongPosCount*"*"+righPosCount*"+")
    if righPosCount == 4:
        print("Yay you have won!!!")
        break
    else:
        inpNum = input("Enter a 4 digit number ")
