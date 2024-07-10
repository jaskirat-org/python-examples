class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    raise NotImplementedError

class Dog(Animal):

  def make_sound(self):
    print(f"{self.name} barks!")

class Car(Animal, object):  
  def __init__(self, model):
    super().__init__("Car")  
    self.model = model

  def make_sound(self):
    print(f"{self.model} honks!")

dog = Dog("Fido")
dog.make_sound()

car = Car("Tesla")
car.make_sound()  
