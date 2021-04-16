#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# tkinter-menu-try01.py
# Created originally in 2021 as part of a simplistic exercise in broad-spectrum py use
# @author Joe Jackson 


from tkinter import *
from tkinter.filedialog import askopenfilename

def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()

