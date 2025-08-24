import fibo
#other form to import specific functions
#from fibo import fib, fib2
#or import all functions
#from fibo import *

print(fibo.fib(1000))
print(fibo.fib2(1000))

#__name__ variable is for know the name of the module
print(fibo.__name__)  # prints 'fibo'

#if you want to use a function with frequency, you can assign it to a local name
fib = fibo.fib
fib(500)