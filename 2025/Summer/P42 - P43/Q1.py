Stack = ["-1"] * 20
TopOfStack = -1 

def Push(value):
    global Stack
    global TopOfStack
    if TopOfStack == 19 :
        return -1
    else:
        TopOfStack += 1
        Stack[TopOfStack] = value
        return 1

def Pop():
    global Stack
    global TopOfStack
    if TopOfStack == -1:
        return "-1"
    else:
        data = Stack[TopOfStack]
        TopOfStack -= 1
        return data
    
def ReadData(filename):
    filePath = f'2025/Summer/P42/Text Files/{filename}'

    try:
        myFile = open(filePath,'r')
        for line in myFile:
            result = Push(line.strip()) 
            if result == -1 :
                print("Stack is full")
        myFile.close()
    except:
        print("File couldn't be open")

def Calculate():
    global Stack
    global TopOfStack

    Total = Pop()
    Total = int(Total)

    Return = 0
    LastOperator = ""
    Operator = True

    while Return != "-1":
        Return = Pop()

        if Operator == False:
            Data = int(Return)

            if LastOperator == "+":
                Total = Total + Data
            elif LastOperator == "-":
                Total = Total - Data
            elif LastOperator == "*":
                Total = Total * Data
            elif LastOperator == "/":
                Total = Total / Data
            elif LastOperator == "^":
                Total = Total ** Data

            Operator = True

        else:
            LastOperator = Return
            Operator = False

    return Total

filename = input("Enter a filename : ")
ReadData(filename='StackData.txt')
print(Calculate())

filename = input("Enter a filename : ")
ReadData(filename='SecondStack.txt')
print(Calculate())
