# class Student:
#     name = "Hola"


# student1 = Student()

# print(student1.name)


# class Car:

#     # default
#     def __init__(self):
#         pass

#     # Parameterized
#     def __init__(self, fname, age):
#         self.fname = fname
#         self.age = age
#         print(self)
#         print("Hey there")


# car1 = Car("Honda", 33)
# print(car1.fname, car1.age)


# class and instance attributes
# jo chiz haru common hunca ni sabai objects lai teslai chai hamle class attribute vanxan vane jo chis chai farak farak hunxa objects lai teslai chai hamle instance attribute vanxam


# class Student:
#     # This is a class attribute
#     name = "Pasa Engineering College"

#     # This is a default constructor
#     def __init__(self):
#         pass

#     # Parameterized constructor
#     def __init__(self, fname, marks):
#         self.fname = fname  # this is instance attribute
#         self.marks = marks  # this is instance attribute


# student1 = Student("Dude", 99)
# print(student1.fname, student1.marks)

# Methods

# class Student:
#     def __init__(self, fname, cilas):
#         self.fname = fname
#         self.cilas = cilas

#     def hello(self):
#         print(f"Hey welcome to the class {self.fname}.")

#     def get_cilas(self):
#         return self.cilas


# s1 = Student("Pasa", 10)
# s1.hello()
# print(s1.get_cilas())


# Question: Create student class that takes name and marks of 3 subjects as argument in constructor. Then create a method to print the average.


# class Bidyarthi:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello")

#     def get_average(self):
#         sum = 0
#         for mark in self.marks:
#             sum += mark
#         print("Hi", self.name, "your avg score is", sum / 3)


# bidyarthi1 = Bidyarthi("Dude Pasa", [99, 98, 97])
# bidyarthi1.get_average()


# Abstraction - hiding unnecessary details
# Encapsulation - wrapping data and function in single unit (object)

# Question: Create account class with 2 attribute - balance and account_no. Create methods for debit, credit and printing the balance.


# class Account:
#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no

#     def Debit(self):
#         print(
#             f"Your account number {self.account_no} has been debited by 100 and your new balance is {self.balance - 100}."
#         )

#     def Credit(self):
#         print(
#             f"Your account number {self.account_no} has been credited by 100 and your new balance is {self.balance + 100}."
#         )

#     def check_balance(self):
#         print(f"Your account number {self.account_no} has balance {self.balance}.")


# acc1 = Account(10000, 1011)
# acc1.Debit()
# acc1.Credit()
# acc1.check_balance()
