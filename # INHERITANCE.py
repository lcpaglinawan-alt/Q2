# INHERITANCE
class Animal:
    def __init__(self,name:str):
        self.name = name

class Dog(Animal):
    def bark(self):
        return f"{self.name} barks. They cant meow. they are't a cat."

pet1 = Dog("Carlos")
print(pet1.bark())