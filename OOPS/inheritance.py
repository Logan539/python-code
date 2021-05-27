class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_data(self):
        self.name = input("Enter the name of Student = ")
        self.age = int(input("Enter the age of Student = "))
    def print_data(self):
        print(self.name)
        print(self.age)
        

class Sci_stud(Students):
    def science(self):
        print("This is a science method")
a = Sci_stud("","")
a.get_data()
a.print_data()