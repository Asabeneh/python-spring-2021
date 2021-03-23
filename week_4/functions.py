# Functions: Builtin functions
# Custom functions
# It is a collection of codes that can perform a single task
# It is better to make a function that solve one problem

# sum()
# len()
# print()
# input('Enter something')



def do_something ():
    return 'I am doing something'


print(do_something())

def add_two_numbers (a, b):
    c = a + b
    return c

print(add_two_numbers(3, 5))
print(add_two_numbers(3, 3))
print(add_two_numbers(1, 1))

# calculate_weight, mass, gravity and it calculates the weight of the object(weight = mass * gravity)

def calculate_weight (mass, gravity = 9.81):
    weight = mass * gravity
    return weight


weight = calculate_weight(75)
print(f'The weight of the object is {round(weight, 1)} N.')


weight = calculate_weight(75, 1.62)
print(f'The weight of the object is {round(weight, 1)} N.')


def sum_all_nums(n):
   total = 0
   for i in range(n + 1):
    total = total + i
   return total

print(sum_all_nums(1000))
print(sum_all_nums(25))


def sum_all_evens(n):
   total = 0
   for i in range(0, n + 1, 2):
    total = total + i
   return total
print(sum_all_evens(100))


def sum_all_odds(n):
   total = 0
   for i in range(1, n + 1, 2):
    total = total + i
   return total

print(sum_all_odds(100))



import random


# def generate_user_id ():
#     pass

# print(2 ** 2)
# print(math.sqrt(2))
# print(2 ** 0.5)
# print(math.pi)
# print()
# print(random.random())

txt = 'abcdefghijklmnopkrstuvwxyz01234589ABCDEFGHIJKLMNOPKRSTUVWXYZ'

# create a function called generate_user_id,
"""I want you to develop a simple script that generate a unique user id.
The length of the unique id is 24 and it may have numbers, lower case and upper case characters only. 
"""

def generate_user_id(n = 6):
    user_id = ''
    length = len(txt) - 1
    for i in range(n):
        index = random.randint(0, length)
        user_id = user_id + txt[index]
    return user_id

print(generate_user_id())
print(generate_user_id())
print(generate_user_id(24))




