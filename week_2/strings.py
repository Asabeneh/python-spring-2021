# What is string - a text data type
# a character or a paragraph

a = 'a'
print(a)
print(len(a))

paragraph = """The   Python Software Foundation (PSF) is a 501(c)(3) non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.
"""
print('Python'.swapcase())
print(len(paragraph))
print(paragraph.upper())
print(paragraph.lower())
print(paragraph.title())
print(paragraph.swapcase())
print(paragraph.replace(' ', '#'))
words = paragraph.split()

# startswith, endswith

print(words)
length = len(words)
print(length)
print(paragraph.startswith('The'))
print(paragraph.endswith('projects.'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name + ' ' +  last_name

print(full_name)
age = 250



print('lETS CHECK THIS', 'two' == 2)


# Casting data types - changing one data type to another

num = 10
gravity = 9.81
print(type(num))
print(float(num))
print(type(gravity))
print(int(gravity))
print(round(gravity))

gravity_str = str(gravity)
print(gravity_str)
print(type(gravity_str))

num_str = '2.5'
num_float = float(num_str)
num_int = int(num_float)
print(type(num_float))
print(type(num_int))

# What is the difference between builtin-funtion and a method

# num = 10.5

# str_with_spaces = '    why to much space every where    '
# print(str_with_spaces.strip())






