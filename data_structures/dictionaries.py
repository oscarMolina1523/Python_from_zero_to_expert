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