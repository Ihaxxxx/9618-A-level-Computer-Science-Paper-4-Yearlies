import random

TheArray = []
TheArray = random.sample(range(0,101),20)

def PrintArray(array):
    newStr = ''
    for item in array :
        newStr += str(item) + ' '
    print(newStr)

def BubbleSort(DataArray):
    Swap = True

    while Swap == True:
        Swap = False
        for y in range(0, len(DataArray) - 1):
            if DataArray[y] > DataArray[y + 1]:
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
                Swap = True

    return DataArray

PrintArray(TheArray)
TheArray = BubbleSort()
print("Sorted")
PrintArray(TheArray)

def RecursiveBinarySearch(array, low, high, target):
    if high >= low:
        mid = low + (high - low) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            return RecursiveBinarySearch(array, low, mid - 1, target)

        else:
            return RecursiveBinarySearch(array, mid + 1, high, target)

    else:
        return -1

SearchVal = int(input("Enter a number to search : "))
returnVal = RecursiveBinarySearch(TheArray,0,19,SearchVal)
if returnVal != -1 :
    print(f"Found at position {returnVal}")
else:
    print("Not found")