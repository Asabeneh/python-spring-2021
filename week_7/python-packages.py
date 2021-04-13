
import numpy as np
import pandas as pd
import webbrowser
import os
import json

import requests
from pprint import pprint

person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

# print(dir(os))
if os.path.exists('./sample.txt'):
    os.remove('./sample.txt')

# os.mkdir('test_folder')
# os.rmdir('test_folder')


print('Numpy version:', np.__version__)
print('Pandas version:', pd.__version__)

lst = [1, 2, 3, 4, 5]
print(lst)
np_arr = np.array(lst)
print(np_arr)

# url = 'https://restcountries.eu/rest/v2/all'
# countries = pd.read_json(url)
# print(countries.head())
# for country in countries.head():
#     print(countries.head(country))

# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://twitter.com/Asabeneh',
#     'https://github.com/Asabeneh',
# ]


# for url in url_lists:
#     webbrowser.open_new(url)

# url = 'https://restcountries.eu/rest/v2/all'

# response = requests.get(url)
# countries = response.json()
# pprint(countries[:2])

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

# txt = requests.get(url).text
# print(txt)

# reading
# f = open('sample.txt')
# lines = f.read().splitlines()
# print(lines)
# for line in lines:
#     print(line)
# f.close()

# writing and updating
# lst_text = ['I love everyone','I love Python too','I love teaching']
# with open('sample.txt', 'a') as f:
#     for txt in lst_text:
#         f.write(txt + '\n')

person_dct = json.loads(person_json)
pprint(person_dct)

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

test_json = json.dumps(person, indent=8)
print(type(test_json))
print(test_json)
