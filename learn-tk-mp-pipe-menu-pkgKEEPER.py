#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# learn-tk-mp-pipe-menu-pkg.py now, was 
# calculate_pi-add-another.py 

# 2001-05-27-1625 - learn-tk-mp-pipe-menu-pkg.py -- rolled from below previous for purpose of learning. 
# calculate_pi-add-another.py 
# Created originally in 2021 as a simplistic exercise in broad-spectrum py use
#   copied from web and modified for study @author Joe Jackson 
#   choosing to expand this into a multi-window parallel processing app
#   missed logging git commit comment here, no biggie, rolling this to a better learning title.
#   Rolling to file learn-tk-mp-pipe-menu-pkg.py


aComment="""
ZetCode Tkinter e-book

This script produces a long-running task of calculating 
a large Pi number, while keeping the GUI responsive.

Author: Jan Bodnar
Last modified: January 2016
Website: www.zetcode.com

Copied for study by JC Jackson, 2021-04-21
"""

import tkinter as tk
from tkinter import (Tk, BOTH, Text, E, W, S, N, END, INSERT, 
    NORMAL, DISABLED, StringVar)
from tkinter.ttk import Frame, Label, Button, Progressbar, Entry
from tkinter import scrolledtext as st

win = tk.Tk() 

import multiprocessing
from multiprocessing import Queue, Process
import queue 
from decimal import Decimal, getcontext

import time

# import keyboard 

# import XInitThreads

screenWidth = win.winfo_screenwidth()
screenHeight = win.winfo_screenheight()

DELAY1 = 10
DELAY2 = 20

# KEEPER KEEPER KEEPER KEEPER KEEPER
class Example(Frame):
  
    def __init__(self, parent, q):
        Frame.__init__(self, parent)   
         
        self.queue = q 
        self.parent = parent
        self.initUI()

    def callback(self):
        self.root.quit()

    def initUI(self):
      
        # self.root = tk.Tk()
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.parent.title("Pi Computation")
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
        
        self.txt = st.ScrolledText(self)  
        self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5,
            columnspan=5, sticky=E+W+S+N)
       
        # self.root.mainloop() 
        
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END)
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        self.p1 = Process(target=self.generatePi, args=(self.queue, ))
    #   self.p1 = Process(target=self.generatePi, args=(self.queue ))
        self.p1.start()
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue)
        
       
    def onGetValue(self):
        
        if (self.p1.is_alive()):
            
            self.after(DELAY1, self.onGetValue)
            return
        else:    
        
            try:
                self.txt.insert('end', self.queue.get(0))
                self.txt.insert('end', "\n")
                self.pbar.stop()
                self.startBtn.config(state=NORMAL)
            
            except queue.Empty:
                print("queue is empty")
            
            
    def generatePi(self, queue):
        
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        k = 0
        n = self.accuracy
        
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1
            print ("Example frame is still alive = ", self.p1.is_alive())
            # queue.put("Example frame is still alive = ", self.p1.is_alive())
            
        queue.put(pi)    
        print("Example frame end")    


###########################################################
class ExampleAlso(Frame):
  
    def __init__(self, parent, q):
        Frame.__init__(self, parent)   
         
        self.queue = q 
        self.parent = parent
        self.initUI()

    def callback(self):
        self.root.quit()

                
    def initUI(self):
      
        # self.root = tk.Tk()
        # self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.parent.title("Pi Computation Also")
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
        
        self.txt = st.ScrolledText(self)  
        self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5,
            columnspan=5, sticky=E+W+S+N)

        # self.root.mainloop()
       
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END)
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        self.p1 = Process(target=self.generatePi, args=(self.queue,))
        self.p1.start()
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue)
        
       
    def onGetValue(self):
        
        if (self.p1.is_alive()):
            
            self.after(DELAY1, self.onGetValue)
            return
        else:    
        
            try:
                self.txt.insert('end', self.queue.get(0))
                self.txt.insert('end', "\n")
                self.pbar.stop()
                self.startBtn.config(state=NORMAL)
            
            except queue.Empty:
                print("queue is empty")
            
            
    def generatePi(self, queue):
        
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        k = 0
        n = self.accuracy
        
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1
            print ("ExampleAlso frame is still alive = ", self.p1.is_alive())
            
        queue.put(pi)    
        print("ExampleAlso frame end")    


#####################################################
# class TextFrameTry01(Frame):
class MenuChooseAppStarts(Frame):
  
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
        
        aComment=''' 
        st.insert(tkinter.INSERT, 'Following Ports are open\n' )
        st.insert(tkinter.INSERT, str(portlist)) 
        
        # Creating scrolled text 
        # area widget
        text_area = st.ScrolledText(win, 
                                              wrap = tk.WORD, 
                                              width = 40, 
                                              height = 10, 
                                              font = ("Times New Roman",
                                                      15))
          
        text_area.grid(column = 0, pady = 10, padx = 10)
          
        # Placing cursor in the text area
        text_area.focus()
        
        '''
                
        # self.txt = st.ScrolledText(self.root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 15), grid=(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N))
    
        # self.txt = st.ScrolledText(width = 40, height = 10, font = ("Times New Roman", 15), grid.row(2), grid.column(0), grid.rowspan(4), grid.padx(10), grid.pady(5), grid.columnspan(5), grid.sticky(E+W+S+N), wrap(tk.WORD))

        # self.txt = st.ScrolledText(self)  
        
        # self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N)

        # text_area = st.ScrolledText(win, 
                                      #wrap = tk.WORD, 
                                      #width = 40, 
                                      #height = 10, 
                                      #font = ("Times New Roman",
                                            #15))
  
        # self.root.mainloop()
       
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END) 
        self.txt.insert(INSERT, "\n\nNow onStart method is running.\n\n") 
        print(self.onStart, "\nNow onStart method is running.\n") 
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        print("\nonStart, start to process generatePi is next.\n") 
        self.txt.insert(INSERT, "\n\nonStart, start to process to generatePi is next.\n\n") 


        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        
        # creating new processes
        # p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
        # p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

        msgs = ""
        
        # self.p1 = Process(target=self.generatePi)
        # self.p1 = Process(target=self.generatePi, args=(self.queue, ))
        self.p1 = Process(target=self.generatePi, args=(self.parent_conn, msgs ))
        self.p1.start() 
        
        
        print("\nonStart, start to parallel process to generatePi started.\n")
        self.txt.insert(INSERT, "\n\nonStart, start to parallel process to generatePi started.\n\n") 
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue(self.child_conn, msgs))
        
       
    def onGetValue(self, conn, msgs):
        
        # if (self.p1.is_alive()):

          while self.p1.is_alive():    
              print("\nonGetValue finds ------------------------- generatePi Process is alive")
              self.txt.insert(INSERT, "\nonGetValue finds ---------------------- generatePi Process is alive\n") 
              # self.after(DELAY1, self.onGetValue(conn, msgs))   # self.onGetValue)
              # return 
              # msg = conn.recv() 
              # self.txt.insert( msg ) 
              time.sleep(0.1) 
              

        # else:    

          # while 1:
          #     msg = conn.recv()
          #     if msg == "END":
          #         break
          #     print("Received the message: {}".format(msg))
        
            # try: 
          msg = "msg"
          msg = conn.recv() 
          print("This should be a pi: ", msg) 
          self.txt.insert(END, "\nThis should be a pi: ")               # self.queue.get(0))
          self.txt.insert(END, msg)               # self.queue.get(0))
          self.txt.insert(END, "\n") 
          self.txt.insert(INSERT, "\n\nNow running onGetValue else section.\n\n") 
          print("\nNow running onGetValue else section.\n") 

          self.pbar.stop() 
          self.startBtn.config(state=NORMAL)
          
            # except conn.Empty:   # queue.Empty:
                # print("\nqueue is PLACEKEEPER empty\n") 
                # self.txt.insert("\nqueue is PLACEKEEPER empty\n")         

            
    def generatePi(self, conn, msgs):
    # def generatePi(self, queue):
    # def generatePi(self):               self.queue, , self.parent_conn, msgs
    #                  def sender(conn, msgs):
    
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        # pi=999
        k = 0
        n = self.accuracy
        
        # self.txt.delete('1.0', END) 
        # clear the outputtext text widget. 1.0 and         
        # self.txt.delete("1.0", "end-1c")
        
        #self.txt.focus() 
        
        # self.txt.delete(1.0,tk.END) # clear the outputtext text widget. 1.0 and tk.END are neccessary. tk implies the tkinter module. If you just want to add text dont incude that line
        print("\nNow running generatePi section.\n") 
        ##### self.text.put("---------------") 
        self.txt.insert(INSERT,"\n\n---------------\n\n")   
        self.txt.insert(INSERT, "\n\nNow running generatePi section.\n\n") 


        # aComment='''
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1 
            
            # self.txt.insert(INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, str(portlist))
            # myvar = "the answer is {}".format(answer) 
            # myvar = "the answer is " + str(answer) 
            insertToTxtfr = ("\nTextFrameTry02 is still alive = " + str(self.p1.is_alive())+"")   
            
            # insertToTxtfr = ('TextFrameTry02 is still alive = {}'.format(self.p1.is_alive())   
            # insertToTxtfr = ('TextFrameTry02 is still alive = XXX')   
                        
            print(insertToTxtfr) 
            # queue.put("TextFrameTry02 is still alive = ", self.p1.is_alive()) 
            # queue.put(" ") 
            
            # outputtext.insert(tk.END,entryvar) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            #self.txt.insert(INSERT, insertToTxtfr) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            ##### self.txt.update_idletasks() 
            # XInitThreads
            # self.txt.pack
            # conn.send( insertToTxtfr )
            time.sleep(0.01) 
            # '''
            
        
            
        #### self.txt.update_idletasks() 
        # self.txt.pack
        
        print("\nNow running print out pi section.\n") 
        self.txt.insert(INSERT, "\n\nNow running print out pi section.\n\n") 
        print( pi ) 
        print( self.parent.title(), " frame end")    

        self.txt.insert(INSERT, "\n\nNow running INSERT out pi section.\n\n") 
        self.txt.insert(INSERT, pi )  
        self.txt.insert(INSERT, "\n\nDone INSERTING and printing out pi.\n\n") 
        print("\nDone INSERTING and printing out pi.\n") 

        conn.send( pi ) 
        
        #queue.put(" ") 
        #queue.put("Putting Pi from generatePi function.\n")
        #queue.put(pi) 
        #queue.put("Done putting Pi from generatePi function.\n")
        # queue.put(" ") 
        # self.txt.pack
        print("Returning from generatePi.") 
        return pi

#########################################################


#####################################################
# class TextFrameTry01(Frame):
class ReAppEmptyUbu(Frame):
  
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
        
        aComment=''' 
        st.insert(tkinter.INSERT, 'Following Ports are open\n' )
        st.insert(tkinter.INSERT, str(portlist)) 
        
        # Creating scrolled text 
        # area widget
        text_area = st.ScrolledText(win, 
                                              wrap = tk.WORD, 
                                              width = 40, 
                                              height = 10, 
                                              font = ("Times New Roman",
                                                      15))
          
        text_area.grid(column = 0, pady = 10, padx = 10)
          
        # Placing cursor in the text area
        text_area.focus()
        
        '''
                
        # self.txt = st.ScrolledText(self.root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 15), grid=(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N))
    
        # self.txt = st.ScrolledText(width = 40, height = 10, font = ("Times New Roman", 15), grid.row(2), grid.column(0), grid.rowspan(4), grid.padx(10), grid.pady(5), grid.columnspan(5), grid.sticky(E+W+S+N), wrap(tk.WORD))

        # self.txt = st.ScrolledText(self)  
        
        # self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N)

        # text_area = st.ScrolledText(win, 
                                      #wrap = tk.WORD, 
                                      #width = 40, 
                                      #height = 10, 
                                      #font = ("Times New Roman",
                                            #15))
  
        # self.root.mainloop()
       
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END) 
        self.txt.insert(INSERT, "\n\nNow onStart method is running.\n\n") 
        print(self.onStart, "\nNow onStart method is running.\n") 
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        print("\nonStart, start to process generatePi is next.\n") 
        self.txt.insert(INSERT, "\n\nonStart, start to process to generatePi is next.\n\n") 


        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        
        # creating new processes
        # p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
        # p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

        msgs = ""
        
        # self.p1 = Process(target=self.generatePi)
        # self.p1 = Process(target=self.generatePi, args=(self.queue, ))
        self.p1 = Process(target=self.generatePi, args=(self.parent_conn, msgs ))
        self.p1.start() 
        
        
        print("\nonStart, start to parallel process to generatePi started.\n")
        self.txt.insert(INSERT, "\n\nonStart, start to parallel process to generatePi started.\n\n") 
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue(self.child_conn, msgs))
        
       
    def onGetValue(self, conn, msgs):
        
        # if (self.p1.is_alive()):

          while self.p1.is_alive():    
              print("\nonGetValue finds ------------------------- generatePi Process is alive")
              self.txt.insert(INSERT, "\nonGetValue finds ---------------------- generatePi Process is alive\n") 
              # self.after(DELAY1, self.onGetValue(conn, msgs))   # self.onGetValue)
              # return 
              # msg = conn.recv() 
              # self.txt.insert( msg ) 
              time.sleep(0.1) 
              

        # else:    

          # while 1:
          #     msg = conn.recv()
          #     if msg == "END":
          #         break
          #     print("Received the message: {}".format(msg))
        
            # try: 
          msg = "msg"
          msg = conn.recv() 
          print("This should be a pi: ", msg) 
          self.txt.insert(END, "\nThis should be a pi: ")               # self.queue.get(0))
          self.txt.insert(END, msg)               # self.queue.get(0))
          self.txt.insert(END, "\n") 
          self.txt.insert(INSERT, "\n\nNow running onGetValue else section.\n\n") 
          print("\nNow running onGetValue else section.\n") 

          self.pbar.stop() 
          self.startBtn.config(state=NORMAL)
          
            # except conn.Empty:   # queue.Empty:
                # print("\nqueue is PLACEKEEPER empty\n") 
                # self.txt.insert("\nqueue is PLACEKEEPER empty\n")         

            
    def generatePi(self, conn, msgs):
    # def generatePi(self, queue):
    # def generatePi(self):               self.queue, , self.parent_conn, msgs
    #                  def sender(conn, msgs):
    
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        # pi=999
        k = 0
        n = self.accuracy
        
        # self.txt.delete('1.0', END) 
        # clear the outputtext text widget. 1.0 and         
        # self.txt.delete("1.0", "end-1c")
        
        #self.txt.focus() 
        
        # self.txt.delete(1.0,tk.END) # clear the outputtext text widget. 1.0 and tk.END are neccessary. tk implies the tkinter module. If you just want to add text dont incude that line
        print("\nNow running generatePi section.\n") 
        ##### self.text.put("---------------") 
        self.txt.insert(INSERT,"\n\n---------------\n\n")   
        self.txt.insert(INSERT, "\n\nNow running generatePi section.\n\n") 


        # aComment='''
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1 
            
            # self.txt.insert(INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, str(portlist))
            # myvar = "the answer is {}".format(answer) 
            # myvar = "the answer is " + str(answer) 
            insertToTxtfr = ("\nTextFrameTry02 is still alive = " + str(self.p1.is_alive())+"")   
            
            # insertToTxtfr = ('TextFrameTry02 is still alive = {}'.format(self.p1.is_alive())   
            # insertToTxtfr = ('TextFrameTry02 is still alive = XXX')   
                        
            print(insertToTxtfr) 
            # queue.put("TextFrameTry02 is still alive = ", self.p1.is_alive()) 
            # queue.put(" ") 
            
            # outputtext.insert(tk.END,entryvar) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            #self.txt.insert(INSERT, insertToTxtfr) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            ##### self.txt.update_idletasks() 
            # XInitThreads
            # self.txt.pack
            # conn.send( insertToTxtfr )
            time.sleep(0.01) 
            # '''
            
        
            
        #### self.txt.update_idletasks() 
        # self.txt.pack
        
        print("\nNow running print out pi section.\n") 
        self.txt.insert(INSERT, "\n\nNow running print out pi section.\n\n") 
        print( pi ) 
        print( self.parent.title(), " frame end")    

        self.txt.insert(INSERT, "\n\nNow running INSERT out pi section.\n\n") 
        self.txt.insert(INSERT, pi )  
        self.txt.insert(INSERT, "\n\nDone INSERTING and printing out pi.\n\n") 
        print("\nDone INSERTING and printing out pi.\n") 

        conn.send( pi ) 
        
        #queue.put(" ") 
        #queue.put("Putting Pi from generatePi function.\n")
        #queue.put(pi) 
        #queue.put("Done putting Pi from generatePi function.\n")
        # queue.put(" ") 
        # self.txt.pack
        print("Returning from generatePi.") 
        return pi

#########################################################


#####################################################
# class TextFrameTry01(Frame):
class SpeakerDrooled(Frame):
  
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
        
        aComment=''' 
        st.insert(tkinter.INSERT, 'Following Ports are open\n' )
        st.insert(tkinter.INSERT, str(portlist)) 
        
        # Creating scrolled text 
        # area widget
        text_area = st.ScrolledText(win, 
                                              wrap = tk.WORD, 
                                              width = 40, 
                                              height = 10, 
                                              font = ("Times New Roman",
                                                      15))
          
        text_area.grid(column = 0, pady = 10, padx = 10)
          
        # Placing cursor in the text area
        text_area.focus()
        
        '''
                
        # self.txt = st.ScrolledText(self.root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 15), grid=(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N))
    
        # self.txt = st.ScrolledText(width = 40, height = 10, font = ("Times New Roman", 15), grid.row(2), grid.column(0), grid.rowspan(4), grid.padx(10), grid.pady(5), grid.columnspan(5), grid.sticky(E+W+S+N), wrap(tk.WORD))

        # self.txt = st.ScrolledText(self)  
        
        # self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N)

        # text_area = st.ScrolledText(win, 
                                      #wrap = tk.WORD, 
                                      #width = 40, 
                                      #height = 10, 
                                      #font = ("Times New Roman",
                                            #15))
  
        # self.root.mainloop()
       
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END) 
        self.txt.insert(INSERT, "\n\nNow onStart method is running.\n\n") 
        print(self.onStart, "\nNow onStart method is running.\n") 
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        print("\nonStart, start to process generatePi is next.\n") 
        self.txt.insert(INSERT, "\n\nonStart, start to process to generatePi is next.\n\n") 


        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        
        # creating new processes
        # p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
        # p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

        msgs = ""
        
        # self.p1 = Process(target=self.generatePi)
        # self.p1 = Process(target=self.generatePi, args=(self.queue, ))
        self.p1 = Process(target=self.generatePi, args=(self.parent_conn, msgs ))
        self.p1.start() 
        
        
        print("\nonStart, start to parallel process to generatePi started.\n")
        self.txt.insert(INSERT, "\n\nonStart, start to parallel process to generatePi started.\n\n") 
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue(self.child_conn, msgs))
        
       
    def onGetValue(self, conn, msgs):
        
        # if (self.p1.is_alive()):

          while self.p1.is_alive():    
              print("\nonGetValue finds ------------------------- generatePi Process is alive")
              self.txt.insert(INSERT, "\nonGetValue finds ---------------------- generatePi Process is alive\n") 
              # self.after(DELAY1, self.onGetValue(conn, msgs))   # self.onGetValue)
              # return 
              # msg = conn.recv() 
              # self.txt.insert( msg ) 
              time.sleep(0.1) 
              

        # else:    

          # while 1:
          #     msg = conn.recv()
          #     if msg == "END":
          #         break
          #     print("Received the message: {}".format(msg))
        
            # try: 
          msg = "msg"
          msg = conn.recv() 
          print("This should be a pi: ", msg) 
          self.txt.insert(END, "\nThis should be a pi: ")               # self.queue.get(0))
          self.txt.insert(END, msg)               # self.queue.get(0))
          self.txt.insert(END, "\n") 
          self.txt.insert(INSERT, "\n\nNow running onGetValue else section.\n\n") 
          print("\nNow running onGetValue else section.\n") 

          self.pbar.stop() 
          self.startBtn.config(state=NORMAL)
          
            # except conn.Empty:   # queue.Empty:
                # print("\nqueue is PLACEKEEPER empty\n") 
                # self.txt.insert("\nqueue is PLACEKEEPER empty\n")         

            
    def generatePi(self, conn, msgs):
    # def generatePi(self, queue):
    # def generatePi(self):               self.queue, , self.parent_conn, msgs
    #                  def sender(conn, msgs):
    
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        # pi=999
        k = 0
        n = self.accuracy
        
        # self.txt.delete('1.0', END) 
        # clear the outputtext text widget. 1.0 and         
        # self.txt.delete("1.0", "end-1c")
        
        #self.txt.focus() 
        
        # self.txt.delete(1.0,tk.END) # clear the outputtext text widget. 1.0 and tk.END are neccessary. tk implies the tkinter module. If you just want to add text dont incude that line
        print("\nNow running generatePi section.\n") 
        ##### self.text.put("---------------") 
        self.txt.insert(INSERT,"\n\n---------------\n\n")   
        self.txt.insert(INSERT, "\n\nNow running generatePi section.\n\n") 


        # aComment='''
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1 
            
            # self.txt.insert(INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, str(portlist))
            # myvar = "the answer is {}".format(answer) 
            # myvar = "the answer is " + str(answer) 
            insertToTxtfr = ("\nTextFrameTry02 is still alive = " + str(self.p1.is_alive())+"")   
            
            # insertToTxtfr = ('TextFrameTry02 is still alive = {}'.format(self.p1.is_alive())   
            # insertToTxtfr = ('TextFrameTry02 is still alive = XXX')   
                        
            print(insertToTxtfr) 
            # queue.put("TextFrameTry02 is still alive = ", self.p1.is_alive()) 
            # queue.put(" ") 
            
            # outputtext.insert(tk.END,entryvar) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            #self.txt.insert(INSERT, insertToTxtfr) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            ##### self.txt.update_idletasks() 
            # XInitThreads
            # self.txt.pack
            # conn.send( insertToTxtfr )
            time.sleep(0.01) 
            # '''
            
        
            
        #### self.txt.update_idletasks() 
        # self.txt.pack
        
        print("\nNow running print out pi section.\n") 
        self.txt.insert(INSERT, "\n\nNow running print out pi section.\n\n") 
        print( pi ) 
        print( self.parent.title(), " frame end")    

        self.txt.insert(INSERT, "\n\nNow running INSERT out pi section.\n\n") 
        self.txt.insert(INSERT, pi )  
        self.txt.insert(INSERT, "\n\nDone INSERTING and printing out pi.\n\n") 
        print("\nDone INSERTING and printing out pi.\n") 

        conn.send( pi ) 
        
        #queue.put(" ") 
        #queue.put("Putting Pi from generatePi function.\n")
        #queue.put(pi) 
        #queue.put("Done putting Pi from generatePi function.\n")
        # queue.put(" ") 
        # self.txt.pack
        print("Returning from generatePi.") 
        return pi

#########################################################


#####################################################
# class TextFrameTry01(Frame):
class UnitsConverter(Frame):
  
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
        
        aComment=''' 
        st.insert(tkinter.INSERT, 'Following Ports are open\n' )
        st.insert(tkinter.INSERT, str(portlist)) 
        
        # Creating scrolled text 
        # area widget
        text_area = st.ScrolledText(win, 
                                              wrap = tk.WORD, 
                                              width = 40, 
                                              height = 10, 
                                              font = ("Times New Roman",
                                                      15))
          
        text_area.grid(column = 0, pady = 10, padx = 10)
          
        # Placing cursor in the text area
        text_area.focus()
        
        '''
                
        # self.txt = st.ScrolledText(self.root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 15), grid=(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N))
    
        # self.txt = st.ScrolledText(width = 40, height = 10, font = ("Times New Roman", 15), grid.row(2), grid.column(0), grid.rowspan(4), grid.padx(10), grid.pady(5), grid.columnspan(5), grid.sticky(E+W+S+N), wrap(tk.WORD))

        # self.txt = st.ScrolledText(self)  
        
        # self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N)

        # text_area = st.ScrolledText(win, 
                                      #wrap = tk.WORD, 
                                      #width = 40, 
                                      #height = 10, 
                                      #font = ("Times New Roman",
                                            #15))
  
        # self.root.mainloop()
       
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END) 
        self.txt.insert(INSERT, "\n\nNow onStart method is running.\n\n") 
        print(self.onStart, "\nNow onStart method is running.\n") 
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        print("\nonStart, start to process generatePi is next.\n") 
        self.txt.insert(INSERT, "\n\nonStart, start to process to generatePi is next.\n\n") 


        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        
        # creating new processes
        # p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
        # p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

        msgs = ""
        
        # self.p1 = Process(target=self.generatePi)
        # self.p1 = Process(target=self.generatePi, args=(self.queue, ))
        self.p1 = Process(target=self.generatePi, args=(self.parent_conn, msgs ))
        self.p1.start() 
        
        
        print("\nonStart, start to parallel process to generatePi started.\n")
        self.txt.insert(INSERT, "\n\nonStart, start to parallel process to generatePi started.\n\n") 
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue(self.child_conn, msgs))
        
       
    def onGetValue(self, conn, msgs):
        
        # if (self.p1.is_alive()):

          while self.p1.is_alive():    
              print("\nonGetValue finds ------------------------- generatePi Process is alive")
              self.txt.insert(INSERT, "\nonGetValue finds ---------------------- generatePi Process is alive\n") 
              # self.after(DELAY1, self.onGetValue(conn, msgs))   # self.onGetValue)
              # return 
              # msg = conn.recv() 
              # self.txt.insert( msg ) 
              time.sleep(0.1) 
              

        # else:    

          # while 1:
          #     msg = conn.recv()
          #     if msg == "END":
          #         break
          #     print("Received the message: {}".format(msg))
        
            # try: 
          msg = "msg"
          msg = conn.recv() 
          print("This should be a pi: ", msg) 
          self.txt.insert(END, "\nThis should be a pi: ")               # self.queue.get(0))
          self.txt.insert(END, msg)               # self.queue.get(0))
          self.txt.insert(END, "\n") 
          self.txt.insert(INSERT, "\n\nNow running onGetValue else section.\n\n") 
          print("\nNow running onGetValue else section.\n") 

          self.pbar.stop() 
          self.startBtn.config(state=NORMAL)
          
            # except conn.Empty:   # queue.Empty:
                # print("\nqueue is PLACEKEEPER empty\n") 
                # self.txt.insert("\nqueue is PLACEKEEPER empty\n")         

            
    def generatePi(self, conn, msgs):
    # def generatePi(self, queue):
    # def generatePi(self):               self.queue, , self.parent_conn, msgs
    #                  def sender(conn, msgs):
    
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        # pi=999
        k = 0
        n = self.accuracy
        
        # self.txt.delete('1.0', END) 
        # clear the outputtext text widget. 1.0 and         
        # self.txt.delete("1.0", "end-1c")
        
        #self.txt.focus() 
        
        # self.txt.delete(1.0,tk.END) # clear the outputtext text widget. 1.0 and tk.END are neccessary. tk implies the tkinter module. If you just want to add text dont incude that line
        print("\nNow running generatePi section.\n") 
        ##### self.text.put("---------------") 
        self.txt.insert(INSERT,"\n\n---------------\n\n")   
        self.txt.insert(INSERT, "\n\nNow running generatePi section.\n\n") 


        # aComment='''
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1 
            
            # self.txt.insert(INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, str(portlist))
            # myvar = "the answer is {}".format(answer) 
            # myvar = "the answer is " + str(answer) 
            insertToTxtfr = ("\nTextFrameTry02 is still alive = " + str(self.p1.is_alive())+"")   
            
            # insertToTxtfr = ('TextFrameTry02 is still alive = {}'.format(self.p1.is_alive())   
            # insertToTxtfr = ('TextFrameTry02 is still alive = XXX')   
                        
            print(insertToTxtfr) 
            # queue.put("TextFrameTry02 is still alive = ", self.p1.is_alive()) 
            # queue.put(" ") 
            
            # outputtext.insert(tk.END,entryvar) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            #self.txt.insert(INSERT, insertToTxtfr) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            ##### self.txt.update_idletasks() 
            # XInitThreads
            # self.txt.pack
            # conn.send( insertToTxtfr )
            time.sleep(0.01) 
            # '''
            
        
            
        #### self.txt.update_idletasks() 
        # self.txt.pack
        
        print("\nNow running print out pi section.\n") 
        self.txt.insert(INSERT, "\n\nNow running print out pi section.\n\n") 
        print( pi ) 
        print( self.parent.title(), " frame end")    

        self.txt.insert(INSERT, "\n\nNow running INSERT out pi section.\n\n") 
        self.txt.insert(INSERT, pi )  
        self.txt.insert(INSERT, "\n\nDone INSERTING and printing out pi.\n\n") 
        print("\nDone INSERTING and printing out pi.\n") 

        conn.send( pi ) 
        
        #queue.put(" ") 
        #queue.put("Putting Pi from generatePi function.\n")
        #queue.put(pi) 
        #queue.put("Done putting Pi from generatePi function.\n")
        # queue.put(" ") 
        # self.txt.pack
        print("Returning from generatePi.") 
        return pi

#########################################################


#####################################################
# class TextFrameTry02(Frame):
class PiCruncher(Frame):

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
        
        aComment=''' 
        st.insert(tkinter.INSERT, 'Following Ports are open\n' )
        st.insert(tkinter.INSERT, str(portlist)) 
        
        # Creating scrolled text 
        # area widget
        text_area = st.ScrolledText(win, 
                                              wrap = tk.WORD, 
                                              width = 40, 
                                              height = 10, 
                                              font = ("Times New Roman",
                                                      15))
          
        text_area.grid(column = 0, pady = 10, padx = 10)
          
        # Placing cursor in the text area
        text_area.focus()
        
        '''
                
        # self.txt = st.ScrolledText(self.root, wrap = tk.WORD, width = 40, height = 10, font = ("Times New Roman", 15), grid=(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N))
    
        # self.txt = st.ScrolledText(width = 40, height = 10, font = ("Times New Roman", 15), grid.row(2), grid.column(0), grid.rowspan(4), grid.padx(10), grid.pady(5), grid.columnspan(5), grid.sticky(E+W+S+N), wrap(tk.WORD))

        # self.txt = st.ScrolledText(self)  
        
        # self.txt.grid(row=2, column=0, rowspan=4, padx=10, pady=5, columnspan=5, sticky=E+W+S+N)

        # text_area = st.ScrolledText(win, 
                                      #wrap = tk.WORD, 
                                      #width = 40, 
                                      #height = 10, 
                                      #font = ("Times New Roman",
                                            #15))
  
        # self.root.mainloop()
       
        
    def onStart(self):
        
        self.startBtn.config(state=DISABLED)
        self.txt.delete("1.0", END) 
        self.txt.insert(INSERT, "\n\nNow onStart method is running.\n\n") 
        print(self.onStart, "\nNow onStart method is running.\n") 
        
        self.digits = int(self.ent1.get())
        self.accuracy = int(self.ent2.get())
        
        print("\nonStart, start to process generatePi is next.\n") 
        self.txt.insert(INSERT, "\n\nonStart, start to process to generatePi is next.\n\n") 


        self.parent_conn, self.child_conn = multiprocessing.Pipe()
        
        # creating new processes
        # p1 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
        # p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

        msgs = ""
        
        # self.p1 = Process(target=self.generatePi)
        # self.p1 = Process(target=self.generatePi, args=(self.queue, ))
        self.p1 = Process(target=self.generatePi, args=(self.parent_conn, msgs ))
        self.p1.start() 
        
        
        print("\nonStart, start to parallel process to generatePi started.\n")
        self.txt.insert(INSERT, "\n\nonStart, start to parallel process to generatePi started.\n\n") 
        self.pbar.start(DELAY2)
        self.after(DELAY1, self.onGetValue(self.child_conn, msgs))
        
       
    def onGetValue(self, conn, msgs):
        
        # if (self.p1.is_alive()):

          while self.p1.is_alive():    
              print("\nonGetValue finds ------------------------- generatePi Process is alive")
              self.txt.insert(INSERT, "\nonGetValue finds ---------------------- generatePi Process is alive\n") 
              # self.after(DELAY1, self.onGetValue(conn, msgs))   # self.onGetValue)
              # return 
              # msg = conn.recv() 
              # self.txt.insert( msg ) 
              time.sleep(0.1) 
              

        # else:    

          # while 1:
          #     msg = conn.recv()
          #     if msg == "END":
          #         break
          #     print("Received the message: {}".format(msg))
        
            # try: 
          msg = "msg"
          msg = conn.recv() 
          print("This should be a pi: ", msg) 
          self.txt.insert(END, "\nThis should be a pi: ")               # self.queue.get(0))
          self.txt.insert(END, msg)               # self.queue.get(0))
          self.txt.insert(END, "\n") 
          self.txt.insert(INSERT, "\n\nNow running onGetValue else section.\n\n") 
          print("\nNow running onGetValue else section.\n") 

          self.pbar.stop() 
          self.startBtn.config(state=NORMAL)
          
            # except conn.Empty:   # queue.Empty:
                # print("\nqueue is PLACEKEEPER empty\n") 
                # self.txt.insert("\nqueue is PLACEKEEPER empty\n")         

            
    def generatePi(self, conn, msgs):
    # def generatePi(self, queue):
    # def generatePi(self):               self.queue, , self.parent_conn, msgs
    #                  def sender(conn, msgs):
    
        getcontext().prec = self.digits
        
        pi = Decimal(0)
        # pi=999
        k = 0
        n = self.accuracy
        
        # self.txt.delete('1.0', END) 
        # clear the outputtext text widget. 1.0 and         
        # self.txt.delete("1.0", "end-1c")
        
        #self.txt.focus() 
        
        # self.txt.delete(1.0,tk.END) # clear the outputtext text widget. 1.0 and tk.END are neccessary. tk implies the tkinter module. If you just want to add text dont incude that line
        print("\nNow running generatePi section.\n") 
        ##### self.text.put("---------------") 
        self.txt.insert(INSERT,"\n\n---------------\n\n")   
        self.txt.insert(INSERT, "\n\nNow running generatePi section.\n\n") 


        # aComment='''
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) - \
                (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5))- \
                (Decimal(1)/(8*k+6)))
            k += 1 
            
            # self.txt.insert(INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, 'Following Ports are open\n' )
            #st.insert(tkinter.INSERT, str(portlist))
            # myvar = "the answer is {}".format(answer) 
            # myvar = "the answer is " + str(answer) 
            insertToTxtfr = ("\nTextFrameTry02 is still alive = " + str(self.p1.is_alive())+"")   
            
            # insertToTxtfr = ('TextFrameTry02 is still alive = {}'.format(self.p1.is_alive())   
            # insertToTxtfr = ('TextFrameTry02 is still alive = XXX')   
                        
            print(insertToTxtfr) 
            # queue.put("TextFrameTry02 is still alive = ", self.p1.is_alive()) 
            # queue.put(" ") 
            
            # outputtext.insert(tk.END,entryvar) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            #self.txt.insert(INSERT, insertToTxtfr) # insert the entry widget contents in the text widget. tk.END is necessary.
            
            ##### self.txt.update_idletasks() 
            # XInitThreads
            # self.txt.pack
            # conn.send( insertToTxtfr )
            time.sleep(0.01) 
            # '''
            
        
            
        #### self.txt.update_idletasks() 
        # self.txt.pack
        
        print("\nNow running print out pi section.\n") 
        self.txt.insert(INSERT, "\n\nNow running print out pi section.\n\n") 
        print( pi ) 
        print( self.parent.title(), " frame end")    

        self.txt.insert(INSERT, "\n\nNow running INSERT out pi section.\n\n") 
        self.txt.insert(INSERT, pi )  
        self.txt.insert(INSERT, "\n\nDone INSERTING and printing out pi.\n\n") 
        print("\nDone INSERTING and printing out pi.\n") 

        conn.send( pi ) 
        
        #queue.put(" ") 
        #queue.put("Putting Pi from generatePi function.\n")
        #queue.put(pi) 
        #queue.put("Done putting Pi from generatePi function.\n")
        # queue.put(" ") 
        # self.txt.pack
        print("Returning from generatePi.") 
        return pi
    
#############################################################

def main():
    
    
    aComment='''
    frame = Frame(
        rootTextFrameTry01,
        text='another title try'
    ) 
    frame.pack() 
    '''
    

    aComment='''
    processes = (
        multiprocessing.Process(
            target=Example,
            name='Example',
            args=(rootA, args[0])
        ),
        multiprocessing.Process(
            target=ExampleAlso,
            name='ExampleAlso',
            args=(rootAlso, args[1])
        )
    )

    for process in processes:
        process.start()
    '''

    q = Queue()
    # queue = multiprocessing.Queue() 
    # args = (queue, queue)
  
    xPosThisFrame = 400 ; yPosThisFrame = 300
    xJump = -25 ; yJump = -25

    rootPiCruncher = tk.Tk()
    xPosThisFrame+=xJump ; yPosThisFrame+=yJump
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    ##### rootTextFrameTry01.parent.title('root title try') 
    # rootTextFrameTry01.geometry("400x350+700+300") 
    # appTextFrameTry02 = TextFrameTry02(textTextFrameTry02, q) 
    appPiCruncher = PiCruncher(rootPiCruncher, q) 
    # appTextFrameTry02.parent.title("appTextFrameTry02 title try") 
    appPiCruncher.parent.title("appPiCruncher title try") 
    appPiCruncher.parent.geometry(dotGeoStr) 

    # UnitsConverter
    xPosThisFrame+=xJump ; yPosThisFrame+=yJump
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    rootUnitsConverter = tk.Tk() 
    ##### rootTextFrameTry01.parent.title('root title try') 
    # rootTextFrameTry01.geometry("400x350+700+300") 
    # appTextFrameTry02 = TextFrameTry02(textTextFrameTry02, q) 
    appUnitsConverter = UnitsConverter(rootUnitsConverter, q) 
    # appTextFrameTry02.parent.title("appTextFrameTry02 title try") 
    appUnitsConverter.parent.title("UnitsConverter title try") 
    appUnitsConverter.parent.geometry(dotGeoStr) 

    # SpeakerDrooled
    xPosThisFrame+=xJump ; yPosThisFrame+=yJump
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    rootSpeakerDrooled = tk.Tk() 
    ##### rootTextFrameTry01.parent.title('root title try') 
    # rootTextFrameTry01.geometry("400x350+700+300") 
    # appTextFrameTry02 = TextFrameTry02(textTextFrameTry02, q) 
    appSpeakerDrooled = UnitsConverter(rootSpeakerDrooled, q) 
    # appTextFrameTry02.parent.title("appTextFrameTry02 title try") 
    appSpeakerDrooled.parent.title("SpeakerDrooled title try") 
    appSpeakerDrooled.parent.geometry(dotGeoStr) 
    
    # MenuChooseAppStarts
    xPosThisFrame+=xJump ; yPosThisFrame+=yJump
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    rootMenuChooseAppStarts = tk.Tk() 
    ##### rootTextFrameTry01.parent.title('root title try') 
    # rootTextFrameTry01.geometry("400x350+700+300") 
    # appTextFrameTry02 = TextFrameTry02(textTextFrameTry02, q) 
    appMenuChooseAppStarts = MenuChooseAppStarts(rootMenuChooseAppStarts, q) 
    # appTextFrameTry02.parent.title("appTextFrameTry02 title try") 
    appMenuChooseAppStarts.parent.title("MenuChooseAppStarts title try") 
    appMenuChooseAppStarts.parent.geometry(dotGeoStr) 

    # appAlso 
    # appA = multiprocessing.Process(target = Example,args=(rootA, q))
    xPosThisFrame+=xJump ; yPosThisFrame+=yJump
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    rootAlso = Tk()
    # rootAlso.geometry("400x350+500+200") 
    appAlso = ExampleAlso(rootAlso, q) 
    appAlso.parent.title("appAlso title try") 
    appAlso.parent.geometry(dotGeoStr) 
   

    # appA     
    xPosThisFrame+=xJump ; yPosThisFrame+=yJump
    dotGeoStr="400x350"+"+"+str(xPosThisFrame)+"+"+str(yPosThisFrame)
    rootA = Tk()
    # rootA.geometry("400x350+300+100")
    # p1 = multiprocessing.Process(target = calc_square,args=(arr,))
    appA = Example(rootA, q) 
    appA.parent.title("appA title try") 
    appA.parent.geometry(dotGeoStr) 

    aComment='''
    root = Tk()
    text = Text(root)
    text.insert(INSERT, "Hello.....")
    text.insert(END, "Bye Bye.....")
    text.pack() 
    '''
    unRoot = Tk() 
    textTTT = Text(unRoot) 
    textTTT.insert(INSERT, "Hello......") 
    textTTT.insert(END, "Bye Bye......") 
    textTTT.pack() 

    # appAlso = multiprocessing.Process(target = ExampleAlso,args=(rootAlso, q))
    
    # self.mainloop()args=(rootAlso, q))
    
    # self.mainloop()
    # rootA.mainloop()  
    # rootA.mainloop()  
    # tk.mainloop()
    
    # appA.start()
    # appAlso.start() 

    tk.mainloop()
    
    # mainloop() 
    
    #rootAlso.destroy
    #rootA.destroy


if __name__ == '__main__':
    main()  
    
    exit()
    
