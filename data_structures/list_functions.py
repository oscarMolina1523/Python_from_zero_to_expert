#declare a list of fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#the method "count" counts the number of occurrences of an item in the list
# in this case it counts how many times 'apple' appears in the list 
fruits.count('apple')
#response
#2

#in this case it counts how many times 'tangerine' appears in the list
fruits.count('tangerine')
#response
# 0

#the method "index" returns the index of the first occurrence of an item in the list
# in this case it returns the index of the first 'banana' in the list
#the index starts at 0, so the first 'banana' is at index 3
fruits.index('banana')
#response
# 3

#in this case it returns the index of the first 'banana' after or starting in the index 4
#the second 'banana' is at index 6
fruits.index('banana', 4)  # Find next banana starting at position 4
#response
# 6

#the method "reverse" reverses the order of the items in the list
#in this case it reverses the order of the fruits in the list
fruits.reverse()
fruits
#response
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

#the method "append" adds an item to the end of the list
#in this case it adds 'grape' to the end of the list
fruits.append('grape')
fruits
#response
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

#the method "sort" sorts the items in the list in ascending order
#in this case it sorts the fruits in alphabetical order
fruits.sort()
fruits
#response
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

#the method "pop" removes the last item in the list and returns the item deleted
#in this case it removes 'pear' from the end of the list and returns it
fruits.pop()
#response
# 'pear'