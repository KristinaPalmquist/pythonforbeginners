# print('Hello World')
# print('Kristina Palmquist')
# print('o----')
# print(' ||||')
# print('*' * 10)
# print('o' + '-' * 4)
# print(' ' + '|' * 4)



# print('  __  __ ')
# print(' /  \/  \\')
# print('|        |')
# print(' \      /')
# print('  \    / ')
# print('    \/  ')


# simple values
# price = 10
# rating = 4.9

# full_name = 'John Smith'
# age = 20
# is_new_patient = True
# print(price)

# name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print('Hello ' + name + ', your favorite color is ' + color)

# complex values
# patient = {
#     'name': 'John Smith',
#     'age': 20,
#     'is_new_patient': True
# }

# print(patient['name'])


# birth_year  = input('Birth year: ')
# age = 2025 - int(birth_year)
# print('Your age is ' + str(age))

# print(type(birth_year))
# print(type(age))

# weight_lbs = input('What is your weight? (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print('Weight in kg: ' + str(weight_kg))

# strings + index
# course = 'Python\'s for "Beginners"'
# new_course = "Python's for Beginners"
# third_course = '''
# Python
# for

# "Beginners"'''
# print('Welcome to ' + third_course + '!')
# print(course[-2])
# print(course[0:3]) # print first three characters
# print(course[1:]) # print from startindex to end
# print(course[:3]) # print from start to endindex
# print(course[:]) # print from start to end
# print(course[0:len(course)]) # print from start to end
# print(course[0:10:2]) # print from start to end with step (every other character)
# print(course[::2]) # print from start to end with step (every other character)
# print(course[::-1]) # print from end to start

# name  = 'Jennifer'
# print(name[1:-1]) # print from startindex to endindex - ennife

#formatted strings
# first = 'Kristina'
# last = 'Palmquist'
# message = first + ' [' + last + '] is a coder' # string concatenation
# msg = f'{first} [{last}] is a coder' # formatted string
# print(msg)

# course = ' Python for Beginners '
# # general purpose function
# print(len(course)) # length of string
# # string methods
# print(course.upper()) # convert to uppercase
# print(course.lower()) # convert to lowercase
# print(course.find('B')) # find index of first occurrence of character, case sensitive
# print(course.replace('Beginners', 'Experts')) # replace character
# print(course) # print original string
# print(course.title()) # convert to title case
# print(course.strip()) # remove whitespace from start and end
# print(course.split()) # split string into list of words
# print(course.split('o')) # split string into list of words with separator
# print(course.split(' ')) # split string into list of words with separator
# print('Python' in course)
# print('python' in course)

# print(10 + 3)
# print(10/3)
# print(10//3) # floor division - gives integer value
# print(10 % 3) # modulus
# print(10 ** 3) # exponentiation -  10^3
# print(round(10/3)) # round to nearest integer

# x = 10
# x = x + 3
# print('x = ' + str(x))
# y = 10
# y += 3 # shorthand for y = y + 3 - augmented assigment
# print(f'y = {y}')
# z = 10 + 3 * 2 ** 2
# print('z = ' + str(z))

# x = (2 + 3) * 10 - 3
# print('x = ' + str(x))

# x = 2.9
# y = -2.9
# print(round(x)) # round to nearest integer
# print(abs(y)) # absolute value

# import math
# x = 2.9
# y = -2.9
# print(math.floor(x)) # round down to nearest integer
# print(math.ceil(x)) # round up to nearest integer

# is_hot = True
# is_cold = True

# if is_hot:
#     print('It is a hot day')
#     print('Drink plenty of water')
# elif is_cold:
#     print('It is a cold day')
#     print('Drink hot chocolate')
# else:
#     print('It is a lovely day')

# print('Enjoy your day')

# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price

# if len(str(down_payment)) > 6:
#     print('Down payment: ${:,.2f}'.format(down_payment))
# else:
#     print('Down payment: ${}'.format(down_payment))

# price = 1000000
# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
# if has_good_credit and has_high_income:
#     print('Eligible for loan')
# elif has_good_credit or has_high_income:
#     print('Eligible for loan with conditions')
# else:
#     print('Not eligible for loan')
# if has_good_credit and not has_criminal_record:
#     print('Eligible for loan')


# temperature = 35
# if temperature > 30:
#     print('It is a hot day')
# elif temperature == 20:
#     print('It is a nice day')
# else:
#     print('It is a cold day')

# name = input('What is your name? ')
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 50:
#     print('Name can be a maximum of 50 characters')
# else:
#     print('Name is valid')
# first_name = input('What is your first name? ')
# while len(first_name) < 3 or len(first_name) > 50:
#     print('Name must be 3 - 50 characters')
#     first_name = input('What is your first name? ')
# print('First name is valid!')

# name = 'John'
# print(len(name))

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# unit = unit.upper()
# if unit == 'L':
#     converted = weight * 0.45
#     print(f'Weight in kg: {converted}' )
# elif unit == 'K':
#     converted = weight / 0.45
#     print(f'Weight in lbs: {converted}')

# i = 1
# print('           ')
# print('  Merry   ')
# while i <= 5:
#     print(' ' * (5 - i) + '*' * i * 2)
#     i += 1
# print('*  X-mas! *')

#for-loops
# for i in range(5):
#     print(i + 1)
# print('Done')

# for item in 'Python':
#     print(item)

# for item in ['Python', 'Java', 'C++']:
#     print(item)

# for i in range(2, 10, 3):
#     print(i)

# prices = [10, 20, 30]
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for price in prices:
#     sum += price
#     for number in numbers:
#         print(f'{sum}: {number}')

# print(f'Sum: {sum}')

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     print('*' * i)


# numbers = [5, 2, 5, 2, 2]
# string = ''
# for i in numbers:
#     for x in range(i + 1):
#         string = '*' * x
#     print(string)
#     string = ''

# numbers = [2, 2, 2, 2, 5]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)

# names = ['John', 'Sarah', 'Mary', 'Rut', 'Harry']
# print(names)
# print(names[-2:])
# # for name in names:
# #     print(name)
# names[0] = 'Jon'
# print(names)



# # two dimensional list

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# matrix[1][1] = 20
# print(matrix[0])
# print(matrix[1][1])

# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [4, 6, 7, 2, 3]
# numbers.append(21)
# print(numbers)
# numbers.insert(3, 156) # index, value
# print(numbers)
# numbers.remove(6) # value, not index
# print(numbers)
# numbers.pop(4) # index
# print(numbers)
# # numbers.clear()
# # numbers.pop() # removes last
# print(numbers.index(21)) # returns index of first occurrence of value
# print(numbers)
# print(50 in numbers) # returns boolean, not error
# numbers.insert(1, 21)
# print(numbers.count(21))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(10)
# numbers2.append(8)
# print(numbers2)

# # tuples
# # like lists but immutable, we can't mutate or change them, only get information
# # numbers = [1, 2, 3] # list
# numbers = (1, 2, 3) # tuple
# print(numbers.count(1))
# print(numbers.index(1))
# print(numbers[-1])

# # unpacking
# coordinates = (1, 2, 3)
# # print(coordinates[0] * coordinates[1] * coordinates[2])
# # x = coordinates[0]
# # y = coordinates[1]
# # z = coordinates[2]
# # print(x*y*z)
# x, y, z = coordinates
# print(x * y * z)
# numbers = [4, 5, 7]
# x, y , z = numbers
# print(x, y, z)

# # dictionary
# # key value pairs
# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }

# print(customer)
# print(customer['name']) # returns error
# print(customer.get('name')) # returns None
# print(customer.get('Name', 'John Doe')) # returns default value
# customer['name'] = 'Jack Smith'
# print(customer)
# customer['birthdate'] = 'Jan 1 1980'
# print(customer)


# functions
# def greet_user(name):
#     print(f'Hi {name}!')
#     print('Welcome aboard')
# from greet_user import greet_user

# def greet_user(first_name, last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')

# print('Start')
# greet_user('Anna', 'Johnson') # positional argumnents
# greet_user(last_name = 'Smith', first_name = 'Jack') # keyword arguments
# print('Finish')


# def square(number):
#     # return number * number
#     return number ** 2


# print(square(4))
# result = square(int(input('>')))
# print(result)

#exceptions
# age = int(input('Age: '))
# print(age)

# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError: # exception - crashes program
#     print('Invalid value')
# except ZeroDivisionError:
#     print("0 is not a valid age")
# print('Done')


# # Classes
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print('Move')
#     def draw(self):
#         print('Draw')


# # point1 = Point()
# # point1.x = 10
# # point1.y = 21
# # point1.draw()
# # point1.move()
# # print(point1.x)

# # point2 = Point()
# # point2.x = 23
# # point2.y = 14
# # print(point2.y)
# point = Point(14, 21)
# point.x = 13
# print(point.x)


# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         # return (f'Hello my name is {self.name}!')
#         # print('talk')
#         print(f'Hello my name is {self.name}!')


# me = Person('Kristina Palmquist')
# # print(me.name)
# me.talk()
# bob = Person('Bob Smith')
# bob.talk()


# #inheritance
# class Mammal:
#     def walk(self):
#         print('Walk')


# class Dog(Mammal):
#     def bark(self):
#         print('Bark')


# class Cat(Mammal):
#     def meow(self):
#         print('Meow')


# h = Dog()
# h.walk()
# h.bark()

# k = Cat()
# k.walk()
# k.meow()


# # #modules
# # # import converters
# # # print(converters.kg_to_lbs(80))

# # from converters import  kg_to_lbs
# # print(kg_to_lbs(100))

# import utils
# numbers = [37, 45, 1, 2, 89, 56, 3, 4, 128, 7, 5, 38, 43, 6, 7, 789, 8, 9]
# # utils.find_max(numbers)
# # utils.find_min(numbers)
# print(utils.find_max(numbers))
# print(max(numbers))

# # Packages
# # import ecommerce.shipping
# # ecommerce.shipping.calc_shipping()

# # from ecommerce.shipping import calc_shipping
# # calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()

# # built in modules
# # search online for: python 3 module index
# import random
# import math
# # for i in range(3):
# #     print(f'{i + 1}: {math.floor(random.random() * 100)}%')
# #     print(random.randint(1, 100))
# # members = ['John', 'Jack', 'Sarah', 'Mary Celeste']
# # leader = (random.choice(members))
# # print(leader)

# import dice

# # die1 = dice.Dice()
# # die2 = dice.Dice()
# # print(f'({die1.roll()}, {die2.roll()})')
# # print(type(die1.numbers))
# dice = dice.Dice()
# roll1 = dice.roll()
# print(roll1)



# # Files and directories
# from pathlib import Path
# import os
# # absolute path
# # /usr/local/bin/...

# # relative path
# path1 = Path("ecommerce")
# # print(path1.exists())
# path2 = Path('email')
# # print(path2.mkdir())
# # print(path2.rmdir())
# path3 = Path()
# print(path3)
# for file in path3.glob('*'):
#     print(file)


# PyPI and Pip
# Standard Python library + 
# PyPI - Python Package Index - packages built by users
# 
