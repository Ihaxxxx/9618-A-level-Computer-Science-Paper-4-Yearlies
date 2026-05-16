def RevursiveCount(ArrayCopy,NumberElements,DataToFind):

    if len(ArrayCopy) <= 0:
        return 0
    
    if ArrayCopy[0] == DataToFind:
        return RevursiveCount(ArrayCopy[1:],NumberElements - 1 ,DataToFind) + 1
    else:
        return RevursiveCount(ArrayCopy[1:],NumberElements - 1 ,DataToFind)


TheArray = [0 ,5, 1, 2, 5, 9, 9, 6, 5, 0]
print(RevursiveCount(TheArray,10,0))

x = "x=0;y=1;x=x+y;y++;"
def SplitData(value):
    startIndex = 0
    commands = []
    for count in range(len(value)):

        if value[count] == ';':
            commands.append(value[startIndex:count+1])
            startIndex = count + 1
    
    return commands

print(SplitData(x))


