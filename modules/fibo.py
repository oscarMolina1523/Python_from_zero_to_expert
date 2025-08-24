# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        #we need to put end=' ' in print because by default print adds a newline
        #if we don't put it, all numbers will be printed in different lines
        #with this we say print in the same line with a space
        print(a, end=' ')
        a, b = b, a+b
    #this print is to add a newline at the end of the series
    #because we have end=' ' in the previous print by default
    #so we need to add a newline at the end of the series
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result