def ReadData():
    Colours = []
    try:
        File = open("Data.txt")
        Colours = File.read().split("\n")
        File.close()
        return Colours
    except:
        print("No file found")
        return []


def FormatArray(DataArray):
    OutputText = ""
    for x in range(0, min(45, len(DataArray))):
        OutputText = OutputText + DataArray[x] + " "
    return OutputText   # ✅ moved outside loop


Colours = ReadData()
print(FormatArray(Colours))


def CompareStrings(First, Second):
    Count = 0
    while Count < len(First) and Count < len(Second):
        if First[Count] < Second[Count]:
            return 1
        elif First[Count] > Second[Count]:
            return 2
        else:
            Count += 1

    # If one string is shorter
    if len(First) < len(Second):
        return 1
    elif len(First) > len(Second):
        return 2
    else:
        return 0


def Bubble(DataArray):
    ArrayLength = len(DataArray)
    for x in range(ArrayLength - 1):
        for y in range(0, ArrayLength - x - 1):
            Result = CompareStrings(DataArray[y], DataArray[y + 1])
            if Result == 2:
                DataArray[y], DataArray[y + 1] = DataArray[y + 1], DataArray[y]
    return DataArray


BubbleSorted = Bubble(Colours)
print(FormatArray(BubbleSorted))


class Horse:
    def __init__(self, PName, PMaxFenceHeight, PPercentageSuccess):
        self.__Name = PName
        self.__MaxFenceHeight = PMaxFenceHeight
        self.__PercentageSuccess = PPercentageSuccess