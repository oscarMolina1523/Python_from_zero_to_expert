#similar to list comprehensions but with sets
#in list comprehensions you need to use [] but in set comprehensions you need to use {}
a = {x #save the value of x
     for x in 'abracadabra' #iterate over each letter in the string
     if x not in 'abc' #filter out letters that are in 'abc'
    }
print(a)
#output: {'d', 'r'}