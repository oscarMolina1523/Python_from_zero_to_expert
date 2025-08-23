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