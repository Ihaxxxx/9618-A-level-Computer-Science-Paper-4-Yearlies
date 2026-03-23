TreeArray = []

for x in range(50):
    TreeArray.append([-1,-1,-1])

RootPointer = -1
FreeNode = 0

TreeArray = []

for x in range(50):
    TreeArray.append([-1, -1, -1])

RootPointer = -1
FreeNode = 0


def AddNode(value):
    global FreeNode
    global TreeArray
    global RootPointer

    if FreeNode <= 49:
        TreeArray[FreeNode][0] = -1
        TreeArray[FreeNode][1] = value
        TreeArray[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            inserted = False
            current = RootPointer

            while inserted == False:
                if value < TreeArray[current][1]:
                    if TreeArray[current][0] == -1:
                        TreeArray[current][0] = FreeNode
                        inserted = True
                    else:
                        current = TreeArray[current][0]
                else:
                    if TreeArray[current][2] == -1:
                        TreeArray[current][2] = FreeNode
                        inserted = True
                    else:
                        current = TreeArray[current][2]

        FreeNode = FreeNode + 1

    else:
        print("The tree is full")

try:
    File= open("2025/Winter/P42 - P43/TreeData.txt")
    for Line in File:
       AddNode(int(Line.strip()))
    File.close()
except:
    print("Error cannot open file")

def WriteAllToFile():
    global TreeArray
    try:
        newFile = open('Tree.txt','a+')
        for item in TreeArray:
            newStr = str(item[0]) + ',' + str(item[1]) + ',' + str(item[2]) + '\n'
            newFile.write(newStr) 
        newFile.close()
    except:
        print("cannot create file")

WriteAllToFile()