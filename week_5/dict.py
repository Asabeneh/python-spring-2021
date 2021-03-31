# What are dictionaries - >
from pprint import pprint

dct = {
    'kirja':'book',
    'koulu':'school',
    'tietokone':'computer'
}

print(dct)
# kirja  Book
# koulu school
# tietokone computer

print(dct['kirja'])
print(dct['koulu'])
print(dct['tietokone'])

person = {

    "firstName":"Asabeneh",
    'lastName':'Yetayeh',
    'country':'Finland',
    'city':'Helsink',
    'age':250,
    'skills':['HTML','CSS','JS','React']
}


person['nationality'] = 'Ethiopian'

pprint(person)

skills = person['skills']
print(skills[-1])

for skill in skills:
    print(skill)

for key in person:
    print(person[key])



if 'nationality' in person:
    print(person['nationality'])

print(person.get('nationality'))

person['skills'].append('Python')

pprint(person)

for skill in ['Node','Java','D3.js']:
    person['skills'].append(skill)

pprint(person)

# person.pop('city')
# del person['city']
# pprint(person)
# person.popitem()
# person.popitem()
# pprint(person)
pprint(person.items())

for key, value in person.items():
    print(key, value)


keys = person.keys()
print(keys)

values = person.values()
print(values)

