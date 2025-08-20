#FIRST USE CASE

# This code demonstrates a double for loop with a condition to filter pairs
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

#output
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]