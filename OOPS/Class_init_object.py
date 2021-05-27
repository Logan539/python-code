#Initializing class, using init function, object
class Teddy:
   quantity = 200

    def __init__(self, name, color):
        self.name = name
        self.color = color
        

teddy1 = Teddy('Apple', 'Red', 2)
print("name is = ",teddy1.name)
print("Color is = ",teddy1.color)
print("Stock is = ",teddy1.stock)

print("----------------------")

teddy2 = Teddy('Banana', 'Yellow', 3)
print("name is = ",teddy2.name)
print("Color is = ",teddy2.color)
print("Stock is = ",teddy2.stock)