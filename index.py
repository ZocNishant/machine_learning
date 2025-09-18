from math import *

# print("Pasa K xa. I am back")

# Variables and Datatypes
# name = "John"  # String
# age = 22  # Number

# is_float = 7.0886  # Float
# is_boolean = True  # Boolean
# what_is_this = 1j  # Complex

# print(f"Hey {name}. How are you doing?")
# print(f"He is {age} years old.")
# print(f"{name} is all set to go. Hehohahaha")
# print(type(name))
# print(type(age))
# print(type(is_float))
# print(type(is_boolean))
# print(type(what_is_this))

# Working with strings.
# phrase = "Hey this is a string and this is how you can store it in a variable."

# print(
#     phrase.upper()
#     + 'Hey, this is a string. \n String can be written like this. "Hehohahah"'
# )

# print(phrase.isupper())
# print(len(phrase))
# print(phrase[5:-1])
# print(phrase.index("H"))
# print(phrase.replace("Hey", "Whats Upppp"))

# Working with numbers
# number1 = 57
# number2 = -73

# print(number1 * (number2 + 4))
# print(number2 % number1)
# print(str(number1) + " Hehohaha")

# print(abs(number2))
# print(pow(3, 2))
# print(max(3, 4, 7, 9))
# print(min(3, 4, 7, 9))
# print(round(3.7657))
# print(floor(4.9867))
# print(ceil(89.9783))
# print(sqrt(99))


# Getting input from a user

# getting_name = input("What is your name?? ")
# getting_age = input(f"How old are you {getting_name}?? ")
# print(f"Hi! {getting_name}. You are {getting_age} years old.")


# Building a basic calculator
# Hawa program

# input_one = int(input("Enter the first number: "))
# input_two = int(input("Enter the second number: "))

# more_number = input("Do you want to enter more number? ")

# if more_number == "yes":
#     input_three = int(input("Enter the third number: "))
# else:
#     input_three = 0
#     print("Lets compute.")

# print(input_one + input_two + input_three)


# Mad Libs Game

# color = str(input("Which color do you like in you happy birthday?? "))
# flower_bhan = str(input("Which flower do you like in you happy birthday?? "))
# pasa_ko_ho = str(input("Who do you like in you happy birthday?? "))

# print(f"Roses are {color}.")
# print(f"{flower_bhan} are blue.")
# print(f"I loppa {pasa_ko_ho}.")

# Lists (Yo bhaneko chai array ho javascript ko. (just samjine tarika mero lagi))

# fruits = ["Apple", "Banana", "Canelope", "Dragon Fruit", "Eggplant", "Fig", "Grapes"]

# print(type(fruits))
# print(fruits[0])
# print(fruits[-1])
# print(fruits[2:4])
# print(fruits.append)

# fruits[-1] = "Hehehe"
# print(fruits)

# List Functions

# lucky_numbers = [1, 2, 3, 6, 7, 8, 9]
# khane_kuro = [
#     "Apple",
#     "Banana",
#     "Canelope",
#     "Dragon Fruit",
#     "Eggplant",
#     "Fig",
#     "Grapes",
# ]

# khane_kuro.insert(1, "Bamboo")
# print(khane_kuro)

# khane_kuro.append("Holly")
# print(khane_kuro)

# khane_kuro.extend(lucky_numbers)
# print(khane_kuro)

# khane_kuro.remove("Holly")
# print(khane_kuro)


# Tuples - Immutable

# first_tuple = ("Hehe", 1, "Hoho", 2)
# print(first_tuple[2])

# Functions


# def sayHello(a, b):
#     print(f"Hi! {a}, Hi! {b}.")


# sayHello("Nishant", "Pasa")
# sayHello("Sani", "Pasa")
# sayHello("Thuli", "Pasa")


# Return Statement


# def cube_a_number(a):
#     return a * a * a


# result = cube_a_number(3)
# print(result)


# If Statements

# is_Male = True

# if is_Male:
#     print("Male Vai.")
# else:
#     print("Baini")

# Largest of 3 numbers

# num_one = int(input("Enter the first number: "))
# num_two = int(input("Enter the second number: "))
# num_three = int(input("Enter the third number: "))

# if num_one > num_two and num_one > num_three:
#     print(f"{num_one} one is the largest.")
# elif num_two > num_one and num_two > num_two:
#     print(f"{num_two} two is the largest.")
# else:
#     print(f"{num_three} three is the largest.")
# print("Done")


# Better Calculator


# def calculator(digit_1, digit_2, operator):
#     if operator == "+":
#         return digit_1 + digit_2
#     elif operator == "-":
#         return digit_1 - digit_2
#     elif operator == "/":
#         return digit_1 / digit_2
#     elif operator == "*":
#         return digit_1 * digit_2
#     else:
#         return "Something is wrong."


# result = calculator(2, 3, "+")
# print(result)


# Dictionaries

# example_dict = {"name": "Nishant", "age": 24}

# print(example_dict["name"])

# While Loop

# i = 1

# while i <= 15:
#     print(i)
#     i += 1
# print("Done with the loop.")

# Guessing Game

# secret_word = "Khatarnak"
# guess = ""
# number_of_guess = 0
# lives = 5
# out_of_guesses = False


# while guess != secret_word and not (out_of_guesses):
#     if number_of_guess < lives:
#         guess = input("Enter your guess. ")
#         number_of_guess += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("You lose.")
# else:
#     print("You win.")


# for loop

# for letter in "Pasa k xa yar.":
#     print(letter)


# falfuls = ["Apple", "Banana", "Canelope", "Dragon Fruit", "Eggplant", "Fig", "Grapes"]

# for falful in falfuls:
#     print(falful)


# i = 10

# for digit in range(i):
#     if digit == 0:
#         print("Yeah Buddy.")
#     else:
#         print(digit)

# Exponent Function


# def raise_to_power(base_num, power_num):
#     result = 1
#     for index in range(power_num):
#         result *= base_num
#     return result


# print(raise_to_power(5, 9))


# 2D List and Nested Loop

# grid_number = [["K xa", "Hehiaha"], [1, 2, 3], ["hehe"]]

# print(grid_number[1][2])

# for index in grid_number:
#     for vitra in index:
#         print(vitra)

# Build a translator


# phrase = input("Enter the phrase you like: ")


# def translate(info):
#     result = ""
#     for letter in info:
#         if letter in "AEIOUaeiou":
#             result += "g"
#         else:
#             result += letter
#     return result


# print(translate(phrase))


# Try..Except

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("No pasa no")
# except ValueError:
#     print("Na baba na.")

# Reading from external files
