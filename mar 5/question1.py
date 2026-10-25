#part a
class node:
    def __init__(self, data,nextNode):
        self.data = data                #Declared data as integer
        self.nextNode= nextNode         #Declared nextNode as integer


#part b 
linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),
              node(-1,6),node(-1,7),node(56,3),node(-1,9),node(-1,-1)]

startPointer = 0 #Declared startPointer as integer
emptyList = 5    #Declared emptyList as integer


#part c (i)
def outputNodes(linkedList, selectedPointer):
    while(selectedPointer != -1):
        print(str(linkedList[selectedPointer].data))
        selectedPointer = linkedList[selectedPointer].nextNode


#part c (ii)
outputNodes(linkedList, startPointer)


#part d 
def addNode(linkedList, currentPointer, emptyList):

    dataToAdd = input("Enter the data to add")   

    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newNode = node(int(dataToAdd), -1)      
        nextFree = linkedList[emptyList].nextNode 

        linkedList[emptyList] = newNode        

        previousPointer = 0

        while(currentPointer != -1):
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode

        linkedList[previousPointer].nextNode = emptyList

        emptyList = nextFree                               
        return True


outputNodes(linkedList, startPointer)

returnValue = addNode(linkedList, startPointer, emptyList)

if returnValue == True:
    print("Item successfully added")
else:
    print("Item not added, list full")

outputNodes(linkedList, startPointer)