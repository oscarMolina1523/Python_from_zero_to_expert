#create a list of numbers
a = [-1, 1, 66.25, 333, 333, 1234.5]
#using [del] instruction to remove the first element of the list
del a[0] #the number in position 0 is -1
print(a) #output: [1, 66.25, 333, 333, 1234.5]

del a[2:4] #removes the elements in positions 2 and 3
print(a) #output: [1, 66.25, 1234.5]

del a[:] #removes all elements in the list
print(a) #output: []

del a #deletes the list completely
#print(a) #this will raise an error because the list no longer exists
#but you can add a new value to a