# create a loop to execute a range of numbers
for num in range(2, 10):
    #check if the number is even
    if num % 2 == 0:
        print(f"Found an even number {num}")
        #if it is even, skip to the next iteration
        # if is not even, it will continue to the next line
        continue
    #if the number is odd, print it
    print(f"Found an odd number {num}")

#response
#Found an even number 2
# Found an odd number 3
# Found an even number 4
# Found an odd number 5
# Found an even number 6
# Found an odd number 7
# Found an even number 8
# Found an odd number 9