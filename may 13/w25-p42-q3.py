global TreeArray
global RootPointer
global FreeNode
TreeArray = []
for x in range(50): 
    TreeArray.append([-1,-1,-1])
RootPointer = -1
FreeNode = 0
def AddNode(NodeData):
    global FreeNode, TreeArray, RootPointer
    if FreeNode <= 49:
        TreeArray[FreeNode][0] = -1
        TreeArray[FreeNode][1] = NodeData
        TreeArray[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer

            while Placed == False:
                if NodeData < TreeArray[CurrentNode][1]:
                    if TreeArray[CurrentNode][0] == -1:
                        TreeArray[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][0]
                else:
                    if TreeArray[CurrentNode][2] == -1:
                        TreeArray[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = TreeArray[CurrentNode][2]

        FreeNode = FreeNode + 1
    else:
        print("The tree is full")

try:
    FileData = open("TreeData.txt","r")
    for line in FileData:
        AddNode(int(line.strip()))
    FileData.close()
except IOError:
    print("File not found")

def WriteAllToFile():
    try:
        File = open("Tree.txt","a+")
        for line in range(49):
            data = (str(TreeArray[line][0]) + "," + str(TreeArray[line][1]) + "," +  str(TreeArray[line][2])  + "\n")
            File.write(data)
        File.close()
    except IOError:
        print("File not created")

WriteAllToFile()
 