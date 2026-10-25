DataArray = [] # 25 integer array
try:
    DataFile = open("Data.txt","r")
    for line in DataFile:
        DataArray.append(int(line))
    DataFile.close
except IOError:
    print("File not found")
def PrintArray():
    
