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