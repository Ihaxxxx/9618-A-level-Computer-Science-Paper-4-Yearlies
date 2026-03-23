class Record:
    # DECLARE PUBLIC Key : INTEGER
    # DECLARE PUBLIC Data : STRING

    def __init__(self,pKey, pData):
        self.Key = pKey
        self.Data = pData
    

HashTable = []
def InitialiseHashTable():
    global HashTable
    HashTable = [[Record(-1,"")]*10 for i in range(100)]

def Hash(key):
    return key % 100

def InsertData(RecordToAdd):
    global HashTable
    calcHash = Hash(RecordToAdd.Key)

    for index in range(10):
        if HashTable[calcHash][index].Key == -1 :
            HashTable[calcHash][index] = RecordToAdd
            break

def ReadData():
    global HashTable
    File = open("2025/Winter/P41/Text Files/HashTableData.txt",'r')
    for Line in File:
       key , data = Line.strip().split(",")
       InsertData(Record(int(key), data))
    File.close()

def GetRecord(keyField):
    global HashTable
    calcHash = Hash(keyField)
    for index in range(10):
        if HashTable[calcHash][index].Key == keyField :
            return HashTable[calcHash][index].Data
    
    return "Not found"

InitialiseHashTable()
ReadData()


for x in range(5):
    keyFields = int(input("Enter a key field : "))
    returnVal = GetRecord(keyFields)
    print(returnVal)