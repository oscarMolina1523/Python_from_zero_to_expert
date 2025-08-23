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