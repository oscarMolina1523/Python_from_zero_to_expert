#create a functiion, it receives two arguments, one is mandatory and one with a default value
#and returns a string 
def f(ham: str, eggs: str = 'eggs') -> str:
    #you can access the annotations of the function using the __annotations__ attribute
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    #that concatenates the two arguments
    return ham + ' and ' + eggs

#example of how to call the function
f('spam')

#response
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'