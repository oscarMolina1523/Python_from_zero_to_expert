#We receive a value in the console and store it in the variable "x"
x = int(input("Please enter an integer: "))

#We check the value of "x" and print a message accordingly
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')