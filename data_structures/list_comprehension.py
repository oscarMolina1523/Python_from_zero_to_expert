#FIRST CASE OF STUDY
#create an empty list
squares = []
#execute a for loop to append the square of each number from 0 to 9
for x in range(10):
    #append the square of x to the list
    squares.append(x**2)
#using this method we have a problem
#the var x exists outside the loop
#the var x that still exists after completing the loop
print(squares)
#output
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#SECOND CASE OF STUDY
#using list comprehension we can create the same list in a single line
#first we create the list using the [list] keyword 
# to save the result of the comprehension
squares2 = list(
    map( #using the map function to applies a function to each element of an iterable
        lambda x: x**2, #Lambda is an anonymous function: it receives a value (x) and returns x squared
        range(10) #range(10) generates numbers from 0 to 9
    )
)


print(squares2)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]