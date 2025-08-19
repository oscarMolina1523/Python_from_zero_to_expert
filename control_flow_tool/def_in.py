# function recives a prompt string like this ('Do you really want to quit?')
#have 4 retries to answer with 'yes' or 'no'
#and have a message to remind the user to try again
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    #while answer is true repeat the question
    while True:
        # get user input
        reply = input(prompt)
        # if the response have one of these values return True
        if reply in {'y', 'ye', 'yes'}:
            return True
        # if the response have one of these values return False
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        # if the response is not valid, reduce the retries and print the reminder
        retries = retries - 1
        # if retries are 0, raise an error
        if retries < 0:
            raise ValueError('invalid user response')
        # print the reminder message
        print(reminder)