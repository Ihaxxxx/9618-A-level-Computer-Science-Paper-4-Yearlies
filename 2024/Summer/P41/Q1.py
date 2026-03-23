def ReadData():
    DataArray = []
    try:
        File = open("2024/Summer/P41/Data.txt",'r')
        for line in File:
            DataArray.append(line.strip())
        File.close()
        return DataArray
    except:
        print("No file found")

def FormatArray(DataArray):
    newStr = ""
    for item in DataArray:
        newStr += item + " "
    return newStr


def CompareString(value1,value2):
    count = 0

    while True:

        if value1[count] > value2[count] : 
            return 2
        elif value1[count] < value2[count]:
            return 1
        count += 1

def Bubble(DataArray):
    ArrayLength = len(DataArray)

    for x in range(ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            Result = CompareString(DataArray[y], DataArray[y + 1])

            if Result == 2:
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]

    return DataArray

Colors = ReadData()
print(FormatArray(Colors))
Colors = Bubble(Colors)
print(FormatArray(Colors))