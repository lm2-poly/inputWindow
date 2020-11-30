# Import
from lm2.inputWindow import inputWindow

# Variable initiliazing
myStringVar = 'something'
myIntegerVar = 999
myChoice = ['Option 1','Option 2','Option 3', 1]

# Window creation
title = 'Project parameters'
instructions = 'Provide the specifc parameters for your program by filling the following fields.'
windowWidth = 375               # Width of the window in pixels
fields = ['String param here','Integer param here','Choice']           # Number of field entries matching the variables that you want a user input for.
defaultVal = [myStringVar, myIntegerVar, myChoice]             # Number of default values must fit the number of fields.
radios = ['Choose your project type :','Type 1','Type 2','Type 3']          # the first string is the radio buttons subtile. For no radio buttons, set to None
photo = None#['path\picture.png',100,127]                # file path, width, height. If a picture isn't needed, set to None.
smallFields = False;                # To reduce the width of the input field, set to True.
myWindow = inputWindow.inputWindow(title,instructions,windowWidth,fields,defaultVal,radios,photo,smallFields)            # With this instruction, the window will appear

# Values assignments if 
if myWindow.values:
    [myStringVar, myIntegerVar, myChoice] = myWindow.values
    
    projectType = myWindow.radioVal
    
    # All values are output as string and must be converted after depending on the expected type. For example :
    myIntegerVar = int(myIntegerVar)
    
    print(myStringVar)
    print(myIntegerVar)
    print(myChoice)
    print(projectType)
else:
    print('User canceled')