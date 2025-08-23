#To loop through two or more sequences at the same time, entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

#zip function create tuples (elemento_de_lista1, elemento_de_lista2)
#example:
#list(zip(questions, answers))
# [('name', 'Lancelot'), ('quest', 'the holy grail'), ('favorite color', 'blue')]

#this example receives two lists
for q, a in zip(questions, answers):
    #then format replace the value of [q] and [a] with the {0} and {1}
    print('What is your {0}?  It is {1}.'.format(q, a))

#output:
#What is your name?  It is lancelot.
#What is your quest?  It is the holy grail.
#What is your favorite color?  It is blue.