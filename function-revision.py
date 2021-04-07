# functions a set of code that solve a single task
# it is easy to use, test, reuse
# you make a function, addTwo(a, b) => a + b
# How to make function

def do_something():
    return 'I am doing something'

print(do_something())

def greet_people(name):
    return f'Hello, {name}!'

print(greet_people('Eero'))
print(greet_people('Asab'))

def make_square(n):
    return n ** 2

print(make_square(2))

# x^2 + 6x + 9 => x2 + 3x + 3x + 9 => (x+ 3)(x + 3) => {-3}
# x^2+ 3x + 2
def solveQuadraticEqn(a, b, c):
    d = b ** 2 - 4 * a * c
    solnSet = set()
    if d == 0:
        s1 = (-b) /(2 * a)
        solnSet.add(s1)
        return solnSet
    elif d > 0:
        s1 = (-b - (d ** 0.5)) / (2 * a)
        s2 = (-b + (d ** 0.5)) / (2 * a)
        solnSet.add(s1)
        solnSet.add(s2)
        return solnSet
    elif d < 0:
        solveQuadraticEqn
    else:
        'Invalid'

print(solveQuadraticEqn(1, 6, 9))
print(solveQuadraticEqn(1, 3, 2))  # x^2+ 3x + 2

#LAMBDA Function -> Anonymous function, a nameless function, a function withutname

nums = [1, 2, 3, 4, 5] # 1, 4, 9, 16, 25


newNums = list(map(lambda num : num ** 2, nums))
print(newNums)

countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

newCountries = list(
    map(lambda country: [country.upper(), country.upper()[:3]], countries))
print(newCountries)

c= [[country.upper(), country.upper()[:3]] for country in countries]
print(c)

b = 3
print('Lets after this ----')
for i in range(10):
    if i != 0:
        print(b / i)

