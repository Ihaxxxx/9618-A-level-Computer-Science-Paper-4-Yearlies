Queue = [-1] * 50
HeadPointer = -1
TailPointer = -1

def Enqueu(dataToAdd):
    global HeadPointer,Queue,TailPointer

    if (HeadPointer == 0 and TailPointer == 50) or (HeadPointer == 0 and TailPointer == 50):
        return False
    else:
        if HeadPointer == -1 and TailPointer == -1 :
            HeadPointer = 0
            TailPointer = 0
        elif TailPointer == 50:
            TailPointer = 0
        else:
            TailPointer += 1
        Queue[TailPointer] = dataToAdd
        return True

def Dequeu():
    global HeadPointer,Queue,TailPointer
    if HeadPointer == -1 and TailPointer == -1 :
        return False
    else:
        data = Queue[HeadPointer]
        
        if HeadPointer == TailPointer :
            HeadPointer = -1
            TailPointer = -1
        else:
            HeadPointer += 1
            if HeadPointer > 50 :
                HeadPointer = 0

        return data

def CreateQueue():
    global HeadPointer,Queue,TailPointer
    try:
        myFile = open('2025/Summer/P43/QueueData.txt',mode='r')
        for line in myFile:
            reponse = Enqueu(int(line.strip()))
            if reponse == False:
                break
        
    except IOError:
        print("File cannot be open")


CreateQueue()

total = 0
for i in range(50):
    item = Dequeu()
    if item != False:
        total = total + item
    else:
        break
print(total)