class Vehicle:
    def __init__(self, IDP, MaxSpdP, IncreaseAmountP):
        self.__ID = IDP #string
        self.__MaxSpd = MaxSpdP #integer
        self.__IncreaseAmount = IncreaseAmountP #integer
        self.__CurrentSpd = 0
        self.__HorizontalPos = 0

    def GetCurrentSpd(self):
        return self.__CurrentSpd

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPos(self):
        return self.__HorizontalPos

    def GetMaxSpd(self):
        return self.__MaxSpd

    def SetCurrentSpd(self, CSpdP):
        self.__CurrentSpd = CSpdP

    def SetHorizontalPos(self, HPosP):
        self.__HorizontalPos = HPosP

    def IncreaseSpd(self):
        self.__CurrentSpd = self.__CurrentSpd + self.__IncreaseAmount

        if self.__CurrentSpd > self.__MaxSpd:
            self.__CurrentSpd = self.__MaxSpd

        self.__HorizontalPos = self.__HorizontalPos + self.__CurrentSpd

    def OutputCurrentPos(self):
        print("Current pos = ", self.__HorizontalPos)
        print("Current spd = ", self.__CurrentSpd)

class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpdP, IncreaseAmountP, VerticalChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpdP, IncreaseAmountP)
        self.__VerticalPos = 0
        self.__VerticalChange = VerticalChangeP
        self.__MaxHeight = MaxHeightP

    def IncreaseSpd(self):
        self.__VerticalPos = self.__VerticalPos + self.__VerticalChange

        if self.__VerticalPos > self.__MaxHeight:
            self.__VerticalPos = self.__MaxHeight

        super().IncreaseSpd()

    def OutputCurrentPos(self):
        super().OutputCurrentPos()
        print("Current vertical pos = ", self.__VerticalPos)



Car = Vehicle("Tiger", 100, 20)
Heli1 = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpd()
Car.IncreaseSpd()
Car.OutputCurrentPos()

print("")

Heli1.IncreaseSpd()
Heli1.IncreaseSpd()
Heli1.OutputCurrentPos()