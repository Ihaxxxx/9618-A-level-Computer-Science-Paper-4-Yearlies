DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54,1]

def insertionSort(numArray):

    for i in range(1,len(numArray)):
        temp = numArray[i]
        pointer = i - 1
        while pointer > 0 and numArray[pointer] > temp:
            numArray[pointer + 1] = numArray[pointer]
            pointer -= 1
        
        numArray[pointer + 1] = temp

    return numArray


def OutputArray(NumArray):
    for item in NumArray:
        print(item,end=" ")

def BinarySearch(DataArray,ItemToFind):

    upper = len(DataArray)
    lower = 0

    while lower <= upper:

        mid = (lower + upper) // 2
        if DataArray[mid] == ItemToFind:
            return mid
        elif DataArray[mid] > ItemToFind:
            upper = mid - 1
        elif DataArray[mid] < ItemToFind:
            lower = mid + 1
    
    return -1

DataArray = insertionSort(DataArray)
print(DataArray)
print(BinarySearch(DataArray,0))
print(BinarySearch(DataArray,345))
print(BinarySearch(DataArray,67))
print(BinarySearch(DataArray,2))