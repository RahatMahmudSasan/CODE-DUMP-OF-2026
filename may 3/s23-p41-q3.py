Animal = []
Colour = []
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
ColourTopPointer = 0


def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush.strip())
        AnimalTopPointer += 1
        return True


def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def ReadData():
    try:
        global AnimalTopPointer
        global ColourTopPointer
        AnimalFile = open("AnimalData.txt", "r")
        for line in AnimalFile:
            PushAnimal(line.strip())
        AnimalFile.close()

        ColourFile = open("ColourData.txt", "r")
        for line in ColourFile:
            PushColour(line.strip())
        ColourFile.close()
    except IOError:
        print("File not Found")


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour.append(DataToPush.strip())
        ColourTopPointer += 1
        return True


def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData


def OutputItem():
    global AnimalTopPointer
    global ColourTopPointer
    A = PopAnimal()
    C = PopColour()
    if C == "":
        print("No Colour")
        PushAnimal(A.strip())
    elif A == "":
        print("No Animal")
        PushColour(C.strip())
    else:
        print(f"{C} {A}")


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()