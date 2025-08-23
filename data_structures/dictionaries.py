#create a dictionary
#dictionaries are mutable mappings, they map keys to values
tel = {'jack': 4098, 'sape': 4139}

#you can add a new item
tel['guido'] = 4127
print(tel) #output: {'jack': 4098, 'sape': 4139, 'guido': 4127}

#tou can receive the value of a key
print(tel['jack']) #output: 4098

#you can delete an item by its key
del tel['sape'] #sape is the key
print(tel) #output: {'jack': 4098, 'guido': 4127}

#you can create a list with the keys of a dictionary
#by default, iterating a dictionary iterates over its keys
print(list(tel)) #output: ['jack', 'guido']
print(list(tel.keys()))   # ['jack', 'guido']
print(list(tel.values())) # [4098, 4139]
print(list(tel.items()))  # [('jack', 4098), ('guido', 4139)]

#you can sort the keys of a dictionary
print(sorted(tel)) #output: ['guido', 'jack']

#validate if a key is in a dictionary
print('guido' in tel) #output: True 
print('jack' not in tel) #output: False because jack is in tel