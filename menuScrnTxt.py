#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# menuScrnTxt.py
# Created on Mon Mar  8 16:17:50 2021
# @author: jcj52436999

# menuScrnTxt.py-2021-03-08-1641-just noting a general restart in efforts here

import sys

def printTest2():
    
    if 0 == 0 :
        print(" ")
        print("# jcj-jcj-jcj- TOP START OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
        thisProgramIs = "menuScrnTxt.py"
        print(("Top of Start of program " + thisProgramIs))
        print(" ")
    return


def printTest2():

    if 0 == 0 :
        print(" ")
        print("# jcj-jcj-jcj- printTest2() - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
        thisProgramIs = "menuScrnTxt.py"
        print(("printTest2() " + thisProgramIs))
        print(" ")
    return


#  import 

def menuInit(cmdArray):

    if 0 == 0 :
        print(" ")
        print("# jcj-jcj-jcj- TOP START OF def menuInit - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
        thisProgramIs = "menuScrnTxt.py"
        print(("start of menuInit of program " + thisProgramIs))
        print(" ") 
        
    return


# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of main   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def main(argv=None):
    #import sys
    if argv is None:
        argv = sys.argv
        lenArgv = len(sys.argv) 
        pyScriptProgramName = sys.argv[0]


    print(" ")
    print("# jcj-jcj-jcj- START OF PROGRAM IN MAIN - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    thisProgramIs = "menuScrnTxt.py"
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
    import pygame
    import tkinter
    
    print ("  ") 

    # Trying to install a favorite set of Ubu software.
    
    #tempHold = tempHold[1] 
            ## print( tempHold )
            ## cmdArray = " " ;   
            ## cmdArray = menuLineReactions[ tempHold ](); 

    reEntered = (input( "Stop chosen, all RAM data will be lost, are you sure? y or n: " ))  
    if reEntered == "y" or reEntered == "Y":
        return   #sys.exit()       sys.exit()
    else: 
        print( "Staying for more entry. ")
        
    # 
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
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of main   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
if __name__ == "__main__":
    sys.exit(main())


# =============================================================================
# 
# def main():
#     ...
# 
# if __name__ == "__main__":
#     main()
# 
# 
# =============================================================================



