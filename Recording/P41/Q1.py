Queue = [-1] * 20

HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueu(number):
    global HeadPointer , TailPointer , Queue , NumberItems
    if NumberItems == 20 :
        return False
    
    if TailPointer <= -1 :
        TailPointer = 0
        HeadPointer = 0
        Queue[TailPointer] = number
    else:
        TailPointer += 1
        if TailPointer == 20 :
            TailPointer = 0
        Queue[TailPointer] = number
        
    NumberItems += 1
    return True


def Dequeue():
    global HeadPointer , TailPointer , Queue , NumberItems
    if NumberItems <= 0 :
        return -1
    else:
        returnVal = Queue[HeadPointer]
        HeadPointer += 1
        if HeadPointer >= 20 :
            HeadPointer = 0
            NumberItems -= 1
        if NumberItems == 0:
            HeadPointer = -1
            TailPointer = -1
        return returnVal


for i in range(1,26):
    returnVal = Enqueu(i)
    if returnVal == True:
        print(f"{i} Successful")
    else:
        print(f"{i} Unsuccessful")
    
print(Dequeue())
print(Dequeue())