# List: is a collection of different or the same data types in an ordered way.



nums = [1, 2, 3, 4, 5]

#       0  1   2  3, 4
print(nums)
print(len(nums))
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[-1])
print(nums[-2])
nums[0] = 10
print(nums)

nums[1] = 22

print(nums)

last_index = len(nums) - 1

nums[last_index] = 555
print(nums)

nums.append(6)
print(nums)
nums.extend([7, 8, 9, 10, 0,-5])
print(nums)

new_list = [1, 2, 3, 4, 5, 6]

print(new_list)
print(new_list[-3:])

print(5 in new_list)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2,'Apple')

print(fruits)
fruits.insert(-1, 'Lime')
print(fruits)

fruits.remove('mango')
print(fruits)






# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a  + b
# print(c)

# shopping_list = ['Avocado','Mango','Honey','Coffee','Tea', 'Sugar','Meat','Milk']

# syntax
lst = ['item1', 'item2']
lst = []
print(lst)

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits_copy = fruits.copy()
fruits_copy.append('Apple')

print(fruits)
print(fruits_copy)



a = 5
b = a

b = a * 5
print(b)

new_list = [1, 2,25, 3, -2, 4, 10, 5, 6]

new_list.reverse()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
sorted_list = sorted(new_list)