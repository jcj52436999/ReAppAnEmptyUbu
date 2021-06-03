#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# mainMenuThisAppTry01.py 

#####################################################
# class TextFrameTry02(Frame):
class MainMenuThisApp(Frame):
        print() 


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
def main(): 

    # q = Queue()
    # queue = multiprocessing.Queue() 
    # args = (queue, queue)

    xy=mainMenuThisApp() 

####################################################################
if __name__ == '__main__':
    main()  
    
    exit()
    
