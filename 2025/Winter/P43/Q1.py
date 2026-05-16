class BoardObject:

    def __init__(self,pCode,pValue) -> None:
        self.__Code = pCode
        self.__Value = pValue
    
    def GetCode(self):
        return self.__Code

    def GetValue(self):
        return self.__Value

Object1 = BoardObject("A",2)
Object2 = BoardObject("B",3)
Object3 = BoardObject("C",5)
Object4 = BoardObject("D",2)
Object5 = BoardObject("E",7)

class Board:

    def __init__(self) -> None:
        self.__TheBoard = [[BoardObject('-',0) for i in range(10)] for i in range(10)]
    
    def GetObject(self,row,col):
        return self.__TheBoard[row][col]

    def SetObject(self,row,col,bObj):
        self.__TheBoard[row][col] = bObj
    
    def Display(self):

        for row in range(10):
            line = ''
            for col in range(10):
                line += self.GetObject(row,col).GetCode() + ' '
            print(line)

MainBoard = Board()
MainBoard.SetObject(0,0,Object1)
MainBoard.SetObject(9,9,Object2)
MainBoard.SetObject(4,5,Object3)
MainBoard.SetObject(2,2,Object4)
MainBoard.SetObject(8,7,Object5)

MainBoard.Display()

InputRow = -1
while InputRow < 0 or InputRow > 9:
    InputRow = int(input("Enter the row position between 0 and 9 "))

InputColumn = -1
while InputColumn < 0 or InputColumn > 9:
    InputColumn = int(input("Enter the column position between 0 and 9 "))
GuessObject = MainBoard.GetObject(InputRow, InputColumn)


if GuessObject.GetCode() == "-":
    print("Miss")
else:
    print("You found " + str(GuessObject.GetCode()) + " with value " +
          
str(GuessObject.GetValue()))