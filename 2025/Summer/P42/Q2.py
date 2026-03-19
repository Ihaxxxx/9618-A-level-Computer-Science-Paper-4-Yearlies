class NewRecord:
    #  DECLARE PRIVATE Key : INTEGER
    #  DECLARE PRIVATE Item1 : INTEGER
    #  DECLARE PRIVATE Item2 : INTEGER

    def __init__(self, pKey, pItem1, pItem2):

        self.__Key = pKey 
        self.__Item1 = pItem1 
        self.__Item2 = pItem2 

    def GetKey(self):
        return self.__Key
    def GetItem1(self):
        return self.__Item1
    def GetItem2(self):
        return self.__Item2
        
HashTable = []
Spare = []

def Initialise():
    global HashTable
    global Spare

    for x in range(200):
        HashTable.append(NewRecord(-1,-1,-1))

    for j in range(200):
        Spare.append(NewRecord(-1,-1,-1))

def CalculateHash(keyField):
    return keyField % 200 

def InsertIntoHash(NewRecord):
    global HashTable
    global Spare

    key = CalculateHash(NewRecord.GetKey())
    
    if HashTable[key].GetKey() == -1:
        HashTable[key] = NewRecord
    else:
        for x in range(200):
            if Spare[x].GetKey() == -1 :
                Spare[x] = NewRecord
                break

def CreateHashTable():
    try:
        myFile = open('/Users/apple/Documents Local/A2/COMPUTER SCIENCE/Yearlies P4/2025/Summer/P42/Text Files/HashData.txt','r')
        print('meow')
        for line in myFile:
            key , item1 , item2 = line.strip().split(',')
            record = NewRecord(int(key),int(item1),int(item2))
            InsertIntoHash(record)
        myFile.close()
    except:
        print("file couldn't be open")

def PrintSpare():
    global Spare
    for item in Spare:
        if item.GetKey() != -1 :
            print(item.GetKey())

Initialise()
CreateHashTable()
PrintSpare()