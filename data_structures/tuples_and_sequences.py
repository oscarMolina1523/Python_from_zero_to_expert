#tuples are inmutable sequences, but can contain mutable objects
#tuples use parentheses, but they can be created without them
t = 12345, 54321, 'hello!' #tuple without parentheses
print(t[0]) #output: 12345
print(t) #output: (12345, 54321, 'hello!')

#tuples may be nested
u = t, (1, 2, 3, 4, 5) #nested tuple
print(u) #output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

#tuples are inmutables, you cannot modify them
# t[0] = 88888 
# #if you want do this, you will get an error
#Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment

#but they can contain mutable objects, like lists
v = ([1, 2, 3], [3, 2, 1]) #tuple using parentheses
print(v) #output: ([1, 2, 3], [3, 2, 1])

#you can create tuples empty or with one item
#in case of one item, you need to add a comma after the item
empty = () #empty tuple
singleton = 'hello', #tuple with one item, note the comma
print(len(empty)) #output: 0
print(len(singleton)) #output: 1