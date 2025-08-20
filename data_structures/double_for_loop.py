#FIRST USE CASE

# This code demonstrates a double for loop with a condition to filter pairs
#create a list using a list comprehension
#general sintaxis is 
#[ expression for variable1 in iterable1 for variable2 in iterable2 if condition ]
response=[(x, y) #generate a tuple (x,y)
          for x in [1,2,3] #first loop x takes each value in [1,2,3]
          for y in [3,1,4] #second loop y takes each value in [3,1,4]
          if x != y] #condition to filter pairs where x is not equal to y
                     #only saves pairs where x and y are different

#output
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#SECOND USE CASE
result = [] # create an empty list to store results
for x in [1,2,3]: #iterate the first list in x variable
    for y in [3,1,4]: #iterate the second list in y variable
        if x != y: #if the var x is different than y
            result.append((x, y)) #append the tuple (x,y) to the result list

#output
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]