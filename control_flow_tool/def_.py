#the keyword def introduces a function definition. 
# It must be followed by the function name and the parenthesized list of formal parameters.
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
print("Ejecutando def_.py")
# Now call the function we just defined:
fib(2000)

#response
# Ejecutando def_.py
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 15

#second example using array to save the results
# The function fib2 is similar to fib, but it returns the results as a list instead
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

print('Ejecutando def_.py fib2')

print(fib2(100))   # call it
 # write the result
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]