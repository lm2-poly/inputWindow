# inputWindow
A simple class to instantiate an input window made with tkinter in Python.

## How to implement
here is a code example of how to implement the input window for a generic project :

    # Import
    from inputWindow import inputWindow
    
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
  
![Input window example](/images/example.JPG)

** Note for combo box : When initializing the values, the index of the item to be selected by default must be appended to the end of the choice list ! For instance :
myChoice = ['Option 1', 'Option 2', 'Option 3', 1]
Here, item indexed at position 2 (item : 'Option 2') will be selected by default.

Then, you may want to convert some values (all returned values are string type) :

    # Values assignments if 
    if myWindow.values:
        [myStringVar, myIntegerVar, myChoice] = myWindow.values

        projectType = myWindow.radioVal

        # All values are output as string and must be converted after depending on the expected type. For example :
        myIntegerVar = int(myIntegerVar)
    
Similarly as the values assignments, you may also detect if the user has clicked the Ok button or Cancel :

    if myWindow.values:
        # Do something
        print(myStringVar)
        print(myIntegerVar)
        print(myChoice)
        print(projectType)        
    else:
        print('User canceled')
