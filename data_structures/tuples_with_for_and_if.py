#create a list of numbers negatives and positives
vec = [-4, -2, 0, 2, 4]

#create a new list with the numbers multiplied by 2
double=[x*2 for x in vec]
print(double) #output: [-8, -4, 0, 4, 8]

#create a new list with the numbers that are greater than or equal to 0
# in simple words, filter the list to get only the positive numbers
positives=[x for x in vec if x >= 0]
print(positives) #output: [0, 2, 4]

#abs is a function to count the spaces between the number and 0
absolute=[abs(x) for x in vec]
print(absolute) #output: [4, 2, 0, 2, 4]

#create a list of fruits with spaces at the beginning and end
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

#strip() function removes spaces at the beginning and end of each string
#only start or end , not in the middle
fruits_without_spaces=[fruit.strip() for fruit in freshfruit]
print(fruits_without_spaces) #output: ['banana', 'loganberry', 'passion fruit']

#double tuple with for loop and range function
doble_tuple=[(x, x**2) for x in range(6)]
print(doble_tuple) #output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#sintax error, be careful with the indentation
#you cannot do this
#you need to put the parentheses like the line over this one [(x, x**2)]
error=[x, x**2 for x in range(6)]
#print(error) #output:  File "<stdin>", line 1
#     [x, x**2 for x in range(6)]
#      ^^^^^^^
# SyntaxError: did you forget parentheses around the comprehension target?