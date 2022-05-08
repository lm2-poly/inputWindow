# -*- coding: utf-8 -*-
"""
Created on : Fri Nov 29 14:52:52 2019
Last updated : 2020-11-12

@author: Jean-François Chauvette
Definition: Creates an instance of an input window that is used to initialize
            some script's parameters.

Prerequisites: The class, the favicon and the photo must all be in the same folder as the import

Example of import: 
    
    from inputWindow import inputWindow

Example of implementation:
    
    # Window creation
    title = 'Project parameters'
    instructions = 'Provide the specifc parameters for your program by filling the following fields.'
    windowWidth = 375               # Width of the window in pixels
    fields = ['String param','Integer param','comboBox']           # Number of field entries matching the variables that you want a user input for.
    defaultVal = [myStringVar, myIntegerVar,['a','b',1]]             # Number of default values must fit the number of fields. For combobox, the last data is an integer representing the index of the selected item by default
    radios = ['Choose your project type :','Type 1','Type 2','Type 3']          # the first string is the radio buttons subtile. For no radio buttons, set to None
    photo = ['path\picture.png',100,127]                # file path, width, height. If a picture isn't needed, set to None.
    smallFields = False;                # To reduce the width of the input field, set to True.
    myWindow = inputWindow.inputWindow(title,instructions,windowWidth,fields,defaultVal,radios,photo,smallFields)            # With this instruction, the window will appear
    
    # Values assignments
    if myWindow.values:
        [myStringVar, myIntegerVar, myComboBoxChoice] = myWindow.values
    
    projectType = myWindow.radioVal
    
    # All values are output as string and must be converted after depending on the expected type. For example :
    myIntegerVar = int(myIntegerVar)
    
Combo box choice:
    A list of values can be sent within defaultVal. e.g. : defaultVal = [value1, [value2.1, value2.2], value3].
    This will change the text field for a combobox where the user can choose among options.
"""
import tkinter as tk 
from tkinter import ttk
import collections
import math
import os
import json

class inputWindow:
    def __init__(self, title, instructions, width, fields, defaultVal, infosImage=None, smallFields=False, radios=None):
        self.root = None         # Shortcut for tk.Tk()
        self.ents = None         # Entries a textfield
        self.v = None            # Variable for radio buttons
        self.values = []         # List of final values
        self.radioVal = ''       # Project type
        self.folderPath = ''     # Folder of where this script is located
        self.fields = fields
    
        # Gettting the script folder path
        filePath = os.path.realpath(__file__)
        self.folderPath = filePath[0:filePath.rfind('\\')]
        
        # Making the form and getting the entries
        infosImage = [0,0,50] if infosImage is None else infosImage
        self.root = tk.Tk()
        self.root.title(title)
        self.v = tk.IntVar()
        self.ents = self.makeform(instructions, width, fields, defaultVal, radios, infosImage, smallFields)
        self.root.bind('<Return>', self.callback_enter)
        self.ents[next(iter(self.ents))].focus()
        
        # Adding the buttons
        col = 2 if radios is None else max(2,len(radios)-2)
        b2 = tk.Button(self.root, text='Cancel', width=12, command=(lambda e=self.ents: self.clearValues(e)))
        b2.grid(row=len(fields)+3,column=col, sticky='e', padx=10, pady=10)
        b1 = tk.Button(self.root, text='OK', width=12, command=(lambda e=self.ents: self.assignValues(e)))
        b1.grid(row=len(fields)+3,column=col-1, sticky='e', pady=10)
        
        # Managing window size and screen position
        extraHeight = 110 if radios is not None else 50
        self.center_window(width, infosImage[2] + len(fields)*22 + extraHeight) # Width = Constant, Height = (Subtitle + nb of fields*height + subtitle + row of radios + row of buttons)
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file=self.folderPath+'\images\Logo-LM2-fav_icon.ico'))
        self.root.lift()
        self.root.attributes("-topmost", True)       
        self.root.mainloop() 
        
    # Function for generating the window with the project parameters  
    # Return entries as a dictionnary
    def makeform(self, instructions, width, fields, defVal, radios, infosImage, smallFields):
        entries = collections.OrderedDict()
        
        # Adding the image and instructions
        if infosImage[0] != 0:
            photo = tk.PhotoImage(file=self.folderPath+'\images\\'+infosImage[0])
            img = tk.Label(self.root, image = photo, width=infosImage[1], height=infosImage[2], anchor='w')
            img.image = photo
            img.grid(row=0, column=0)
        instr = tk.Label(self.root, text=instructions, justify='left' , anchor='w', wraplength=width-15-infosImage[1]-(30 if infosImage[0] != 0 else 0))
        colspan = 2 if infosImage[0] != 0 else 4 if radios is None else max(2 if infosImage[0] != 0 else 4,len(radios)-(2 if infosImage[0] != 0 else 1))
        instr.grid(row=0, column=(1 if infosImage[0] != 0 else 0), columnspan=colspan, sticky='w e', padx=10, pady=10)
        
        # Adding the fields entry
        if fields is not None:
            colspanLab = 2 if radios is None else max(2,math.floor((len(radios)-1)/2))
            colspanEnt = 2 if radios is None else max(2,len(radios)-2)
            if smallFields:
                colspanLab += 1
                colspanEnt -= 1
            idx = 0
            for field in fields:
                # Label
                lab = tk.Label(self.root, text=field+" : ", anchor='w')#, width=5)
                lab.grid(row=idx+1, column=0, columnspan=colspanLab, sticky='w', padx=10)
                
                # Field
                if type(defVal[idx]) is list:
                    ent = ttk.Combobox(self.root, values = defVal[idx][0:-1], state='readonly')
                    ent.current(defVal[idx][-1])
                    #ent.bind('<<ComboboxSelected>>', self.callback_comboBox)
                else:
                    ent = tk.Entry(self.root)#, width=35)
                    ent.insert(0, defVal[idx])
                ent.grid(row=idx+1, column=colspanLab, columnspan=colspanEnt, sticky='w e', padx=10)
                
                entries[field] = ent
                
                idx += 1
        
        # Adding the radio buttons
        if radios is not None:
            pChoice = tk.Label(self.root, text=radios[0], wraplength=width-10, justify = 'left', anchor='w')
            pChoice.grid(row=len(fields)+1, column=0, columnspan=3, sticky='w', padx=10, pady=10)
        
            for idx, rad in enumerate(radios[1:]):
                pVal = idx+1  
                c = tk.Radiobutton(self.root, text=rad, variable=self.v, value=pVal)
                c.grid(row=len(fields)+2, column=idx, sticky='', padx=10)
                c.deselect()
                if idx == 0:
                    c.select()
        
        # Managing column's automatic width
        nbcol = 4 if radios is None else max(4,len(radios)-1)
        for i in range(nbcol):
            self.root.grid_columnconfigure(i, weight=1, uniform="foo")
            
        return entries
    
    # Function for centering the window
    def center_window(self, width, height):
        # get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
    
        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
       
    # Callback function of window for pressing enter
    def callback_enter(self,event):
        self.assignValues(self.ents)
        
    # def callback_comboBox(self,event):
    #     self.center_window(100, 500)
        
    # Function for assigning values from the window
    def assignValues(self,e):
        for key in e:   # clears all the field
            self.values.append(e[key].get())
        self.radioVal = self.v.get()
        self.root.destroy()
    
    # Function for clearing the window form
    def clearValues(self,e):
        for key in e:   # clears all the field
            e[key].delete(0, tk.END)
        e[next(iter(e))].focus() # focus the first field
        self.root.destroy()
                        
    def export_json(self, filename, defaultVal):
        paramDict = dict(zip(self.fields, defaultVal))
        
        #Writing json file
        for p in range(len(self.values)):
            # looping through the window values to reconstruct a valid dict for the json file
            paramValue = self.values[p]
            paramField = paramDict[self.fields[p]]
            
            # if the parameter to update is the index of a list
            if type(paramDict[self.fields[p]]) is list:
                
                # if it's a list of bool, just update the index with True = 0 and False = 1
                if paramValue == 'True':
                    paramDict[self.fields[p]][-1] = 0
                elif paramValue == 'False':
                    paramDict[self.fields[p]][-1] = 1
                # otherwise, just update the index with the right paramValue as key to the dict
                else:
                    try:
                        paramValue = int(paramValue)
                    except:
                        paramValue = str(paramValue)  
                    choiceIndex = paramField.index(paramValue)
                    paramDict[self.fields[p]][-1] = choiceIndex
            # if any other type than list, update with the corresponding type of the original dict
            else:
                paramDict[self.fields[p]] = type(paramField)(paramValue)
        
        with open(filename, 'w') as outfile:
            json.dump(paramDict, outfile)