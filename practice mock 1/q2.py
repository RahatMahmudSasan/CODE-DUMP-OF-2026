# Part (a): Global declarations
LibraryData = [[-1, -1] for i in range(50)]
RecordCount = 0


def Initialise():
    global LibraryData, RecordCount
    RecordCount = 0
    for i in range(50):
        LibraryData[i][0] = -1
        LibraryData[i][1] = -1

print(LibraryData)



# Part (b): AddRecord function
def AddRecord(ID, Access):
    global LibraryData, RecordCount
    if RecordCount < 50:
        LibraryData[RecordCount][0] = ID
        LibraryData[RecordCount][1] = Access
        RecordCount += 1
        return True
    else:
        return False


# Part (c): InsertionSort (REVISED to sort by Student ID Ascending)
def InsertionSort():
    global LibraryData, RecordCount
    for index in range(1, RecordCount):
        key = LibraryData[index]
        place = index - 1

        # Sort ASCENDING by Student ID (index 0)
        # This makes the array compatible with Binary Search
        while place >= 0 and LibraryData[place][0] > key[0]:
            LibraryData[place + 1] = LibraryData[place]
            place -= 1
        LibraryData[place + 1] = key


# Part (d): Recursive Binary Search (Search by ID)
def RecursiveSearch(TargetID, Low, High):
    if Low > High:
        return -1

    Mid = (Low + High) // 2

    if LibraryData[Mid][0] == TargetID:
        return LibraryData[Mid][1]  # Return the Access Level
    elif LibraryData[Mid][0] < TargetID:
        # Target is in the upper half
        return RecursiveSearch(TargetID, Mid + 1, High)
    else:
        # Target is in the lower half
        return RecursiveSearch(TargetID, Low, Mid - 1)



# Part (e): Display records
def DisplayRecords():
    global LibraryData, RecordCount
    for i in range(RecordCount):
        print("Student ID:", str(LibraryData[i][0]), "| Access Level:", str(LibraryData[i][1]))


# Part (f) & (g): Main Program Logic
Initialise()

# Adding data
AddRecord(1001, 3)
AddRecord(1050, 1)
AddRecord(1200, 5)
AddRecord(1025, 2)
AddRecord(1100, 4)

# Sort by ID so Binary Search works
InsertionSort()

print("--- Current Records (Sorted by ID) ---")
DisplayRecords()

print("\n--- Search ---")
SearchID = int(input("Enter Student ID to search: "))
Result = RecursiveSearch(SearchID, 0, RecordCount - 1)

if Result == -1:
    print("Student not found")
else:
    print("Student found! Access Level is:", str(Result))
    