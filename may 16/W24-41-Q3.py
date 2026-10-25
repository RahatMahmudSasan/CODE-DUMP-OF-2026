LinkedList = []
FirstEmpty = 0
FirstNode = -1

for i in range(20):
    LinkedList.append([-1, i + 1])
LinkedList[19][1] = -1

def InsertData():
    global LinkedList, FirstEmpty, FirstNode
    for x in range(5):
        if FirstEmpty != -1:
            temp = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Enter value: "))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = temp

def OutputLinkedList():
    global LinkedList, FirstNode
    CurrentPointer = FirstNode
    if CurrentPointer == -1:
        print("List is empty.")
        return
    while CurrentPointer != -1:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]

InsertData()
OutputLinkedList()
print()