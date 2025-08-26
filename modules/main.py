import fibo
#other form to import specific functions
#from fibo import fib, fib2

#or import all functions
#from fibo import *

#you can rename the module or give an alias using 'as'
#import fibo as fib
#fib.fib(500)

#you can combine both
#from fibo import fib as fibonacci, fib2 as fibonacci2


print(fibo.fib(1000))
print(fibo.fib2(1000))

#__name__ variable is for know the name of the module
print(fibo.__name__)  # prints 'fibo'

#if you want to use a function with frequency, you can assign it to a local name
fib = fibo.fib
fib(500)

print(dir(fibo))  # list all the functions defined in the module fibo
#output: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fib2']