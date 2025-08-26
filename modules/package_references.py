# mipaquete/
#  ├── __init__.py
#  ├── sonido/
#  │    ├── __init__.py
#  │    ├── echo.py
#  │    └── efectos.py

#think you have a package structure like this

#this import is similar like this in javascript 
#import echo from "./echo.js";
from . import echo

#this import navigates two levels up
#similar in javascript like this
#import formats from "../formats.js";
from .. import formats

#this import navigates two levels up and then goes to filters folder
#similar in javascript like this
#import equalizer from "../filters/equalizer.js";
from ..filters import equalizer

