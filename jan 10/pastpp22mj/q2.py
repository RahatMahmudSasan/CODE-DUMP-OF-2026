class Balloon:
    #Declare Health as int
    # Declare color as str
    #Declare DefenceItem as str
    #declare balloon as the the + 
    def __init__(self,colorp,DefenceItemp):
        self.__color=colorp
        self.__DefenceItem=DefenceItemp
        self.__Health=100
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self,num):
        self.__Health=self.__Health+num
    def CheckHealth(self):
        if self.__Health<=0:
            return True
        else:
            return False
d=input("enter a defence item:")
c = input ("Enter a color:")
balloon1=Balloon(c,d)
def Defend(ball):
    s = int(input("enter the strength:"))
    ball.ChangeHealth(-s)
    print("defence item", str(ball.GetDefenceItem())) 
    if ball.CheckHealth()== True:
        print("failed")
    else:
        print("success")
    return ball
balloon1=Defend(balloon1)  
class handover():
      