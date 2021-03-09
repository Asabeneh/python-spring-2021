# Functions - is a set of codes that perform a cetain task
# Builtin functions - made
# Custom functions

# print(), int(), float(), str(), input(), len(), list(), tuple(), dict(), set(), abs(), round(), min (), max(), sum(), dir(),help(), open(), sort(), sorted()


print(2020)
txt = 'I just love Python. Because it is just awesome'
print(txt)
length = len(txt)
print(length)
txt_upper = txt.upper()
txt_title = txt.title()
print(txt_upper)
print(txt_title)

num = 10
num_type = type(num)
print(num_type)
num_float = float(num)
num_str = str(10)
print(type(num_str))

# first_name = input('Enter you name: ')
# print('Your name is ', first_name)
# age = input('Enter your age: ')
# print('You are ' + age + ' years old.')

# Weight of an object, w = mass * gravity

# mass = float(input('Enter your mass: '))
# gravity = float(input('Enter the gravity:'))

# weight = mass * gravity
# print(f'You body weight is {round(weight)} N.')

# List => list of task, shopping list, list vegetables



lang = 'Python'
print(list(lang))
print(abs(-5))

min_value = min(-3, -20, 20, 10, 100)
max_value = max(-3, -20, 20, 10, 100)
total = sum([-3, -20, 20, 10, 100])
print(min_value)
print(max_value)
print(total)


# Mutation -> 

nums = [-1, -2, -1, 10, 11, 2, 3, 4, -5, 6]
# print(nums)
# # print('original:', nums)
# xyz =  nums.sort()
# print(nums)
# print(xyz)

sorted_nums = sorted(nums)
print(nums)
print(sorted_nums)



