class Animal:
    def __init__(self,pName,pSound,pSize,pIntelligence):
        self.__Name = pName #String
        self.__Sound = pSound #String
        self.__Size = pSize #Integer
        self.__Intelligence = pIntelligence #Integer
    
    def Constructor(self):
        Message = "The animal's name is" ,self.__Name, ", it makes a ",self.__Sound, ", its size is " ,self.__Size, " and its intelligence level is ",self.__Intelligence,"." 
    
    def Description(self):
        Message = "The animal's name is " + self.__Name + ", it makes a " + self.__Sound + ", its size is " + str(self.__Size) + " and its intelligence level is " + str(self.__Intelligence) + "."
        return Message
    
class Parrot():
    def __init__(self, pName, pSound, pSize, pIntelligence, pWingSpan, pNumberWords):
        super().__init__(pName, pSound, pSize, pIntelligence)
        self.__WingSpan = pWingSpan #integer
        self.__NumberWords = pNumberWords #integer
    
    def ChangeNumberWords(self, Change):
        self.__NumberWords = self.__NumberWords + Change

    def Description(self):
        Message = "The animal's name is " + self._Animal__Name + ", it makes a " + self._Animal__Sound + ", its size is " + str(self._Animal__Size) + " and its intelligence level is " + str(self._Animal__Intelligence) + ". It has a wingspan of " + str(self.__WingSpan) + "cm and can say " + str(self.__NumberWords) + " words."
        return Message

class Wolf(Animal):
    def __init__(self, PName, PSound, PSize, PIntelligence, PTerritorySize):
        super().__init__(PName, PSound, PSize, PIntelligence)
        self.__TerritorySize = PTerritorySize #integer
    
    def SetTerritorySize(self, Change):
        self.__TerritorySize = self.__TerritorySize + Change 
    
    def Description(self):
        Message = "The animal's name is " + self._Animal__Name + ", it makes a " + self._Animal__Sound + ", its size is " + str(self._Animal__Size) + " and its intelligence level is " + str(self._Animal__Intelligence) + " it's territory is " + str(self.__TerritorySize) + " square miles."
        return Message

Animal1 = Parrot("Chewie","Squawk",1,10,30,29) 
Animal2 = Wolf("Nighteyes","Howl",8,7,100) 
Animal3 = Animal("Copper", "Neigh", 10, 6) 

Animal2.SetTerritorySize(-20) 
Animal1.ChangeNumberWords(2) 

print(Animal1.Description()) 
print(Animal2.Description()) 
print(Animal3.Description()) 




