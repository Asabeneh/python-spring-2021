# what is loop?
# it is a process to solve some repetitive task

print('Hello, World!', 1) # please print this 1000 times before the break

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)


countries = ['Finland', 'Sweden', 'Norway', 'Denmary']

for i in countries:
    print(i.upper())


nums = list(range(10))
print(nums)

for num in nums:
    print(num)


for i in range(10):
    print(i)

# What is the sum of all numbers from 0 to 100 , 5050, 4950
# wHAT IS the sum of all even numbers from 0 to 100, 2550
# What is the sum of all odds from 0 to 100,2500 

sum_of_all = 0
for i in range(101):
    sum_of_all = sum_of_all + i
print('The sum of all numbers is', sum_of_all)
  

evens_sum = 0
for i in range(0, 101, 2):
    evens_sum = evens_sum + i
print('The sum of all evens is', evens_sum)

odds_sum = 0
for i in range(1, 101, 2):
    odds_sum = odds_sum + i
print('The sum of all odds is', odds_sum)

"""I want you to develop a simple script that generate a unique user id.
The length of the unique id is 24 and it may have numbers, lower case and upper case characters only. 
"""


for i in range(6):
    print(i)
else:
    print(i, 'This is the end of the iteration')

## break and continue
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# continue to skip 
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)

# break - to terminate or stop the iteration

for i in range(6):
    print(i)
    if i == 3:
        break
    
# While loop
print('This is the while loop part')
count = 0
while count < 6:
    print(count)
    count = count + 1

count = 5
while count >= 0:
    print('lets test', count)
    count = count - 1
   

for i in range(5,-1,-1):
    print(i)



countries_with_land = []
countries_without_land = []
countries_with_way = []

for country in countries:
    if 'land' in country and len(country.split(' ')) == 1:
        print(country.split(' '))
        countries_with_land .append(country)
    elif 'way' in country:
        countries_with_way.append(country)
    else:
        countries_without_land.append(country)

print(countries_with_land)
print(countries_with_way)



