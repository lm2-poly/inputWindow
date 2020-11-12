# inputWindow
A simple class to instantiate an input window made with tkinter in Python.

## How to implement
here is a code example of how to implement the input window for a generic project :

    # Import
    from inputWindow import inputWindow
    
    # Variable initiliazing
    myStringVar = 'something'
    myIntegerVar = 999

    # Window creation
    title = 'Project parameters'
    instructions = 'Provide the specifc parameters for your program by filling the following fields.'
    windowWidth = 375               # Width of the window in pixels
    fields = ['String param here','Integer param here']           # Number of field entries matching the variables that you want a user input for.
    defaultVal = [myStringVar, myIntegerVar]             # Number of default values must fit the number of fields.
    radios = ['Choose your project type :','Type 1','Type 2','Type 3']          # the first string is the radio buttons subtile. For no radio buttons, set to None
    photo = ['path\picture.png',100,127]                # file path, width, height. If a picture isn't needed, set to None.
    smallFields = False;                # To reduce the width of the input field, set to True.
    myWindow = inputWindow.inputWindow(title,instructions,windowWidth,fields,defaultVal,radios,photo,smallFields)            # With this instruction, the window will appear

    # Values assignments
    if myWindow.values:
        [myStringVar, myIntegerVar] = myWindow.values

    projectType = myWindow.radioVal

    # All values are output as string and must be converted after depending on the expected type. For example :
    myIntegerVar = int(myIntegerVar)
    
![Input window example](images/examples.JPG)
