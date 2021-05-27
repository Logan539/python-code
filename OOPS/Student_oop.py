#OOP program to accept student data
class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_data(self,name,age):
        #self.name = input("Enter the name of Student = ")
        #self.age = int(input("Enter the age of Student = "))
        self.name = name
        self.age = age
    def print_data(self):
        print(self.name)
        print(self.age)
        
stu1 = Students("","")
name = input("Enter the name of Student = ")
age = int(input("Enter the age of Student = "))
stu1.get_data(name,age)
stu1.print_data()