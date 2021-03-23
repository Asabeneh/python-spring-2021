# Numbers, Strings, Boolean, List, Set, tuple and dictionary

# Set

st = set()
print(st)

nums = {1, 2, 3, 4, 5, 5, 4,4,1}
print(nums)
print('check lenght', len(nums))

for num in nums:
    print(num)

nums.add(6)
print(nums)
nums.update((7,8,9,10))

print(1 in nums)
print(nums)
fruits = {'banana', 'orange', 'mango', 'lemon'}
# if 'avocodo' in fruits:
#     fruits.remove('avocado') 

fruits.pop()

print(fruits)
