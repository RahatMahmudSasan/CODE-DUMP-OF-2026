class TreasureChest:
    def __init__(self, questionP, answerP, pointsP):
        self.__question = questionP  # string
        self.__answer = int(answerP)  # integer
        self.__points = int(pointsP)  # integer

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answerP):
        return self.__answer == answerP

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0


def readData():
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        dataFetched = file.readline().strip()

        while dataFetched != "":
            question = dataFetched
            answer = file.readline().strip()
            points = file.readline().strip()

            arrayTreasure.append(TreasureChest(question, answer, points))

            dataFetched = file.readline().strip()

        file.close()

    except IOError:
        print("Could not find file")
    

arrayTreasure = []
readData()

choice = int(input("Pick a treasure chest to open: "))

if 0 < choice < 6:
    result = False
    attempts = 0

    while not result:
        answer = int(input(arrayTreasure[choice - 1].getQuestion()))
        result = arrayTreasure[choice - 1].checkAnswer(answer)
        attempts += 1

    print(arrayTreasure[choice - 1].getPoints(attempts))