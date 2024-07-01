#This file shows the usage of Inheritance.
#Cat and Dog are subclasses which inherits from superclass Animal
#Instances from Cat class can access its parent class Animal
#instances from Dog class can access its parent class Animal
#But instances from Dog class connot access instances from cat class, and vice versa.
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name : {self.name}, Age : {self.age}"


class Cat(Animal):
    def __init__(self, name, age, breed, FurColor):
        super().__init__(name, age)
        self.breed = breed
        self.FurColor = FurColor

    def displayInfo(self):
        return f"{super().display()}, Breed : {self.breed}, Color : {self.FurColor}"

class Dog(Animal):
    def __init__(self, name , age, breed):
        super().__init__(name, age)
        self.breed = breed
    def displaInfo(self):
        return f"{super().display()}, Breed: {self.breed}"



Dog1 = Dog("Stella", 3, "Bulldog" )
Dog2 = Dog("Mikey", 2, "German Shepard")
Cat1 = Cat("Mochi", 4, "Domestic Longhair", "Grey&White")
Cat2 = Cat("kookie", 4, "Domestic Longhair", "Grey")

print(Dog1.displaInfo())
print(Cat1.displayInfo())