class Node:
    def __init__(self,pData):
        self.__TheData = pData
        self.__NextNode = None 

    def GetData(self):
        return self.__TheData
    
    def GetNextNode(self):
        return self.__NextNode

    def SetNextNode(self,Node):
        self.__NextNode = Node

class LinkedList:
    def __init__(self):
        self.__HeadNode = None
    
    def InsertNode(self,value):
        newNode = Node(value)
        newNode.SetNextNode(self.__HeadNode)
        self.__HeadNode = newNode
    
    def RemoveNode(self, value):

        if self.__HeadNode is None:
            return False

        if self.__HeadNode.GetData() == value:
            self.__HeadNode = self.__HeadNode.GetNextNode()
            return True

        prevNode = self.__HeadNode
        currentNode = self.__HeadNode.GetNextNode()

        while currentNode is not None:
            if currentNode.GetData() == value:
                prevNode.SetNextNode(currentNode.GetNextNode())
                return True

            prevNode = currentNode
            currentNode = currentNode.GetNextNode()

        return False

    def Traverse(self):
        currentNode = self.__HeadNode
        val = ''
        while currentNode != None:
            val = val + str(currentNode.GetData()) + " "
            currentNode = currentNode.GetNextNode()
        return val


List = LinkedList()
List.InsertNode(10)
List.InsertNode(20)
List.InsertNode(30)
List.InsertNode(40)

print(List.Traverse())
List.RemoveNode(40)
print(List.Traverse())
