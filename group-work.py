# builtin-functions

print('i just love python')
print(len('Python'))
print(type(10))


print(abs(-10))
print(round(9.81))
print(max(1, 3, 2, 5, -5))
print(min(1, 3, 2, 5, -5))
print(sum([1, 3, 2, 5, -5]))


'''
the comment 
goes in here
in multiple lines
'''

# Data types: Number(Int, Float, Complex), String, Boolean, List, Set, Tuple, Dictionary


age = 250
gravity = 9.81
cpx = 1 + 1j
lang = 'Python'
is_married = True
is_light_off = False


fruits_list = ['Mango','Avocado','Orange','Apple','Banana']

nums_set = {-3, -2, -1, 0, 1, 2, 3} # list of integers

nums_tuple = (-3, -2, -1, 0, 1, 2, 3)  # list of integers

countries = {
    'name':'Finland',
    'city':'Helsinki',
    'population':5.6
}

# Set: is a collection of things or items
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

# birth_year = int(input('Enter birth year: '))
# current_year = int(input('Enter the current year: '))

# age = current_year  -  birth_year

# print(f'Your are {age} years old.')

# Enter your mass: 100
# Your weight is 98.1 N.

# mass = float(input('Enter your mass: '))
# gravity = float(input('Gravity: '))

# weight = mass * gravity

# print(f'Your weight is {round(weight, 1)} N.')

print('Python ' + 'For ' + 'Everyone')

company = 'BCoding For AllB'

print(company[0])
print(company[13])
print(company[-1])
# print(company.index('z'))

if 'z' in company:
    print('do something')

print(company.replace('Coding','Python'))
print(company.split(' '))

acronym = ''
for word in company.split(' '):
    acronym += word[0]

print(acronym)

print(company.index('o'))

print(company.rfind('B'))
