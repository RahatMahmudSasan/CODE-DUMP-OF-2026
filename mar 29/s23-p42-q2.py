class Vehicle:
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP):
        self.__ID = IDP  # string
        self.__MaxSpeed = MaxSpeedP  # integer
        self.__IncreaseAmount = IncreaseAmountP  # integer
        self.__CurrentSpeed = 0  # integer
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def SetCurrentSpeed(self, CSP):
        self.__CurrentSpeed = CSP

    def SetHorizontalPosition(self, HPP):
        self.__HorizontalPosition = HPP

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if self.__CurrentSpeed > self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed
        self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed

    def OutputCurrentPosition(self):
        print("Current position = ", self.__HorizontalPosition)
        print("Current speed = ", self.__CurrentSpeed)


class Helicopter(Vehicle):
    def __init__(self, IDP, MaxSpeedP, IncreaseAmountP, VertChangeP, MaxHeightP):
        super().__init__(IDP, MaxSpeedP, IncreaseAmountP)
        self.__VerticalPosition = 0
        self.__VerticalChange = VertChangeP  # Integer
        self.__MaxHeight = MaxHeightP  # Integer

    def OutputCurrentPosition(self):
        print("Current position = ", self.GetHorizontalPosition())
        print("Current speed = ", self.GetCurrentSpeed())
        print("Current vertical position = ", self.__VerticalPosition)


# Main program
Car = Vehicle("Tiger", 100, 20)
Heli1 = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputCurrentPosition()

print("")

Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.OutputCurrentPosition()    