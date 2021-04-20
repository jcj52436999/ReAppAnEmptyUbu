#!/usr/bin/env python3
# -*- coding: utf-8 -*-

multiLineComment='''
# reAppEventProcessLearn.py
# Created originally for learning event driven messaging code
# @author JC Jackson for study
'''

multiLineComment='''

'''

import sys



# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of sysExiter()   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def sysExiter():
    sys.exit()
  
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of sysExiter()   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj



# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# receive an input integer from keyboard
def inputIntegerOnly( promptString ): 
    while True:
        # entered = eval(input( promptString ))
        
        entered = (input( promptString ))
        print("You just entered: ", entered )
        if entered == "stop":
            # print( "Stop chosen. ") 
            reEntered = (input( "Stop chosen, all RAM data will be lost, are you sure? y or n: " ))  
            if reEntered == "y" or reEntered == "Y":
                sys.exit()
            else: 
                print( "Staying for more entry. ")
            # sys.exit()  #  break
        elif not entered.isdigit():
        # elif (( entered.isdigit() != True )):
            print( "Must be a number! ")
        else: 
            entered = int(entered)
            return entered
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of inputIntegerOnly( promptString )   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj



# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# clean new SCREEN print of cmdArray
def screenPrintCmdArray(cmdArray):

    ## cmdArray = genCmdArraySample( 5, 30 )
    ## print("Function genCmdArraySample: ", cmdArray)

    ### cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 98, 1):

        for column in range(0, 4, 1):

            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            
            
            #  cmdArrValDotTxt.write(strOut + '\n')

        print()
        #  cmdArrValDotTxt.write('\n')


    #  cmdArrValDotTxt.close()
    print()
    return  " " ## cmdArray 

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj




# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the start of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# provides a serial line by line terminal interface
def line_by_line_term_interface(cmdArray):

    import getpass
    import subprocess

    out_bytes = subprocess.check_output(['ls'])
    print(out_bytes)

    stringPiecesDict = genStrVariables()   # stringPiecesDict

    line_choice = 1
    print("")
    print("0. Choose 0 to return to previous menu.")
    print("1. Choose 1 for use of upgrade commands from original default array.")
    print("2. Choose 2 for .")
    print("3. Choose 3 for .")
    print("4. Choose 4 for outputting default cmdArray list to csv file.")
    print("5. Choose 5 for gen a file cmdArrVals.txt.")
    print("6. Choose 6 for return to previous menu. ")
    print("7. Choose 7 for cmdArray screen print check. ")
    print("8. Choose 8 to write a sample record to a sample dB.")
    print("9. Choose 9 to READ a sample record FROM a sample dB.")
    print("10. Choose 10 to WRITE a sample record TO a sample dB.")

    line_choice = inputIntegerOnly("Which number do you want? ")
        # line_choice = int(line_choice)  
 
    cmdArrayWidth = 4 ; cmdArrayHeight = 100 ; 

    if line_choice <= 0:
        # out_bytes = "Return to previous menu is chosen. sys.exit() "
        # print(); print( out_bytes )
        # sys.exit()
        out_bytes = "User chose to return to previous menu. "
        print(); print( out_bytes )
        return cmdArray  ## menuInit(cmdArray)  ## 
    elif line_choice <= 1:
        # if line_choice <= 1:
        cmdArray = genCmdArraySample( cmdArrayWidth, cmdArrayHeight )
        # cmdArray = genCmdArraySample( 4, 100 )
        print(("Function genCmdArraySample: ", cmdArray))
        line_by_line_term_interface( cmdArray )
    elif line_choice <= 2:
        cmdArray = genCmdArraySample( cmdArrayWidth, cmdArrayHeight )
        print(("Function genCmdArraySample: ", cmdArray))
        line_by_line_term_interface( cmdArray )
    elif line_choice <= 3:
        cmdArray = genCmdArraySample( 4, 100 )
        print(("Function genCmdArraySample: ", cmdArray))
        line_by_line_term_interface( cmdArray )
    elif line_choice <= 4:
        out_bytes = genaFile_cmdArrValsDotTxt( cmdArrayWidth, cmdArrayHeight )
        print( out_bytes )
        line_by_line_term_interface( cmdArray )
    elif line_choice <= 5:
        out_bytes = genaFile_cmdArrValsDotTxt( cmdArrayWidth, cmdArrayHeight )
        print( out_bytes )
        line_by_line_term_interface( cmdArray )
    elif line_choice <= 6:
        out_bytes = "User chose to return to previous menu. "
        print(); print( out_bytes )
        return cmdArray  ## menuInit(cmdArray)  ## 
    elif line_choice <= 7:
        out_bytes = "User chose to run cmdArray screen printout. "
        print(); print( out_bytes )
        # sys.exit(main())
        out_bytes = screenPrintCmdArray(cmdArray)
        line_by_line_term_interface(cmdArray)
    elif line_choice <= 8:
        out_bytes = "User chose to write a sample record to a sample dB. "
        print(); print( out_bytes )
        # sys.exit(main())
        out_bytes = writeSmplRecordToPostgresDbTable()
        line_by_line_term_interface(cmdArray)
    elif line_choice <= 9:
        out_bytes = "User chose to READ a sample record FROm the sample dB. "
        print(); print( out_bytes )
        # sys.exit(main())
        out_bytes = readSmplRecordFromPostgresDbTable()
        line_by_line_term_interface(cmdArray)
    elif line_choice <= 10:
        out_bytes = "User chose to WRITE a sample record TO the sample dB. "
        print(); print( out_bytes )
        # sys.exit(main())
        out_bytes = writeRecordToPostgresDbTable(" ", " ", " ")
        line_by_line_term_interface(cmdArray)
    elif line_choice > 98:
        out_bytes = "User chose to exit this menu. "
        print(); print( out_bytes )
        return  # sys.exit(main())
    else:
        ### cmdArray = genCmdArraySample()
        ### print("Function genCmdArraySample: ", cmdArray)
        out_bytes = "Entry is out of range." # line_by_line_term_interface()
        print(); print( out_bytes )
        line_by_line_term_interface(cmdArray) ## sys.exit(main())

    return out_bytes

    print("")
    print("Need sudo password to install software.")

    user = getpass.getuser()
    userPassWd = getpass.getpass()

    print(user)
    # print(userPassWd)

    # out_bytes = subprocess.check_output(['apt-get ', 'update', shell=True])
    # cmdLine = ['echo ' + userPassWd + ' | sudo -S apt-get update']
    # cmdLine = "sudo apt-get update"
    # out_bytes = subprocess.Popen(cmdLine, shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    # out_bytes = subprocess.Popen(cmdLine , shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # echo "yourpassword" | sudo -S apt-get autoremove
    # proc = subprocess.Popen('apt-get install -y filetoinstall', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # out_bytes = aptGetShellBash(cmdLine)
    out_bytes = repeatAptGetShellBash(userPassWd, cmdArray)

    return out_bytes

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
###########################################################################################




# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# clean new SCREEN print of cmdArray
def genCmdArray():

    cmdArray = genCmdArraySample( 5, 99 )
    ## print("Function genCmdArraySample: ", cmdArray)

    ### cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 98, 1):

        for column in range(0, 4, 1):

            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            
            
            #  cmdArrValDotTxt.write(strOut + '\n')

        print()
        #  cmdArrValDotTxt.write('\n')


    #  cmdArrValDotTxt.close()
    print()
    return cmdArray 

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj


###########################################################################################
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of menuInit   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def menuInit(cmdArray):

###############################################

    # from tkinter import *
    # import tkinter
    
    import tkinter as tk
    from tkinter import Menu
    from tkinter.filedialog import askopenfilename
    
    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()
       
    root = tk.Tk()
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
    
    
    root.config(menu=menubar)
    root.mainloop()
    

################################################


    ######  temp block pygame allowing test of rest of file
    #import pygame
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

    ## DEFAULT menuLineItems 
    menuLineItems = { 
      '0': ["0. Choose 0 to return to previous menu. ","sysExiter"],
      '1': ["1. Choose 1 for Cursed terminal interface.","line_by_line_term_interface"],
      '2': ["2. Choose 2 for hand built terminal interface.","line_by_line_term_interface"],
      '3': ["3. Choose 3 for line by line terminal interface.","line_by_line_term_interface"],
      '4': ["4. Choose 4 to print present cmdArray to console.","screenPrintCmdArray"],
      '5': ["5. Choose 5 to gen up this apps default internal Ubu app dB. ","genCmdArray"],
      '6': ["6. Choose 6 to EXIT program.","sysExiter"]
      } 
      
    menuLineReactions = { 
      'genCmdArray': genCmdArray,
      'line_by_line_term_interface': line_by_line_term_interface,
      'menuInit': menuInit,
      'screenPrintCmdArray': screenPrintCmdArray, 
      'sysExiter': sysExiter, 
      ## ' ': " "
      'sys.exit()': "sys.exit()"  ## sys.exit()
      } 

    while True:
          
        print(" ")
        line_choice = 3
        print("")
        tempHold = menuLineItems["0"]; tempHold = tempHold[0]; print( tempHold );
        tempHold = menuLineItems["1"]; tempHold = tempHold[0]; print( tempHold );
        tempHold = menuLineItems["2"]; tempHold = tempHold[0]; print( tempHold );
        tempHold = menuLineItems["3"]; tempHold = tempHold[0]; print( tempHold );
        tempHold = menuLineItems["4"]; tempHold = tempHold[0]; print( tempHold );
        tempHold = menuLineItems["5"]; tempHold = tempHold[0]; print( tempHold );
        tempHold = menuLineItems["6"]; tempHold = tempHold[0]; print( tempHold );
        line_choice = inputIntegerOnly("Which number do you want? ")
        # line_choice = int(line_choice)  
        #''' 
        #def inputIntegerOnly( promptString ): 
        #    while True:
        #        inputted = input( promptString )
        #        if inputted == "stop":
        #        print( "Stop chosen. ") 
        #        break
        #    elif not inputted.isdigit():
        #        print( "Must be a number! ")
        #    else: 
        #        inputted = int(inputted)
        #        return inputted
        #''' 
 
        if line_choice <= 0:
            out_bytes = "Return to previous menu is chosen. sys.exit() "
            print(); print( out_bytes ) 

            reEntered = (input( "Stop chosen, all RAM data will be lost, are you sure? y or n: " ))  
            if reEntered == "y" or reEntered == "Y":
                return   #sys.exit()       sys.exit()
            else: 
                print( "Staying for more entry. ")
            # sys.exit()  #  break


        elif line_choice <= 1:
            tempHold = menuLineItems["1"]; tempHold = tempHold[1]; ## print( tempHold );
            out_bytes = menuLineReactions[ tempHold ](cmdArray); 
            ## out_bytes = line_by_line_term_interface(cmdArray);
            ### menuInit( cmdArray );
        elif line_choice <= 2:
            tempHold = menuLineItems["2"]; tempHold = tempHold[1]; ## print( tempHold );
            out_bytes = menuLineReactions[ tempHold ](cmdArray); 
            ## out_bytes = line_by_line_term_interface(cmdArray)
            ### menuInit( cmdArray )
        elif line_choice <= 3:
            tempHold = menuLineItems["3"]; tempHold = tempHold[1]; ## print( tempHold );
            cmdArray = menuLineReactions[ tempHold ](cmdArray); 
            ## cmdArray = line_by_line_term_interface(cmdArray)
            ### menuInit( cmdArray )
        elif line_choice <= 4:
            tempHold = menuLineItems["4"]; tempHold = tempHold[1]; ## print( tempHold );
            menuLineReactions[ tempHold ](cmdArray); 
            ## screenPrintCmdArray( cmdArray )
            ### print( out_bytes )
            menuInit( cmdArray )
        elif line_choice <= 5:
            tempHold = menuLineItems["5"]; tempHold = tempHold[1]; ## print( tempHold );
            cmdArray = menuLineReactions[ tempHold ](); 
            ## cmdArray = genCmdArray()  # genCmdArray()
            # print( out_bytes )
            ### menuInit( cmdArray )
        elif line_choice <= 6:
            out_bytes = "Exit program is chosen. sys.exit() ";
            print(); print( out_bytes );
            tempHold = menuLineItems["6"]; 
            tempHold = tempHold[1]; ## print( tempHold );
            ## cmdArray = " " ;   
            ## cmdArray = menuLineReactions[ tempHold ](); 

            reEntered = (input( "Stop chosen, all RAM data will be lost, are you sure? y or n: " ))  
            if reEntered == "y" or reEntered == "Y":
                return   #sys.exit()       sys.exit()
            else: 
                print( "Staying for more entry. ")
            # sys.exit()  #  break


            ## return ### 
            ## sys.exit() ; 
        elif line_choice > 98:
            out_bytes = "# jcj-jcj-jcj- Function Menuinit is ending with sys.exit(): "
            print(); print( out_bytes )
            # print("# jcj-jcj-jcj- Function Menuinit is ending with sys.exit(): ", out_bytes)


            reEntered = (input( "Stop chosen, all RAM data will be lost, are you sure? y or n: " ))  
            if reEntered == "y" or reEntered == "Y":
                return   #sys.exit()       sys.exit()
            else: 
                print( "Staying for more entry. ")
            # sys.exit()  #  break


            ## return  # sys.exit()
        else:
            out_bytes = "Entry is out of range." # line_by_line_term_interface()
            print(); print( out_bytes )
            ### menuInit( cmdArray )



    # out_bytes.wait()

    print(" ")
    print(" ")
    return
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of menuInit   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
    ## if __name__ == "__main__":
    ## sys.exit(main())


# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of main   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def main(argv=None):
    import sys
    if argv is None:
        argv = sys.argv
        lenArgv = len(sys.argv)

    print(" ")
    print("# jcj-jcj-jcj- START OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    thisProgramIs = "reAppEventProcessLearn.py"
    print(("Start of program in Main " + thisProgramIs))
    print(" ")

    # import sys 
    import curses
    import getpass
    import os
    import shutil
    import subprocess
    import pprint
    # import pformat 
     
    from subprocess import Popen, PIPE, STDOUT

    # import urwid
    import numpy
    #import pygame
    import tkinter

    #'''
    #Trying to install a favorite set of Ubu software.
    #'''
    
    w = 5
    h = 99
    cmdArrayWidth = w
    cmdArrayHeight = h 
    cmdArray = {( w, h): " " for w in range(cmdArrayWidth) for h in range(cmdArrayHeight)}

    menuInit( cmdArray )

    # out_bytes.wait() 
    out_bytes = " " 
    print(("# jcj-jcj-jcj-" + thisProgramIs + " Function Main is ending with sys.exit(): ", out_bytes))

    print(" ")
    print("# jcj-jcj-jcj- END OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    print(" ") 
    
    
    multiLineComment=''' code from turtle example
    def advance_state_machine():
        global state_num
        if state_num == 0:       # Transition from state 0 to state 1
            tess.forward(70)
            tess.fillcolor("orange")
            state_num = 1
        elif state_num == 1:     # Transition from state 1 to state 2
            tess.forward(70)
            tess.fillcolor("red")
            state_num = 2
        else:                    # Transition from state 2 to state 0
            tess.back(140)
            tess.fillcolor("green")
            state_num = 0
    
    # Bind the event handler to the space key.
    wn.onkey(advance_state_machine, "space")
    
    wn.listen()                      # Listen for events
    wn.mainloop()
    '''
    
    return()
    
    
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of main   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
if __name__ == "__main__":
    print(" ")
    print(" YES, we really are at the bottom of the progam, STARTING MAIN FUNCTION! ")
    print(" ")
    main()
    # sys.exit(main())
    sys.exit()





























