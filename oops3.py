# What is Polymorphism?

# Polymorphism means "many forms." In Object-Oriented Programming (OOPs), 
# Polymorphism allows methods to have the same name but behave differently in different classes.

# Polymorphism is mainly achieved in Python through:

# Method Overriding (Runtime Polymorphism),
# Method Overloading (Not natively supported but can be achieved),
# Operator Overloading,


# Method Overriding (Runtime Polymorphism)

# What is Method Overriding?

# A method in the child class has the same name as a method in the parent class but provides a different implementation.
# The method in the child class overrides the parent class’s method.

# syntax

# class Parent:
#     def show(self):
#         print("This is the Parent class method.")

# class Child(Parent):
#     def show(self):  # Overriding the Parent class method
#         print("This is the Child class method.")

# obj = Child()
# obj.show()  # Calls the overridden method in Child class


# ex-1

# class Animal:
#     def speak(self):
#         print("Animals make different sounds.")

# class Dog(Animal):
#     def speak(self):  # Overriding the Parent class method
#         print("Dog barks.")

# class Cat(Animal):
#     def speak(self):  # Overriding the Parent class method
#         print("Cat meows.")

# dog = Dog()
# cat = Cat()
# dog.speak()  # Output: Dog barks.
# cat.speak()  # Output: Cat meows.

# ex-2

# class BankAccount:
#     def interest_rate(self):
#         print("General Bank Account Interest Rate: 4%")

# class SavingsAccount(BankAccount):
#     def interest_rate(self):
#         print("Savings Account Interest Rate: 6%")

# class FixedDeposit(BankAccount):
#     def interest_rate(self):
#         print("Fixed Deposit Interest Rate: 8%")

# savings = SavingsAccount()
# fixed = FixedDeposit()

# savings.interest_rate()  # Output: Savings Account Interest Rate: 6%
# fixed.interest_rate()    # Output: Fixed Deposit Interest Rate: 8%


# ex-3

# Parent Class
# class Vehicle:
#     def describe(self, brand):
#         print(f"This is a vehicle of brand {brand}")

# # Child Class
# class Car(Vehicle):
#     def describe(self, brand, model):  # Overriding with more arguments
#         print(f"This is a {brand} car, model {model}")

# # Creating object of Child class
# car = Car()
# car.describe("Toyota", "Corolla")  # Calls overridden method in Car


# Method Overloading (Compile-Time Polymorphism)

# Method Overloading in Python:

# Python does NOT support method overloading like Java or C++.
# However, we can achieve similar behavior using default arguments or *args (variable-length arguments).

# Example 1: Using Default Arguments

# class MathOperations:
#     def add(self, a, b, c=0):  # c is an optional argument
#         return a + b + c

# obj = MathOperations()
# print(obj.add(10, 20))      # Output: 30
# print(obj.add(10, 20, 30))  # Output: 60

# ex-2

# class Calculator:
#     def multiply(self, *args):  # Accepts multiple arguments
#         result = 1
#         for num in args:
#             result *= num
#         return result

# obj = Calculator()
# print(obj.multiply(2, 3))         # Output: 6
# print(obj.multiply(2, 3, 4))      # Output: 24
# print(obj.multiply(2, 3, 4, 5))   # Output: 120

# operator overloading

# What is Operator Overloading?

# In Python, *operators (+, -, , etc.) are special methods that can be redefined for user-defined classes.
# We use magic methods (dunder methods) like __add__, __sub__, __mul__, etc., to overload operators.

# ex=1

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# # Creating two points
# p1 = Point(2, 3)
# p2 = Point(4, 5)

# p3 = p1 + p2  # Calls __add__ method
# print(f"New Point: ({p3.x}, {p3.y})")  # Output: New Point: (6, 8)

# ex-2

# class Multiplier:
#     def __init__(self, num):
#         self.num = num

#     def __mul__(self, other):
#         return Multiplier(self.num * other.num)

# obj1 = Multiplier(5)
# obj2 = Multiplier(3)

# obj3 = obj1 * obj2  # Calls __mul__ method
# print(obj3.num)  # Output: 15

# ex-3

# class Box:
#     def __init__(self, weight):
#         self.weight = weight

#     def __gt__(self, other):  # Greater than `>`
#         return self.weight > other.weight

#     def __lt__(self, other):  # Less than `<`
#         return self.weight < other.weight

# box1 = Box(10)
# box2 = Box(15)

# print(box1 > box2)  # Output: False
# print(box1 < box2)  # Output: True

# What is Abstraction?

# Abstraction is the concept of hiding the complex implementation details and 
# exposing only the necessary information to the user. In simpler terms, it focuses on what an object does, not how it does it.

# In Python, abstraction is achieved using abstract classes and methods, which are part of the abc (Abstract Base Class) module.


# Abstract Class:

# A class that cannot be instantiated (cannot create objects from it).
# It can contain abstract methods (methods without implementation) and non-abstract methods (with implementation).
# Abstract Method:

# A method that is declared but contains no implementation in the abstract class.
# It must be implemented by any subclass of the abstract class.
# Purpose:

# To provide a blueprint for other classes.
# Abstract classes allow the creation of a contract (the abstract methods) that subclasses must follow.

# How is Abstraction Implemented in Python?
# Abstract Base Class (ABC):
# The ABC class in Python is used to define abstract classes.
# The @abstractmethod decorator is used to define abstract methods inside an abstract class.


# from abc import ABC, abstractmethod

# class AbstractClass(ABC):
#     @abstractmethod
#     def abstract_method(self):
#         pass  # No implementation here

#     def regular_method(self):
#         print("This is a regular method.")

# # Concrete class inheriting from AbstractClass
# class ConcreteClass(AbstractClass):
#     def abstract_method(self):
#         print("Implementation of the abstract method.")

# # Creating object of ConcreteClass
# obj = ConcreteClass()
# obj.abstract_method()  # Output: Implementation of the abstract method.
# obj.regular_method()   # Output: This is a regular method.


# ex-2

# from abc import ABC, abstractmethod

# # Abstract class Shape
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass  # Abstract method to calculate area
    
#     def display(self):
#         print("This is a shape.")

# # Concrete class Circle
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius  # Circle area formula

# # Concrete class Rectangle
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width  # Rectangle area formula

# # Creating objects of concrete classes
# circle = Circle(5)
# rectangle = Rectangle(4, 6)

# # Calling methods
# print(f"Circle Area: {circle.area()}")    # Output: Circle Area: 78.5
# print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 24

# encapsulation method
# Encapsulation in OOP (Object-Oriented Programming)

# Encapsulation is one of the four fundamental principles of Object-Oriented Programming (OOP). 
# It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or class. 
# It also involves restricting direct access to some of the 
# object's components, which is usually done by making some attributes or 
# methods private and only allowing access through public methods (getters and setters).

# In simpler terms, encapsulation is about hiding the internal state of an object and only exposing a controlled interface to the outside world.

# 1. Access Modifiers in Python

# Python does not have strict access control like other languages (e.g., Java, C++). Instead, it follows naming conventions:
# Implementing Encapsulation in Python

# Let's see how encapsulation is implemented with an example.

# Public Members

# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand  # Public variable
#         self.speed = speed  # Public variable

#     def display(self):
#         print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

# car = Car("Toyota", 180)
# print(car.brand)  # Accessible
# print(car.speed)  # Accessible
# car.display()  # Works fine

# Protected Members

# class Car:
#     def __init__(self, brand, speed):
#         self._brand = brand  # Protected variable
#         self._speed = speed  # Protected variable

#     def _display(self):  # Protected method
#         print(f"Brand: {self._brand}, Speed: {self._speed} km/h")

# car = Car("Toyota", 180)
# print(car._brand)  # Accessible but should be used carefully
# print(car._speed)  # Accessible but should be used carefully
# car._display()  # Accessible but not recommended


# Private Members

# class Car:
#     def __init__(self, brand, speed):
#         self.__brand = brand  # Private variable
#         self.__speed = speed  # Private variable

#     def display(self):
#         print(f"Brand: {self.__brand}, Speed: {self.__speed} km/h")

# car = Car("Toyota", 180)
# # print(car.__brand)  # ❌ AttributeError
# # print(car.__speed)  # ❌ AttributeError
# car.display()  # ✅ Works fine

class Car:
    def __init__(self, brand, speed):
        self.__brand = brand
        self.__speed = speed

    # Getter method
    def get_speed(self):
        return self.__speed

    # Setter method
    def set_speed(self, new_speed):
        if new_speed > 0:
            self.__speed = new_speed
        else:
            print("Speed cannot be negative!")

car = Car("Toyota", 180)
print(car.get_speed())  # ✅ Access using getter

car.set_speed(200)  # ✅ Modify using setter
print(car.get_speed())  # ✅ New speed updated

car.set_speed(-10)  # ❌ Invalid speed

