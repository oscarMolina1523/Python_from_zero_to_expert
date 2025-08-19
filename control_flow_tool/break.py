# create a loop to execute a range of numbers
#from 2 to 9, because the range function goes up to, 
# but does not include, the second number
for n in range(2, 10):
    #other loop to execute a range of numbers
    #from 2 to n-1
    for x in range(2, n):
        #if n is divisible by x
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            #break the inner loop
            break

#response 
#because only these numbers are divisible
#by 2
# 4 equals 2 * 2
# 6 equals 2 * 3
# 8 equals 2 * 4
# 9 equals 3 * 3