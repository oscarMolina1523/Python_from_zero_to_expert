for i in range(5):
    print(i)

#response:
# 0
# 1
# 2
# 3
# 4

# Generate a list of numbers from 5 to 9:
list(range(5, 10))
#response
# [5, 6, 7, 8, 9]

# Generate a list of numbers from 0 to 9 with a step of 3:
list(range(0, 10, 3))
#response
#[0, 3, 6, 9]

# Generate a list of numbers from -10 to -100 with a step of -30:
list(range(-10, -100, -30))
#response
#[-10, -40, -70]

#This is a strange case because if you try to 
#print only one range it will give an unexpected result.
range(10)

#response
#range(0, 10)

#but if you use it inside a function it is different
sum(range(4))  # 0 + 1 + 2 + 3

#response
# 6