class Character:
    def __init__(self, XPosP, YPosP, NameP):
        self.XPos = XPosP  # integer
        self.YPos = YPosP  # integer
        self.Name = NameP  # string

    def GetXPos(self):
        return self.XPos

    def GetYPos(self):
        return self.YPos

    def SetXPos(self, Value):
        self.XPos = self.XPos + Value
        if self.XPos > 10000:
            self.XPos = 10000
        elif self.XPos < 0:
            self.XPos = 0

    def SetYPos(self, Value):
        self.YPos = self.YPos + Value
        if self.YPos > 10000:
            self.YPos = 10000 0

    def Move(self, Direction):
        if Direction == "up":
            self.SetYPos(10)
        elif Direction == "down":
            self.SetYPos(-10)
        elif Direction == "right":
            self.SetXPos(10)
        else:
            self.SetXPos(-10)


Jack = Character(50, 50, "Jack")


class BikeCharacter(Character):
    def __init__(self, XPosP, YPosP, NameP):
        super().__init__(XPosP, YPosP, NameP)

    def Move(self, Direction):
        if Direction == "up":
            super().SetYPos(20)
        elif Direction == "down":
            super().SetYPos(-20)
        elif Direction == "right":
            super().SetXPos(20)
        else:
            super().SetXPos(-20)


Karla = BikeCharacter(100, 50, "Karla")

CharacterToMove = input("Would you like to move Jack or Karla? ").lower()
while CharacterToMove != "jack" and CharacterToMove != "karla":
    CharacterToMove = input("Invalid, try again: ").lower()

Direction = input("Which direction? Up, down, left or right? ").lower()
while Direction not in ["up", "down", "left", "right"]:
    Direction = input("Invalid, try again: ").lower()
 
if CharacterToMove == "jack":
    Jack.Move(Direction)
    print("Jack's new position is X =", Jack.GetXPos(), "Y =", Jack.GetYPos())
else:  
    print("Karla's new position is X =", Karla.GetXPos(), "Y =", Karla.GetYPos()) 