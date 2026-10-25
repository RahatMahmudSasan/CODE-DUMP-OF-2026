class Challenge:
    def __init__(self, pName, pCategory, pDifficulty):
        self.__ChallengeName = pName
        self.__Category = pCategory
        self.__Difficulty = pDifficulty

    def GetName(self):
        return self.__ChallengeName

    def GetCategory(self):
        return self.__Category

    def GetDifficulty(self):
        return self.__Difficulty


ChallengeSet = [
    Challenge("Turbo Sprint", "speed", 3),
    Challenge("Desert Endurance", "endurance", 5),
    Challenge("Obstacle Course", "agility", 4),
    Challenge("Heavy Lift", "strength", 2),
    Challenge("Speed Circuit", "speed", 4)
]


class Vehicle:
    def __init__(self, name, speed, endurance, agility, strength):
        self.__VehicleName = name
        self.__SpeedSkill = speed
        self.__EnduranceSkill = endurance
        self.__AgilitySkill = agility
        self.__StrengthSkill = strength

    def GetName(self):
        return self.__VehicleName

    def CalculateSuccessRate(self, category, difficulty):

        if category == "speed":
            skill = self.__SpeedSkill
        elif category == "endurance":
            skill = self.__EnduranceSkill
        elif category == "agility":
            skill = self.__AgilitySkill
        elif category == "strength":
            skill = self.__StrengthSkill

        if skill >= difficulty:
            return 100
        else:
            difference = difficulty - skill

            if difference == 1:
                return 80
            elif difference == 2:
                return 60
            elif difference == 3:
                return 40
            else:
                return 20


Thunderbolt = Vehicle("Thunderbolt", 5, 3, 4, 2)
IronTank = Vehicle("Iron Tank", 2, 5, 2, 5)


ThunderPoints = 0
IronPoints = 0

for C in ChallengeSet:

    Rate1 = Thunderbolt.CalculateSuccessRate(C.GetCategory(), C.GetDifficulty())
    Rate2 = IronTank.CalculateSuccessRate(C.GetCategory(), C.GetDifficulty())

    print("Challenge:", C.GetName())

    if Rate1 > Rate2:
        print("Winner:", Thunderbolt.GetName())
        ThunderPoints += 1
    elif Rate2 > Rate1:
        print("Winner:", IronTank.GetName())
        IronPoints += 1
    else:
        print("Result: Draw")

    print()

print("Total Points")
print("Thunderbolt:", ThunderPoints)
print("Iron Tank:", IronPoints)

if ThunderPoints > IronPoints:
    print("Overall Winner: Thunderbolt")
elif IronPoints > ThunderPoints:
    print("Overall Winner: Iron Tank")
else:
    print("Overall Result: Draw")
