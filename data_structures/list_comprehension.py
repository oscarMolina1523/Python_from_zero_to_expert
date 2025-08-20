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