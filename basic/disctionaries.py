dictionary = {'One': 12, 'Two': 2, 'Three': 3, 'Other': [1, 2, 3]}
print(dictionary['One'])
dictionary['One'] = 1
print(dictionary['One'])
dictionary['Four'] = 4
del dictionary['Four']
print(dictionary)

if('Four' in dictionary.keys()):
    print("Four is present.")
else:
    print("Four is not present.")

print(dictionary.values())

for key in dictionary:
    print(key)

