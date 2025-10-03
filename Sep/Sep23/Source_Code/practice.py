# # s = "GFG"
# # it = iter(s)
# #
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
#
# # Method Overriding
# # We start with a base class and then a subclass that "overrides" the speak method.
# class Animal:
#     def speak(self):
#         return "I am an animal."
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
# print(Dog().speak())
#
# # 2 Duck Typing
# class Cat:
#     def speak(self):
#         return "Meow!"
#
# def make_animal_speak(animal):
#     # This function works for both Dog and Cat because they both have a 'speak' method.
#     return animal.speak()
#
# print(make_animal_speak(Cat()))
# print(make_animal_speak(Dog()))
#
# # 3 Operator Overloading
# # We create a simple class that customizes the '+' operator.
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         # This special method defines the behavior of the '+' operator.
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(2, 3)
# v2 = Vector(4, 5)
# v3 = v1 + v2
#
# print(v3)

class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# Example Usage
dog = Dog("Buddy", "Labrador", 3)

# Accessing public member
print(dog.name)  # Accessible

# Accessing protected member
print(dog._breed)  # Accessible but discouraged outside the class

# Accessing private member using getter
print(dog.get_age())

# Modifying private member using setter
dog.set_age(5)
print(dog.get_info())