class Character:
    def __init__(self, Namep, Xcord, Ycord):
        self.__Name = Namep         #string
        self.__XCoordinate = Xcord #integer
        self.__YCoordinate = Ycord #integer

    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange
Characters = []
TextFile = "Characters.txt"
try:
    File = open(TextFile, 'r')
    for X in range(0, 10):
        Name = File.readline().strip()
        XCord = File.readline().strip()
        YCord = File.readline().strip()
        TC = Character(Name, int(XCord), int(YCord))
        Characters.append(TC)
    File.close()
except:
    print("File not found")
IsValid = False
while(IsValid != True):
    Move = input("Enter A to go left, W to go up, S to go down, or D to go right")
    if Move == "A":
        Characters.ChangePosition(-1,0)
        IsValid = True
    elif Move == "W":
        Characters.ChangePosition(0,1)
        IsValid = True
    elif Move == "S":
        Characters.ChangePosition(0,-1)
        IsValid = True
    elif Move == "D":
        Characters.ChangePosition(1,0)
        IsValid = True
        