#declare a dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}

#using a for loop to iterate the dictionary
#[k] is the key, [v] is the value
#items() method returns a tuple of key-value pairs
#in the first iteration, k = 'gallahad', v = 'the pure'
#in the second iteration, k = 'robin', v = 'the brave'
for k, v in knights.items():
    print(k, v)
#output:
# gallahad the pure
# robin the brave

#ENUMERATE FUNCTION
#enumerate() function adds a counter to an iterable and returns it as an enumerate object
#in the first iteration, i = 0, v = 'tic'
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
#output:
# 0 tic
# 1 tac
# 2 toe