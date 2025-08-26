#str() function is for show legible values
#repr() function need context to show the value
#if you dont pass context to repr() it will show the literal value

s='Hello World'

#we can see the difference between str() and repr()
#str show the value normal, but the repr show the value with quotes and double quotes
print(str(s)) #output: 'Hello World'
print(repr(s)) #output: "'Hello World'"