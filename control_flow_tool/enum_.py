#import Enum from enum module
from enum import Enum

# Define an enumeration for colors
#recives a string and returns the corresponding Enum member
#always use Enum parameter
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# Get user input
user_input = input("Enter your choice of 'red', 'blue' or 'green': ")

try:
    color = Color(user_input)   # try to convert input to Color Enum
except ValueError:
    print("❌ Unknown color") # handle invalid input
else:
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
