#sets doesnt allow duplicate values
#You can use braces or the set() function to create sets.
#if you want to create an empty set you have to use set(), because using {} will create an empty dictionary

#create a set of fruits
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #duplicates are removed
#output: {'orange', 'banana', 'pear', 'apple'}

#check if an item is in the set
print('orange' in basket) #True

#check if an item is not in the set
print('crabgrass' in basket) #False

#demonstrate set operations
#set() function read the word and don't include duplicates letters
a = set('abracadabra')
b = set('alacazam')
print(a) #output: {'a', 'b', 'r', 'c', 'd'} #unique letters in a
print(b) #output: {'a', 'm', 'l', 'c', 'z'} #unique letters in b

#you can do mathematical operations on sets like union, intersection, difference, and symmetric difference
print(a - b) #letters in [a] but not in [b] (difference) 
#output: {'r', 'd', 'b'}

print(a | b) #letters in [a] or [b] or both (union) 
#output: {'a', 'b', 'r', 'c', 'd', 'm', 'l', 'z'}

print(a & b) #letters in both [a] and [b] (intersection) 
#output: {'a', 'c'}

print(a ^ b) #letters in [a] or [b] but not both (symmetric difference) 
#output: {'r', 'd', 'b', 'm', 'l', 'z'}