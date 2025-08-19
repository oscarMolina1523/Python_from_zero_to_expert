#you need to use the operator * to unpack a list or tuple (array)
#and ** to unpack a dictionary (list of key-value pairs)

#this is a normal list
list(range(3, 6))            # normal call with separate arguments
#response
#[3, 4, 5]

#this is an array
args = [3, 6]
#using the * operator to unpack the list
list(range(*args))            # call with arguments unpacked from a list
#response
# [3, 4, 5]

#this is a normal function 
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

#this is a dictionary of arguments
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
#using the ** operator to unpack the dictionary
parrot(**d)
#response
#-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !