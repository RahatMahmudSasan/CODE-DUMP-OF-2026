class Card:
    def __init__(self, NumberP, ColourP):
        self.__Number = NumberP #integer
        self.__Colour = ColourP #string
    
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour

OneRed = Card(1, "red")
TwoRed = Card(2, "red")
ThreeRed = Card(3, "red")
FourRed = Card(4, "red")
FiveRed = Card(5, "red")
OneBlue = Card(1, "blue")
TwoBlue = Card(2, "blue")
ThreeBlue = Card(3, "blue")
FourBlue = Card(4, "blue")
FiveBlue = Card(5, "blue")
OneYellow = Card(1, "yellow")
TwoYellow = Card(2, "yellow")
ThreeYellow = Card(3, "yellow")
FourYellow = Card(4, "yellow")
FiveYellow = Card(5, "yellow")

class Hand:  
    def __init__(self,C1,C2,C3,C4,C5):
        self.__Cards = [] #array
        self.__Cards.append(C1)
        self.__Cards.append(C2)
        self.__Cards.append(C3)
        self.__Cards.append(C4)
        self.__Cards.append(C5)
        self.__FirstCard = 0 #integer
        self.__NumberCards = 5 #integer
    def GetCard(self, pointer):
        return self.__Cards[pointer]
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed,
OneYellow)
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow,
FiveYellow, OneBlue)
def CalculateValue(Player):
    score = 0
    for count in range(0, 5):
        inhand = Player.redguardGetCard(count)
        score = score + inhand.GetNumber()
        Colour = inhand.GetColour()
        if Colour == "red":
            score = score + 5
        elif Colour == "blue":
            score = score + 10
        else:
            score = score + 15
    return score
P1score = CalculateValue(Player1)
P2score = CalculateValue(Player2)
if P1score > P2score:
    print("P1 VICTORY")
elif P1score < P2score:
    print("P2 is the goat")
else:
    print("TIE, YOU BOTH SUCK")
