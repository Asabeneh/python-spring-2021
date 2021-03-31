nums = [1, 2, 3, 4]
new_nums = [num * num for num in nums]

print(new_nums)

countries = ['Finland', 'Sweden', 'Denmark', 'Norway','Iceland']
new_nums = [[country, country.upper(),  country.upper()[0:3]] for country in countries]
print(new_nums)

evens = list(range(0, 101, 2))
print(evens)
