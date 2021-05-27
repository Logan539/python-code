#create an method in

class Teddy:
    quantity = 200

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def color_change(self, color):
        print("this is a method")
        self.color = color

    def name_change(self):
        print("this is 2nd method")
        self.name = input("Please enter the name: ")

teddy1 = Teddy("Ted","Red")
print(teddy1.name)
print(teddy1.color)

teddy1.color_change("Orange")
print(teddy1.name)
print(teddy1.color)

teddy1.name_change()
print(teddy1.name)
print(teddy1.color)