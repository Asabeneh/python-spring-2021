# What is object ?
# Table, Car, Dog, Animal, Person, anything 

class Person:
    def __init__(self, firstName, lastName, age, country):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age 
        self.country = country
        self.skills = []
    def get_person_info(self):
        return f'I am {self.firstName} {self.lastName}. I am {self.age} years old. I live in {self.country}.'
    def add_skill(self, skill):
        self.skills.append(skill)
    def get_skills(self):
        return self.skills



p = Person('Asabeneh','Yetayeh', 250, 'Finland')
print(p.firstName, p.age)
print(p.get_person_info())

for skill in ['HTML','CSS','JS','React','PYTHON']:
    print(p.add_skill(skill))
print('my skills are', p.get_skills())



class Student(Person):
    def __init__(self, firstName, lastName, age, country):
        super().__init__(firstName, lastName, age, country)
        self.hobbies = []
    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
    def get_hobbies(self):
        return self.hobbies
    

s = Student('Eyob','Shitahun',250, 'Finland')
print(s.get_skills())
print(s.get_person_info())
s.add_skill('React')
s.add_skill('Node.js')
s.add_skill('Python')
print(s.get_skills())

s2 = Student('John', 'Doe', 25, 'UK')
print(s2.get_person_info())
print(s2.get_skills())
print(s2.get_hobbies())
s2.add_hobby('Hiking')
s2.add_hobby('teaching')
s2.add_hobby('inspiring')
print(s2.get_hobbies())


