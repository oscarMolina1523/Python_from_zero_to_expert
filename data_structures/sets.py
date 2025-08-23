#sets doesnt allow duplicate values
#You can use braces or the set() function to create sets.
#if you want to create an empty set you have to use set(), because using {} will create an empty dictionary

#create a set of fruits
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #duplicates are removed
#output: {'orange', 'banana', 'pear', 'apple'}