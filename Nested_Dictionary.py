# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 12:45:28 2019

@author: Kanel.Soeng
"""

people = {1: {'name': 'Veasna', 'age': '38', 'sex': 'Male', 'status': 'married'},
          2: {'name': 'Thira', 'age': '45', 'sex': 'Male', 'status': 'single'}}

print(people)

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}

del people[3], people[4]
print(people)


people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])

