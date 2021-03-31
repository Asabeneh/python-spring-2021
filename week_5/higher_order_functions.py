
from functools import reduce

# higher order functions are functions that take a function as a parameter or return a fucntion as a parameter

# n * n
# n * n * n 

def make_square (n):
    return n * n
print(make_square(3))
def make_cube (func, n):
    return func(n) * n 
print(make_cube(make_square, 3))

# map, filter, reduce

# Map => [1, 2, 3, 4] => [1, 4, 9, 16]
nums = [1, 2, 3, 4, 50, 20, 50, 20, 20, 3030]
# new_nums = []
# for num in nums:
#     new_nums.append(num ** 2)
# print(new_nums)

# new_nums = [ num ** 2 for num in nums]
# print(new_nums)

test_lam = lambda num: num ** 2
new_nums = list(map(test_lam, nums))
print(new_nums)
countries = ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
new_countries = list(map(lambda country: [country, country.upper(), country.upper()[:3]], countries))
print(new_countries)

# filter 
odds = list(filter(lambda num: num % 2 != 0, nums))
print(
odds
)

print(reduce(lambda acc, curr: acc + curr, nums))

xyz = lambda x, y, z: 2 * x + y + z

print(xyz(2, 3, 4))

for i in range(10):
    print(i


