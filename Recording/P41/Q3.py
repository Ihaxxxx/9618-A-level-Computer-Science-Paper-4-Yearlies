class Node :
    # DECLARE PRIVATE NodeData : INTEGER
    # DECLARE PRIVATE LeftNode , RightNode : Node

    def __init__(self,PnodeData):
        self.__NodeData = PnodeData
        self.__LeftNode = None
        self.__rightNode = None
    
    def GetLeft(self):
        return self.__LeftNode
    
    def GetRight(self):
        return self.__rightNode
    
    def GetData(self):
        return self.__NodeData
    
    def SetLeft(self,Pnode):
        self.__LeftNode = Pnode
    
    def SetRight(self,Pnode):
        self.__rightNode = Pnode
    
class Tree:
    # DECLARE PRIVATE FirstNode : Node

    def __init__(self,Pnode):
        self.__FirstNode = Pnode
    
    def GetRootNode(self):
        return self.__FirstNode

    def Insert(self,NewNode):
        currentNode = self.__FirstNode
        inserted = False
        while not inserted:
            print(currentNode)
            if NewNode.GetData() < currentNode.GetData():
                if currentNode.GetLeft() == None:
                    currentNode.SetLeft(NewNode)
                    return True
                else :
                    currentNode = currentNode.GetLeft()
            else:
                if currentNode.GetRight() == None:
                        currentNode.SetRight(NewNode)
                        return True
                else :
                    currentNode = currentNode.GetRight()
    

Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7)


def OutputInOrder(RootNode):

    if RootNode.GetLeft() != None:
        OutputInOrder(RootNode.GetLeft())
    
    print(RootNode.GetData())

    if RootNode.GetRight() != None:
        OutputInOrder(RootNode.GetRight())

BinaryTree = Tree(Node1)
BinaryTree.Insert(Node2)
BinaryTree.Insert(Node3)
BinaryTree.Insert(Node4)
BinaryTree.Insert(Node5)

OutputInOrder(BinaryTree.GetRootNode())