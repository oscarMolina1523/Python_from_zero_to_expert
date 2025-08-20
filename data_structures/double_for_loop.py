#FIRST USE CASE

# This code demonstrates a double for loop with a condition to filter pairs
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

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