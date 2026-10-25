import datetime
class Character:
    def __init__(self,CharNameP,DOBP,IntelligenceP,SpeedP):
        self.__CharacterName = CharNameP #string
        self.__DateOfBirth = DOBP #date
        self.__Intelligence = IntelligenceP # float
        self.__Speed = SpeedP #integer

    def GetIntelligence(self):
        return self.__Intelligence
    def GetName(self):
        return self.__CharacterName
    def GetSpeed(self):
        return self.__Speed
    def SetIntelligence(self,Intelligence):
        self.__Intelligence = Intelligence
    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.1
    def Return(self):
        return 2023 - self.__DateOfBirth.year 

FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)

class MagicCharacter(Character):
    def __init__(self, CharNameP, DOBP, IntelligenceP, SpeedP, ElementP):
        super().__init__(CharNameP, DOBP, IntelligenceP, SpeedP)
        self.__Element = ElementP
    def Learn(self):
        if self.__Element == "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence() * 1.20)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence() * 1.30)
        else:
            super().SetIntelligence(super().GetIntelligence() * 1.10)
    def CompareSpeed(self, OtherCharacter):
        if super().GetSpeed() > OtherCharacter.GetSpeed():
            return super().GetName()
        elif super().GetSpeed() < OtherCharacter.GetSpeed():
            return OtherCharacter.GetName()
        else:
            return "Equal speed"
FirstMagic = MagicCharacter("Light", datetime.datetime(2018, 3, 3), 75, 22, "fire")

FirstMagic.Learn()
print("Name:", FirstMagic.GetName())
print("Age:", FirstMagic.Return())
print("Intelligence:", FirstMagic.GetIntelligence())

print()
print("Faster character:", FirstMagic.CompareSpeed(FirstCharacter))