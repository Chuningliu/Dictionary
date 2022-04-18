# person={'name':'jack','age':20,'gender':'male',4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4],x,result)

# get()
person={'name':'jack','age':20,'3':'female',4:{'organisation':'navgurukul','place':'dharamsala'}}
# print(person['gender'])
# print(person[4])
# b=(person['gender'])
# print(b)
# result = person[4]['place']
# print(result)
values = person.values()
values_list = list(values)
a_value = values_list[0]