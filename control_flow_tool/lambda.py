#create a function that returns a function
#this receives a number and returns a function that adds that number to its argument
def make_incrementor(n):
    #this is a lambda function that takes an argument x and adds n to it
    return lambda x: x + n #here n is captured from the make_incrementor function's scope
                           #return a function like this: f(x) = x + n |<--n is the captured variable
                           #in the next line n=42, so the returned function will be f(x) = x + 42

f = make_incrementor(42) #here return the function: f(x) = x + 42
print(f(0)) #here is passing 0 to the function f(x) = x + 42, so it will return 42
#response
#42
print(f(1)) #here is passing 1 to the function f(x) = x + 42, so it will return 43
#response
#43