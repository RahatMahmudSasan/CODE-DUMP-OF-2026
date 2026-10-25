class Node:
    def __init__(self,TheData):
        self.__TheData=TheData #integer
        self.__NextNode=None #node
    def GetData(self):
        return self.__TheData
    def GetNextNode(self):
        return self.__NextNode
    def SetNextNode(self,NewNode):
        self.__NextNode=NewNode
class LinkedList:
    def __init__(self): 
        self.__HeadNode=None
    def InsertNode(self,Data):
        TNode=Node(Data)
        TNode.SetNextNode(self.__HeadNode)
        self.__HeadNode=TNode
    def Traverse(self):
        rs=""
        CurrentNode= self.__HeadNode
        while CurrentNode != None:
            rs=rs+str(CurrentNode.GetData()) + " "
            CurrentNode = CurrentNode.GetNextNode()
        return rs   
    def RemoveNode(self, DataToRemove):
        if self.__HeadNode == None:
            return False
        elif self.__HeadNode.GetData() ==DataToRemove:
            self.__HeadNode = self.__HeadNode.GetNextNode()
            return True
        Found = False
        CurrentNode = self.__HeadNode
        while not Found and CurrentNode != None:
            if CurrentNode.GetNextNode().GetData() == DataToRemove:
                CurrentNode.SetNextNode(CurrentNode.GetNextNode().GetNextNode())
                Found = True
            else:
                CurrentNode = CurrentNode.GetNextNode()
CreateList = LinkedList() 

CreateList.InsertNode(10)  
CreateList.InsertNode(20)  
CreateList.InsertNode(30)  
CreateList.InsertNode(40)  
CreateList.InsertNode(50)  
print(CreateList.Traverse())
print()