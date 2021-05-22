#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# calculate_pi-add-another.py
# Created originally in 2021 as a simplistic exercise in broad-spectrum py use
# copied from web and modified for study @author Joe Jackson 
# choosing to expand this into a multi-window parallel processing app



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
from tkinter import (Tk, BOTH, Text, E, W, S, N, END, 
    NORMAL, DISABLED, StringVar)
from tkinter.ttk import Frame, Label, Button, Progressbar, Entry
from tkinter import scrolledtext

import multiprocessing
from multiprocessing import Queue, Process
import queue 
from decimal import Decimal, getcontext

DELAY1 = 80
DELAY2 = 20

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
        
        self.txt = scrolledtext.ScrolledText(self)  
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
            print ("Example frame is still alive = ", self.p1.is_alive())
            # queue.put("Example frame is still alive = ", self.p1.is_alive())
            
        queue.put(pi)    
        print("Example frame end")    


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
        
        self.txt = scrolledtext.ScrolledText(self)  
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



class TextFrameTry01(Frame):
  
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

        self.parent.title("TextFrameTry01")
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
        
        self.txt = scrolledtext.ScrolledText(self)  
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




def main():
    
    q = Queue()
    # queue = multiprocessing.Queue() 
    # args = (queue, queue)
  
    rootA = Tk()
    rootAlso = Tk()
    rootTextFrameTry01 = Tk()
    rootA.geometry("400x350+300+100")
    rootAlso.geometry("400x350+500+200") 
    rootTextFrameTry01.geometry("400x350+700+300") 

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

    # p1 = multiprocessing.Process(target = calc_square,args=(arr,))
    appA = Example(rootA, q) 

    # appA = multiprocessing.Process(target = Example,args=(rootA, q))

    appAlso = ExampleAlso(rootAlso, q) 

    appTextFrameTry01 = TextFrameTry01(rootTextFrameTry01, q) 


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
    
