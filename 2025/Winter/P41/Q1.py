import random
Stack = [None] * 30
TopOfStack = -1

def Push(DataToPush):
    global Stack
    global TopOfStack
    if TopOfStack < 29:
       TopOfStack = TopOfStack + 1
       Stack[TopOfStack] = DataToPush
       return True
    else:
       return False

def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
       return -999
    else:
       DataReturn = Stack[TopOfStack]
       TopOfStack = TopOfStack - 1
       return DataReturn

for index in range(40) :
    returnVal = Push(random.randint(0,1000))

    if returnVal == False:
        print("Stack is full")
        break


def FindValues():

    largest = Pop()
    smallest = largest
    poppedVal = largest
    while poppedVal != -999 :
        if poppedVal > largest:
            largest = poppedVal
        elif poppedVal < smallest:
            smallest = poppedVal
        poppedVal = Pop()
    print(f"The highest value is {largest} and the lowest value is {smallest}")

FindValues()