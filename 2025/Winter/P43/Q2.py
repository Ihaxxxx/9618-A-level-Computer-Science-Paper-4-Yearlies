Queue = [""] * 100
QueueHead = -1
QueueTail = -1
NumberItems = 0

def Enqueu(val):
    global QueueHead,Queue,QueueTail,NumberItems
    if NumberItems == 100:
        return False
    else:
        if QueueHead == -1 and QueueTail == -1:
            QueueHead = 0
            QueueTail = 0
            Queue[QueueHead] = val
            NumberItems = 1
        else:
            QueueTail += 1
            Queue[QueueTail] = val
            NumberItems += 1
            return True

def Dequeue():
    global Queue, QueueHead, QueueTail, NumberItems
    if NumberItems == 0:
        return "False"
    else:
        ReturnData = Queue[QueueHead]
        QueueHead += 1
        NumberItems -=1
    return ReturnData
def ReadData():
    try:
        myFile = open('2025/Winter/P43/BinaryData.txt','r')
        for line in myFile:
            returnVal = Enqueu(line.strip())
            if returnVal == False:
                break
    except IOError:
        print("Cant Open File")

def Compress():
    global Queue
    compressString = ''
    count = 1
    prevVal = Queue[0]
    for i in range(1,len(Queue)):
        nextVal = Queue[i]

        if nextVal == prevVal:
            count += 1
        else:
            compressString += str(prevVal) + str(count)
            prevVal = nextVal
            count = 1
    print(compressString)

ReadData()
Compress()