# inheritance


# Inheritance is a fundamental concept of Object-Oriented Programming (OOP)
# that allows a class (child/derived class) to inherit properties and methods from 
# another class (parent/base class). This promotes code reusability and modularity.

# Types of Inheritance in Python :

# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# 1. single inheritance

# A child class inherits from a single parent class.
# syntax
# class Parent:
#     # Parent class methods and attributes
#     pass

# class Child(Parent):
#     # Child class methods and attributes
#     pass 



# examples


# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal): 
#     def bark(self):
#         print("Dog barks")

# obj1 = Dog()
# obj1.speak()  
# obj1.bark()   


# ex-2

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_details(self):
#         print(f"Employee Name: {self.name}, Salary: {self.salary}")

# class Manager(Employee):
#     def department(self):
#         print(f"{self.name} is a Manager in the Sales department.")
# obj1 = Manager("Alice", 75000)
# obj1.show_details()  # Inherited from Employee
# obj1.department()    # Method from Manager class


# ex/3

# class Vehicle:
#     def general_info(self):
#         print("Vehicles are used for transportation")
# class Car(Vehicle):
#     def car_type(self):
#         print("This is a sports car")
# my_car = Car()
# print(my_car.general_info())  # Inherited from Vehicle
# print(my_car.car_type()  )    # Method from Car class


# mutilevel inheritance

# A child class inherits from a parent, and another child class inherits from it (Grandparent → Parent → Child).
#  syntax

# class Grandparent:
#     # Methods and attributes of Grandparent
#     pass

# class Parent(Grandparent):
#     # Methods and attributes of Parent
#     pass

# class Child(Parent):
#     # Methods and attributes of Child
#     pass



# ex-1

# class Vehicle:
#     def general_info(self):
#         print("Vehicles are used for transportation")

# class Car(Vehicle):
#     def car_type(self):
#         print("This is a car")

# class SportsCar(Car):
#     def speed(self):
#         print("This sports car is very fast")

# sportscar = SportsCar()
# sportscar.general_info()  
# sportscar.car_type()      # Inherited from Car
# sportscar.speed()         # Defined in SportsCar



# ex-2

# Grandparent class
# class Grandparent:
#     def family_name(self):
#         print("Family Name: Johnson")

# # Parent class inheriting from Grandparent
# class Parent(Grandparent):
#     def parent_info(self):
#         print("Parent: Robert Johnson")

# # Child class inheriting from Parent
# class Child(Parent):
#     def child_info(self):
#         print("Child: Emily Johnson")

# # Object creation
# child = Child()
# child.family_name()  # Inherited from Grandparent
# child.parent_info()  # Inherited from Parent
# child.child_info()   # Method from Child class


# ex-3

# Grandparent class
# class Animal:
#     def breathe(self):
#         print("Animals need oxygen to survive")

# # Parent class inheriting from Animal
# class Mammal(Animal):
#     def warm_blooded(self):
#         print("Mammals are warm-blooded")

# # Child class inheriting from Mammal
# class Dog(Mammal):
#     def bark(self):
#         print("Dogs bark loudly")

# # Object creation
# dog = Dog()
# dog.breathe()      # Inherited from Animal
# dog.warm_blooded() # Inherited from Mammal
# dog.bark()         # Method from Dog class



# Hierarchical Inheritance

# Multiple child classes inherit from the same parent class.

# ex-1

# Parent class
# class Animal:
#     def eat(self):
#         return "Animals eat food"

# # Child class 1
# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"

# # Child class 2
# class Cat(Animal):
#     def meow(self):
#         return "Cat meows"

# # Creating objects
# dog = Dog()
# cat = Cat()
# print(dog.eat())   # Inherited from Animal
# print(dog.bark())  # Method of Dog class
# print(cat.eat())   # Inherited from Animal
# print(cat.meow())  # Method of Cat class


# ex-2

# Parent class
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def show_brand(self):
#         print(f"Brand: {self.brand}")

# # Child class 1
# class Car(Vehicle):
#     def car_type(self):
#         print("This is a Car")

# # Child class 2
# class Bike(Vehicle):
#     def bike_type(self):
#         print("This is a Bike")

# # Creating objects
# car = Car("Toyota")
# car.show_brand()  # Inherited from Vehicle
# car.car_type()    # Specific to Car

# bike = Bike("Yamaha")
# bike.show_brand()  # Inherited from Vehicle
# bike.bike_type()   # Specific to Bike

# ex-3


# Parent class
# class Employee:
#     def role(self):
#         print("General Employee")

# # Child class 1
# class Manager(Employee):
#     def role(self):  # Overriding parent method
#         print("Manager of the company")

# # Child class 2
# class Developer(Employee):
#     def role(self):  # Overriding parent method
#         print("Software Developer")

# # Creating objects
# mgr = Manager()
# mgr.role()  # Calls overridden method in Manager

# dev = Developer()
# dev.role()  # Calls overridden method in Developer

# multiple inheritance
# A child class inherits from multiple parent classes.

# Syntax

# class Parent1:
#     # Methods and attributes of Parent1
#     pass

# class Parent2:
#     # Methods and attributes of Parent2
#     pass

# class Child(Parent1, Parent2):
#     # Child class methods and attributes
#     pass


# ex-1

# class Father:
#     def talent(self):
#         print("Father is a singer")

# class Mother:
#     def skill(self):
#         print("Mother is a dancer")

# class Child(Father, Mother):
#     def hobby(self):
#         print("Child loves painting")

# child = Child()
# child.talent()  # Inherited from Father
# child.skill()   # Inherited from Mother
# child.hobby()   # Defined in Child


# ex-2

# Parent Class 1
# class Father:
#     def show_father(self):
#         print("Father's trait")

# Parent Class 2
# class Mother:
#     def show_mother(self):
#         print("Mother's trait")

# # Child Class inheriting from both Father and Mother
# class Child(Father, Mother):
#     def show_child(self):
#         print("Child's traits")

# # Creating object
# c = Child()
# c.show_father()  # Inherited from Father
# c.show_mother()  # Inherited from Mother
# c.show_child()   # Own method


# ex-3

# class ClassA:
#     def display(self):
#         print("This is Class A")

# class ClassB:
#     def display(self):
#         print("This is Class B")

# # Child class inherits from both A and B
# class ClassC(ClassA, ClassB):
#     def display(self):  # Overriding the method
#         print("This is Class C")

# # Creating object
# obj = ClassC()
# obj.display()  # Calls overridden method in ClassC


# Hybrid Inheritance

#  A combination of multiple types of inheritance in a single program.

# class Parent:
#     # Parent class methods and attributes
#     pass

# class Child1(Parent):
#     # Child1 class methods and attributes
#     pass

# class Child2(Parent):
#     # Child2 class methods and attributes
#     pass

# class GrandChild(Child1, Child2):
#     # GrandChild inherits from Child1 and Child2
#     pass


# ex-1

class School:
    def school_name(self):
        print("ABC High School")

class Teacher(School):
    def subject(self):
        print("Teaches Mathematics")

class Student(School, Teacher):  # Hybrid Inheritance
    def student_name(self):
        print("Student: John Doe")

student = Student()
student.school_name()  # Inherited from School
student.subject()      # Inherited from Teacher
student.student_name() # Defined in Student
