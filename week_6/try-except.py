# try:
#     birth_year = int(input('Enter birth year:'))
#     current_year = int(input('Enter current year:'))
#     age = current_year - birth_year
#     print(age)
# except:
#     print('Something goes wrong')

from math import pi
import math

from find_most_common_words import find_most_common_words as fmcw
try:
    print(int('a'))
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
finally:
    print('I always run whatever the case.')

sample_list = ('Asabeneh','Programmer', 250, 'Finland')

first_name, job, age, country = sample_list
print(first_name)
print(job)
print(age)
print(country)

# that sum all numbers

def sum_all(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total
 
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

fin, swe, nor, *rest = countries
print(fin)
print(swe)
print(nor)
print(rest)


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
# Asabeneh lives in Finland, Helsinki. He is 250 years old.
print(unpacking_person_info(**dct))
dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}

print(tuple(dct.values()))


print(fmcw('i love js. Do not love it', 2))
 
