#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# genNewScreen.py
# Created originally in 2021 as a simplistic exercise in broad-spectrum py use
# @author Joe Jackson 


#import curses
#import getpass
#import os
#import shutil
#import subprocess
#import pprint
    # import pformat 
     
#from subprocess import Popen, PIPE, STDOUT

    # import urwid
#import numpy
#import pygame
#import tkinter

      
#import pygame
    
#screenWidthAvail = winfo_reqwidth()
#screenWidthAvail = self.width()
    
#screenHeightAvail = self.height()
    
    # in JS
    #var screenWidthAvail = screen.availWidth ;  
    #var screenHeightAvail = screen.availHeight ; 
    #'''  

import pyautogui

width, height= pyautogui.size()

print(width)
#1366

print(height)
#768

import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
print(screen_height)

#window_width = root.winfo_windowwidth()
#window_height = root.winfo_screenheight()

#print(screen_width)
#print(screen_height)


import os
columns, rows = os.get_terminal_size(0)
print(columns)
print(rows)








