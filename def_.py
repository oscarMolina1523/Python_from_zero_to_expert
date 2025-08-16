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