#tuples are inmutable sequences, but can contain mutable objects
#tuples use parentheses, but they can be created without them
t = 12345, 54321, 'hello!' #tuple without parentheses
print(t[0]) #output: 12345
print(t) #output: (12345, 54321, 'hello!')

#tuples may be nested
u = t, (1, 2, 3, 4, 5) #nested tuple
print(u) #output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))