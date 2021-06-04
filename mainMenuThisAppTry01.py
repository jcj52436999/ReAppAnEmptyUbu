#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# mainMenuThisAppTry01.py 


import tkinter as tk
from tkinter import (Tk, BOTH, Text, E, W, S, N, END, INSERT, 
    NORMAL, DISABLED, StringVar, Menu)
from tkinter.ttk import Frame, Label, Button, Progressbar, Entry
from tkinter import scrolledtext as st

win = tk.Tk() 

import multiprocessing as mp
from multiprocessing import Queue, Process, Pool
import queue 
from decimal import Decimal, getcontext

import time

#####################################################
# class TextFrameTry02(Frame):
class MainMenuThisApp(Frame):
    print() 

#####################################################
# class TextFrameTry02(Frame):
# class PiCruncher(Frame):

    def __init__(self, parent, q):
        Frame.__init__(self, parent)   
         
        # self.queue = q 
        self.parent = parent
        
        # Status XInitThreads(void) 
        # XInitThreads(void)
        
        self.initUI()

    def callback(self):
        self.root.quit()

                
    def initUI(self):
      
        # self.root = tk.Tk()
        # self.root = Tk()
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.parent.title("TextFrameTry02 init title only")
        #self.title("TextFrameTry02 init title only")
        self.pack(fill=BOTH, expand=True)
        
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=1)
        
        lbl1 = Label(self, text="Digits:")
        lbl1.grid(row=0, column=0, sticky=E, padx=10, pady=10)
        
        self.ent1 = Entry(self, width=10)
        self.ent1.insert(END, "4000")
        self.ent1.grid(row=0, column=1, sticky=W)
        
        lbl2 = Label(self, text="Accuracy:")
        lbl2.grid(row=0, column=2, sticky=E, padx=10, pady=10)

        self.ent2 = Entry(self, width=10)
        self.ent2.insert(END, "100")
        self.ent2.grid(row=0, column=3, sticky=W)        
        
        self.startBtn = Button(self, text="Start", 
            command=self.onStart)
        self.startBtn.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        self.pbar = Progressbar(self, mode='indeterminate')        
        self.pbar.grid(row=1, column=1, columnspan=3, sticky=W+E)     
        
        # self.txt = st.ScrolledText(win)  
        self.txt = st.ScrolledText(self)  
        self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5,columnspan=5, sticky=E+W+S+N) 

        self.txt.insert(INSERT, "\nJust set up this txt.\n") 
        self.txt.insert(INSERT, "Just set up this txt.\n") 
        self.txt.insert(INSERT, "Just set up this txt.\n") 
        self.txt.insert(INSERT, "Just set up this txt.\n") 
        self.txt.insert(INSERT, "Just set up this txt.\n\n") 
        # aKeyStrk = keyboard.read_key()
        # aKeyStrk = input() 
        
#####################################################################


#####################################################
# class TextFrameTry02(Frame):
def mainMenuThisApp():
    print() 

    # from Tkinter import *
    
    def donothing():
       filewin = Toplevel(root)
       button = Button(filewin, text="Do nothing button")
       button.pack()
       
    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    
    filemenu.add_separator()
    
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    
    editmenu.add_separator()
    
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    
    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    xPosThisFrame=400 ; yPosThisFrame=200
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    root.geometry(dotGeoStr) 

    root.config(menu=menubar)
    root.mainloop()
#####################################################################

def main(): 
    print("") 
    # q = Queue()
    # queue = multiprocessing.Queue() 
    # args = (queue, queue)

    xy=mainMenuThisApp() 

####################################################################
if __name__ == '__main__':
    main()  
    
    exit()
    
