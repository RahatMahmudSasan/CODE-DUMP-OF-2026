DataStored = []
NumberItems = 0

def Initialise():
    global DataStored
    global NumberItems
    
    Valid = False
    while Valid == False:
        NumberItems = int(input("How many numbers will you enter? "))
        if NumberItems > 0 and NumberItems < 21:
            Valid = True

    for Count in range(0, NumberItems):
        DataStored.append(int(input("Enter number: ")))

def BubbleSort():
    global DataStored
    global NumberItems
    
    for Count in range(0, NumberItems):
        for Count2 in range(0, NumberItems - 1):
            if DataStored[Count2] > DataStored[Count2 + 1]:
                DataStored[Count2], DataStored[Count2 + 1] = DataStored[Count2 + 1], DataStored[Count2]

def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    
    First = 0
    Last = NumberItems - 1
    
    while First <= Last:
        MidValue = (First + Last) // 2
        
        if DataToFind == DataStored[MidValue]:
            return MidValue
        elif DataToFind < DataStored[MidValue]:
            Last = MidValue - 1
        else:
            First = MidValue + 1
    
    return -1

Initialise()
print("Unsorted:", DataStored)

BubbleSort()
print("Sorted:", DataStored)

Search = int(input("Enter a number to find: "))
print("Index:", BinarySearch(Search))