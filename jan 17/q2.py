class Character:
    
    #Name declared as string
    #XCoordinate declared as integer
    #YCoordinate declared as integer
    
    def __init__(self,NameP,XCoordinateP,YCoordinateP):
        self.__Name=NameP
        self.__XCoordinate=XCoordinateP
        self.__YCoordinate=YCoordinateP
    def GetName(self):
        return self.__Name
    def GetX(self): 
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate=self.__XCoordinate+XChange
        self.__YCoordinate=self.__YCoordinate+YChange
Characters=[] #10 elements of character type
file="Character.txt"
try:
    f=open(open,'r')
    for x in range(0,10):
        Name=f.readline().strip()
        XCoord=f.readline().strip()
        YCoord=f.readline().strip()
        tc=Character(Name,int(XCoord),int(YCoord))
        Characters.append(tc)
    f.close()
except:
    print("File not Found")
    print("hello world")
p=-1

while p==-1:
    ch=input("Enter the Character to move".lower())
    for c in range(0,10):
        temp = str(Character[c].GetName()).lower()
        if temp==ch:
            p=c
valid=False
while valid==False:
    m=input("enter a name")
    if m.upper=='A':
        Characters[p].ChangePosition(-1,0)
        valid=True
    elif m =='W':
        Characters[p].ChangePosition(0,1)
    elif m=='S':
        Characters[p].ChangePosition(0,-1)
       
        valid = True 
    elif  m=="D"
         Character[p].ChangePosition(1,0)
         valid=True
         