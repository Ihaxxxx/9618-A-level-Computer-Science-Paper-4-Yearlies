
def ReadData():
    data = []
    fileName = input("Enter a filename : ")
    filePath = f'2025/Summer/P41/Text Files/{fileName}'
    try:
        myFile = open(filePath,'r')
        for line in myFile :
           data.append(line.strip())
        myFile.close() 
    except:
        print("cannot open the file")
    return data


def SplitData(DataArray):
    Red = []
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []

    for line in DataArray :
        val , color = line.split(",")
        match color :
            case "red":
                Red.append(val)
            case "green":
                Green.append(val)
            case "blue":
                Blue.append(val)
            case "orange":
                Orange.append(val)
            case "yellow":
                Yellow.append(val)
            case "pink":
                Pink.append(val)
    
    # part d
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")

def StoreData(DataToStore,Filename) :
    filePath = f'2025/Summer/P41/Text Files/{Filename}'
    try:
        myFile = open(filePath,'a+')
        for item in DataToStore:
            myFile.write(item)
            myFile.write('\n')
        myFile.close()
    except:
        print("Cannot Create file")
        
data = ReadData()
SplitData(data)