# person = {'name': 'Phill', 'age': 22}
# age = person.setdefault('age')
# print('person = ',person)
# print('Age = ',age)


person = {'name': 'Phill'}
salary = person.setdefault('salary')
print('person = ',person)
print('salary = ',salary)
age = person.setdefault('age', 22)
print('person = ',person)
print('age = ',age)