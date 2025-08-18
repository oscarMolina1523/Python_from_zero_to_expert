# create a function that takes different types of parameters
# the var kind is a required parameter (normal parameter)
# the *arguments is a variable-length argument list (tuple)
#Captures any number of unnamed (positional) extra parameters passed. Saved as a tuple.
# the **keywords is a variable-length keyword argument list (dictionary)
#Captures any number of named parameters (key=value).Saved as a dictionary.

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    # loop through the array using a for loop
    for arg in arguments:
        print(arg)
    print("-" * 40)
    # loop through the dictionary using a for loop
    for kw in keywords:
        # print the key and value
        # keywords[kw] is the value of the key
        print(kw, ":", keywords[kw])

# Example usage of the cheeseshop function
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
#response
# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch
