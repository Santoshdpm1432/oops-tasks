# class_based_example

# Class-based Object-Oriented Programming (OOP) is 
# a paradigm where classes are used as blueprints to create objects.
# A class defines the properties (attributes) and behaviors (methods) that its objects (instances) will have.

# examples :

# Defining a class

# class details():#class definition
#     user_name = "santosh" #attributes
#     dept_id = 1234 #attributes
#     def user_info(self):#methods1
#         print(f"user name {self.user_name} and dept_id {self.dept_id}")
#     def user_info_2(self):#methods2
#         print("this is method 2")
#         self.user_info()
# #syntax
# #objname = classname()
# obj = details()
# obj.user_info()
# obj.user_info_2()
# print(obj.user_name)
# print(obj.dept_id)


# class  cars():#class definition
#     brand_name = "tata" #attributes
#     model_year = 2025
#     def user_info(self):#methods1
#         print(f"my brand name is  {self.brand_name} and the model year is  {self.model_year}")
#     def user_info_2(self):#methods2
#         print("my tata car is working good")
#         self.user_info()
# #syntax
# #objname = classname()
# obj = cars()
# obj.user_info()
# obj.user_info_2()
# print(obj.brand_name)
# print(obj.model_year)


# class Person:
#     def __init__(self, name, age):
#         self.name = name  # Attribute
#         self.age = age    # Attribute

#     def introduce(self):  # Method
#         print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# # Creating an object
# person1 = Person("santosh", 25)
# person1.introduce()

# class mobile_phone(): #class definition 
#     brand_name = "samsung" #attributes
#     color = "white"
#     storage = "256GB"
#     def calling(self):
#         print("you are calling",self.brand_name)
#     def browsing(self):
#         print("you are browsing")
#     def camera(self):
#         print(f"you are capturing a photo from {self.brand_name} storage containing {self.storage}")
# #objname = classname()
# obj = mobile_phone()
# obj.calling()
# obj.camera()
# print(obj.brand_name)
# print(obj.color)
# apple = mobile_phone()
# apple.calling()
# obj_2 = mobile_phone()
# obj_2.browsing()
# obj_2.calling()
# obj_2.camera()




# project - Atm



class ATM:
    def __init__(self, balance=0):
        self.__balance = balance  # Private attribute

    def check_balance(self):
        print(f"Your balance is: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully!")


atm = ATM()  

while True:
    print("\n==== ATM MENU ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")




