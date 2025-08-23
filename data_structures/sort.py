#a list of strings
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

#using a for loop and
#the sorted() function to print the list in alphabetical order
#sorted funtion doesn't change the original list
for i in sorted(basket):
    print(i)

#output:
# apple
# apple
# banana
# orange
# orange
# pear

#to sort a list without duplicates use set() function
#the set() function removes duplicates
for i in sorted(set(basket)):
    print(i)    

#output:
# apple
# banana
# orange
# pear