year = 2016
event = 'Referendum'
#this is a normal concatenation using f-strings
print(f'Results of the {year} {event}')

#SECOND CASE
#you can format string more complicatedly
#using str.format() , example :
yes_votes = 42_572_654
total_votes = 85_705_149
#this calculate the percentage of yes votes by total votes
percentage = yes_votes / total_votes #the values is 0.4967

#in this case we use {} to format with the .format() method
#now we can use [:] to format the numbers, the [-] is to align left
#the [9] is to reserve 9 spaces for the number example ,original number is [42572654] but
#the output is ['42572654 '] with a empty space at the end of the number

#in the second {} we use {:2.2%} to format the percentage
#the first [2] is to indicate the minim number of digits before the decimal point
#the second [2] is to indicate the number of digits after the decimal point
#the [%] is to indicate that we want to format as a percentage,
#like multiplying by 100 and adding the % symbol
#the output is ['49.67%'] with the % symbol at the end
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
#the output is ['42572654  YES votes  49.67%']