#Polymorphism is being able to assign different
# meaning in different classes under the same name.
#Following the same exampl of animal, cat and dog, but adding
# a function "EatFood"
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name : {self.name}, Age : {self.age}"

class Dog(Animal):
    def __init__(self, name, age ):
        super().__init__(name, age)

    def EatFood(self):
        return f"{self.name} eats dry Kebble for dogs"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def EatFood(self):
        return f"{self.name} eats wet fod for cats"



dog1 = Dog("Mikey", 3)
cat1 = Cat("Bo", 2)
print(dog1.EatFood())
print(cat1.EatFood())
