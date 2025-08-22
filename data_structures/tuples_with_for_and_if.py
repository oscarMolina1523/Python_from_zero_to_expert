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