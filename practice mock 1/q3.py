class ProductData:
    def __init__(self,ProductIDP,QuantityP):
        self.__ProductID = ProductIDP #Stirng
        self.__Quantity = QuantityP #Integer
    
    def GetProductID(self):
        return self.__ProductID
    def GetQuantity(self):
        return self.__Quantity
    def SetQuantity(self,Q):
        self.__Quantity = Q
    def SetProductID(self,P):
        self.__ProductID = P

    global Queue,HeadPointer,TailPointer,NumberItems
    Queue = [ "" for _ in range(20)]
    HeadPointer = 0
    TailPointer = 0
    NumberItems = 0

    def Enqueue(NewCode):
        global Queue,HeadPointer,TailPointer,NumberItems
        
        if NumberItems == 20:
            print("QUEUE IS FULL")
            return False
        else:
            Queue[TailPointer] = NewCode
            if TailPointer == 19:
                TailPointer = 0
            else:
                TailPointer += 1
            NumberItems += 1
        return True 
    
    def Dequeue():
        global Queue,HeadPointer,TailPointer,NumberItems

        if NumberItems == 0:
            print("Queue is empty")
        else:
            data = Queue[HeadPointer]
            Queue[HeadPointer] = ""
            if HeadPointer == 19:
                HeadPointer = 0
            else:
                HeadPointer += 1
            NumberItems -= 1
        print(data)

            