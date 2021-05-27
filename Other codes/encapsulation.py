#encapsulation or data hiding
#__ before variable is for hiding or protecting the data

"""class Myclass:
    __hidden = 0
    def add(self,increment):
        self.__hidden+= increment
        print(self.__hidden)
        
a = Myclass()
a.add(5)
print(a.__hidden)