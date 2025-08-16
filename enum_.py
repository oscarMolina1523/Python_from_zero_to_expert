from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

user_input = input("Enter your choice of 'red', 'blue' or 'green': ")

try:
    color = Color(user_input)   # Intentamos convertir el string a Enum
except ValueError:
    print("❌ Unknown color")
else:
    match color:
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")
