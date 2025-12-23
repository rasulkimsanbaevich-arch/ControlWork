class Person:
    def __init__(self, age):
        self._age = age

    def set_age(self, age):
        # if age == self._age:
        #     return self._age
            pass


    def get_age(self):
        return self._age

# p = Person()
# p.set_age(25)
# print(p.get_age())  # Вывод: 25
# p.set_age(-5)  # Должна быть ошибка или предупреждение


# 2
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I'm an Animal"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meo

# 3

class Vehicle:
    def move(self):
        ...
class Car:
    pass

class Bike:
    pass