# we will talk about strings
# Stirngs are actually texts

a = 'a'
alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
print(a)
print(type(a))
print(alphabets_lower)
print(type(alphabets_lower))
print(len(alphabets_lower))
print(len(vowels))

number_consonants = len(alphabets_lower) - len(vowels)
print(number_consonants)
alphabets_upper = alphabets_lower.upper()
print(alphabets_upper)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name  + ' ' +  last_name
country = 'Finland'
city = 'Helsink'
mass = 75
height = 175

print(full_name + ' lives in ' + city + ', ' + country +
      ' weighs ' + str(mass) + ' kg and ' + str(height) + ' cm tall.')
      
print(f'{full_name} lives in {city}, {country}. He weighs {mass} and {height} cm tall. ')



# Asabeneh Yetayeh lives in Helsiki, Finland. He weighs 75 kg and 175 cm tall. 

print(full_name)

text = """Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation."""
print(text)
print(len(text))
print(text.split(' '))
print(len(text.split(' ')))
print(text.startswith('Python'))
print(text.endswith('indentation.'))


