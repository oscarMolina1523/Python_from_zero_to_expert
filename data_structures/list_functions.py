fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
#response
#2
fruits.count('tangerine')
#reponse
# 0
fruits.index('banana')
#response
# 3
fruits.index('banana', 4)  # Find next banana starting at position 4
#response
# 6
fruits.reverse()
fruits
#response
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
fruits
#response
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
fruits
#response
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
#response
# 'pear'