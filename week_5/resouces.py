nums = [1, 2, 3, 4]
# new_nums = [1, 4, 9, 16]

countries = ['Finland', 'Sweden', 'Denmark', 'Norway']
# new_countries = ['FINLAND','SWEDEN','DENMARK','NORWAY']

new_nums = []
for i in nums:
    new_nums.append(i * i)

print(new_nums)

new_countries = []
for i in countries:
    new_countries.append(i.upper())
print(new_countries)
