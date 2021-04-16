###############################################
import tkinter as tk
from tkinter import Menu
from tkinter.filedialog import askopenfilename

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter! This is a sample only.")
w.pack()
#-------------------------------------------------
# from tkinter import *
# from tkinter import Menu
# from tkinter.filedialog import askopenfilename

def NewFile():
    print("New File!")
def OpenFile():
    name = askopenfilename()
    print(name)
def About():
    print("This is a simple example of a menu")
    
#root = Tk()
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

# mainloop()



root.mainloop()

################################################


######  temp block pygame allowing test of rest of file
import pygame
background_colour = (255,255,255)
(width, height) = (300, 200)
#screen = pygame.display.set_mode((width, height))
#pygame.display.set_caption('Pygame Try 1')
#screen.fill(background_colour)
#pygame.display.flip()
#running = True

#while running:
#  for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#      running = False


################################################

