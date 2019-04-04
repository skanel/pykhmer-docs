# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:46:57 2019

@author: Kanel.Soeng
"""

my_dict = {
            "key1":"value1", 
            "key2": "value2"
           }
my_dict
my_dict["key1"]

fruits = {"Apple": 3, "Banna": 1.75, "Cherry": 2}
fruits
fruits["Cherry"]

# 2) Dictionaries with all data type's
new_dict = {
            "k1":147,
            "k2":[15, 25, 35],
            "k3":{"Apple":3}
            }
new_dict
new_dict["k2"]
new_dict["k2"][1]
new_dict["k3"]
new_dict["k3"]["Apple"]

# PRACTISE 
customer_info = {
                "salary": 300, 
                 "age": 40, 
                 "children": {"name": "sopheak", "sex": "male"},
                 "account_start_date": 20190130,
                 "family_number":["Mr.A", "M.B", "Miss.C"],
                 #........
                 #........
                 #....etc...
                }


d = {"students": ["a", "b","c","d"]}
d
d["students"][1]
d["students"][1].upper()
d["students"][1].lower()

# 3) Add values
d = {"k1":100, "k2":200}
d["k0"] = 300
d

# 4) Replace values

d["k1"] = "New One"
d

d.keys()
d.values()
d.items


# 1) Define a Dictionary
# 2) Dictionaries with all data type's 
# 3) Add values 
# 3) Replace values
# 5) Keys, Values and Item's retrieval 

# Exercise: 30min

str = "awesome This is an awesome occation. This has never happend before."

char_occurances = {} #empty dict
for char in str:
    char_occurances[char] = char_occurances.get(char, 0)+1
print(char_occurances)



word_occurances = {}

for word in str.split():
    word_occurances[word] = word_occurances.get(word, 0)+1
    
print(word_occurances)


for (key, value) in char_occurances.items():
    print(f"{key} {value}")

for key in char_occurances.keys():
        print(key)
for val in char_occurances.values():
    print(val)