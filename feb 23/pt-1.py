#Object programming in python

class employee:
    def __init__ (self,name,staffno):
        self.name = name 
        self.staffno = staffno                  #line 3 to 9 is what they call a class defination
    def showDetails(self):                      #line 10 and 11 is the object
        print("Employee Name"+self.name)
        print("Emplaoyee Number",self.staffno)
myStaff = employee("Eric Jones", 72)
myStaff = showDetails()

# data hiding
class employee:
    def __init__(self, name, staffno):
      self.__name = name
      self.__staffno = staffno
    def showDetails(self):           #jus dont fucking write the 10 and 11 line and boom data secure
      print("Employee Name " + self.__name)
      print("Employee Number " , self.__staffno)
# e