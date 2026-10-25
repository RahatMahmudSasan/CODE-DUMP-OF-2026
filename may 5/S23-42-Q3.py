class Employee:
    def __init__(self,HourlyPayP,EmployeeNumberP,JobTitleP):
        self.__HourlyPay = HourlyPayP #float
        self.__EmployeeNumber = EmployeeNumberP #string
        self.__JobTitle = JobTitleP #string
        self.__PayYear2022 = [] # array of 52

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber
    def SetPay(self,WeekNum,HourNum):
        self.__PayYear2022[WeekNum -1] = HourNum * HourlyPay
    def GetTotalPay(self): 
        TotalPay = 0 
        for i in range (0, 51): 
            TotalPay = TotalPay + self.__PayYear2022[i] 
        return TotalPay 
class Manager:
    def __init__(self,HourlyPayP,EmployeeNumberP,JobTitleP,BonusValueP):
        super().__init__(HourlyPayP,EmployeeNumberP,JobTitleP)
        self.__BonusValue = BonusValueP #float

  
Pay = 0.00 
ID = "" 
Bonus = 0.00 
Title = "" 
Temp = "" 
try: 
  TextFile = "Employees.txt" 
  File = open(TextFile, 'r') 
  for x in range(0, 8): 
     Pay = float(File.readline()) 
     ID = File.readline() 
     Temp = File.readline() 
   
      try: 
         
          Bonus = float(Temp) 
          Title = File.readline() 
          EmployeeArray.append(Manager(ID, Pay, Title, Bonus)) 
      except: 
         
          Title = Temp 
          EmployeeArray.append(Employee(ID, Pay, Title))
    