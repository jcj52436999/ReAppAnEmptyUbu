#  reAppAnEmptyUbu.py
'''
reAppAnEmptyUbu.py
@author Joe Jackson 

reAppAnEmptyUbu-201803231857-postgres-menus-now-work-rudimen-tosh-and-acer.py
reAppAnEmptyUbu-2018-03-21-0215-making-generalizable-menus.py
reAppAnEmptyUbu-2018-03-21-0212-months-of-off-and-on-work.py


'''

import sys
import pickle
import json
import sqlite3
import psycopg2
import django
import numpy 

'''
w = 5
h = 99
cmdArrayWidth = w
cmdArrayHeight = h 
cmdArray = {( w, h): " " for w in range(cmdArrayWidth) for h in range(cmdArrayHeight)}
'''

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# clean new SCREEN print of cmdArray
def genStrVariables():   # stringPiecesDict
    '''
    aSpace = str(32)      # String.fromCharCode(32);    
    aDblQuote = str(34)   # String.fromCharCode(34); 
    aSnglQuote = str(39)   # String.fromCharCode(39);  
    aComma = str(44)      # String.fromCharCode(44); 
    aColon = str(58)      # String.fromCharCode(58); 
    aSemiColon = str(59)      # String.fromCharCode(59); 
    aForeSlash = str(47)      # String.fromCharCode(47); 
    aBackSlash = str(92)      # String.fromCharCode(92);  
    aLF = str(10)      # String.fromCharCode(10); 
    aCR = str(13)      # String.fromCharCode(13); 
    aLfCr = aLF + aCR 
    aCrLf = aCR + aLF 
    aColonSpaceDblQuote = aColon + aSpace + aDblQuote
    example = "example" 
    '''
    '''
    screenWidthAvail = self.width()
    screenHeightAvail = self.height()
    
    var screenWidthAvail = screen.availWidth ;  # in JS
    var screenHeightAvail = screen.availHeight ; 
    '''  
    stringPiecesDict = ({"aSpace": str(32), "aDblQuote": str(34)},
            {"aSnglQuote": str(39), "aComma": str(44)},
            {"aColon": str(58), "aSemiColon": str(59)},
            {"aForeSlash": str(47), "aBackSlash": str(92)},
            {"aLF": str(10), "aCR": str(13)},
            {"aLfCr": str(10) + str(13), "aCrLf": str(13) + str(10)},
            {"aColonSpaceDblQuote": str(58) + str(32) + str(34)}
            )
    return stringPiecesDict

    # jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of genStrVariables()   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
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

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

def genaFile_cmdArrValsDotCsv( cmdArrayWidth, cmdArrayHeight ):
    # genCmdArraySample( cmdArrayWidth, cmdArrayHeight )
    cmdArray = genCmdArraySample( cmdArrayWidth, cmdArrayHeight ) # genCmdArraySample()
    ## print("Function genCmdArraySample: ", cmdArray)

    cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 55, 1):

        for column in range(0, 4, 1):
            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            strOut = "    cmdArray[(" + str(row) + ", " + str(column) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print(("    To" + strOut))
            cmdArrValDotTxt.write(strOut + '\n')

        print()
        cmdArrValDotTxt.write('\n')


    cmdArrValDotTxt.close()
    print()
    return

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

def genaFile_cmdArrHeadersAndValsIntoListOfDicts( cmdArrayWidth, cmdArrayHeight ):

    cmdArray = genCmdArraySample( cmdArrayWidth, cmdArrayHeight )
    ## print("Function genCmdArraySample: ", cmdArray)

    cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 55, 1):

        for column in range(0, 4, 1):
            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            strOut = "    cmdArray[(" + str(row) + ", " + str(column) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print(("    To" + strOut))
            cmdArrValDotTxt.write(strOut + '\n')

        print()
        cmdArrValDotTxt.write('\n')


    cmdArrValDotTxt.close()
    print()
    return

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

def genaFile_cmdArrValsDotTxt( cmdArrayWidth, cmdArrayHeight ):  # Gens txt file with some reversals

    cmdArray = genCmdArraySample( cmdArrayWidth, cmdArrayHeight )
    ## print("Function genCmdArraySample: ", cmdArray)

    cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 55, 1):

        for column in range(0, 4, 1):
            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            strOut = "    cmdArray[(" + str(row) + ", " + str(column) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print(("    To" + strOut))
            cmdArrValDotTxt.write(strOut + '\n')

        print()
        cmdArrValDotTxt.write('\n')


    cmdArrValDotTxt.close()
    print()
    return " "
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the start of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# Generates as a dev default an array of apt-get command lines
def genCmdArraySample( cmdArrayWidth, cmdArrayHeight ):
    if (cmdArrayWidth < 1):
      w = 5; cmdArrayWidth = w

    if (cmdArrayHeight < 1):
      h = 99; cmdArrayHeight = h
    '''  
    w = 5
    h = 99
    cmdArrayWidth = w
    cmdArrayHeight = h 
    '''
    cmdArray = {( w, h): " " for w in range(cmdArrayWidth) for h in range(cmdArrayHeight)}
    cmdArrLineNum = 0

    '''
    w = 5
    h = 60
    width = w
    height = h
    cmdArray = {(w, h): " " for w in range(width) for h in range(height)}
    '''

    # y is record number
    # x is item in record
    # x is 0 for a unique name for the desired command line
    # x is 1 for the command line itself
    # x is 2 for a list of strings as properties of the command
    # x is 3 for archive ppa if needed
    # x is 4 for archive key if needed

    # array db headers
    cmdArray[(0, 0)] = "unique-name"
    cmdArray[(1, 0)] = "command"
    cmdArray[(2, 0)] = "cmd-properties"
    cmdArray[(3, 0)] = "ppa"

    cmdArray[(0, 1)] = "apt-get-update"
    cmdArray[(1, 1)] = "sudo -S apt-get update"
    cmdArray[(2, 1)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 1)] = " "

    cmdArray[(0, 2)] = "apt-get-upgrade"
    cmdArray[(1, 2)] = "sudo -S apt-get upgrade -y"
    cmdArray[(2, 2)] = '("UbuSingleLineSimple",)'  # ("UbuComplex", "GeneratesRebootReq")
    cmdArray[(3, 2)] = " "

    cmdArray[(0, 3)] = "apt-get-autoremove"
    cmdArray[(1, 3)] = "sudo -S apt-get autoremove -y"
    cmdArray[(2, 3)] = "UbuSingleLineSimple"
    cmdArray[(3, 3)] = " "

    cmdArray[(0, 4)] = "apt-get-autoclean"
    cmdArray[(2, 4)] = "sudo -S apt-get autoclean -y"
    cmdArray[(3, 4)] = "UbuSingleLineSimple"
    cmdArray[(4, 4)] = " "

    cmdArray[(0, 5)] = "apt-get-install-git"
    cmdArray[(1, 5)] = "sudo -S apt-get install -y git"
    cmdArray[(2, 5)] = "UbuSingleLineSimple"
    cmdArray[(3, 5)] = " "

    cmdArray[(0, 6)] = "apt-get-install-ojava7-installer"
    cmdArray[(1, 6)] = "sudo -S apt-get install -y oracle-java7-installer"
    cmdArray[(2, 6)] = '("UbuComplex", "InstOfInstaller", "NeedsPpa", "NoKey")'
    cmdArray[(3, 6)] = "sudo add-apt-repository ppa:webupd8team/java"

    cmdArray[(0, 7)] = "apt-get-install-ojava8-installer"
    cmdArray[(1, 7)] = "sudo -S apt-get install -y oracle-java8-installer"
    cmdArray[(2, 7)] = '("UbuComplex", "InstOfInstaller", "NeedsPpa", "NoKey")'
    cmdArray[(3, 7)] = "sudo add-apt-repository ppa:webupd8team/java"

    cmdArray[(0, 8)] = "apt-get-opera-stable"
    cmdArray[(1, 8)] = "sudo -S apt-get install -y opera-stable"
    cmdArray[(2, 8)] = '("UbuComplex", "InstOfInstaller", "NeedsPpa", "NeedsKey")'
    cmdArray[(3, 8)] = ""
    cmdArray[(4, 8)] = ""

    cmdArray[(0, 9)] = "apt-get-firefox"
    cmdArray[(1, 9)] = "sudo -S apt-get install -y firefox"
    cmdArray[(2, 9)] = "UbuSingleLineSimple"
    cmdArray[(3, 9)] = " "

    cmdArray[(0, 10)] = "apt-get-chrome"
    cmdArray[(1, 10)] = "sudo -S apt-get install -y google-chrome-stable"
    cmdArray[(2, 10)] = '("UbuComplex", "InstOfInstaller", "NeedsPpa", "NeedsKey")'
    # cmdArray[(10, 3)] = "sudo sh -c 'echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list'"  
    cmdArray[(3, 10)] = "sudo sh -c 'echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list'"
    cmdArray[(4, 10)] = "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -"

    cmdArray[(0, 11)] = "apt-get-canary"
    cmdArray[(1, 11)] = "sudo -S apt-get install -y google-chrome-canary"
    cmdArray[(2, 11)] =  '("UbuComplex", "InstOfInstaller", "NeedsPpa", "NeedsKey")'
    # cmdArray[(11, 3)] = "sudo sh -c 'echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list'"
    cmdArray[(3, 11)] = "sudo sh -c 'echo 'deb http://dl.google.com/linux/chrome/deb/ canary main' >> /etc/apt/sources.list.d/google.list'"
    cmdArray[(4, 11)] = "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -"

    cmdArray[(0, 12)] = "apt-get-shutter"
    cmdArray[(1, 12)] = "sudo -S apt-get install -y shutter"
    cmdArray[(2, 12)] = "UbuSingleLineSimple"
    cmdArray[(3, 12)] = " "

    cmdArray[(0, 13)] = "apt-get-stellarium"
    cmdArray[(1, 13)] = "sudo -S apt-get install -y stellarium"
    cmdArray[(2, 13)] = "UbuSingleLineSimple"
    cmdArray[(3, 13)] = " "

    cmdArray[(0, 14)] = "apt-get-atom"
    cmdArray[(1, 14)] = "sudo -S apt-get install -y atom"
    cmdArray[(2, 14)] = "UbuComplex"
    cmdArray[(3, 14)] = " "

    cmdArray[(0, 15)] = "apt-get-idle3"
    cmdArray[(1, 15)] = "sudo -S apt-get install -y idle3"
    cmdArray[(2, 15)] = "UbuSingleLineSimple"
    cmdArray[(3, 15)] = " "

    cmdArray[(0, 16)] = "apt-get-gcommander"
    cmdArray[(1, 16)] = "sudo -S apt-get install -y gnome-commander"
    cmdArray[(2, 16)] = "UbuSingleLineSimple"
    cmdArray[(3, 16)] = " "

    cmdArray[(0, 17)] = "apt-get-python3-urwid"
    cmdArray[(1, 17)] = "sudo -S apt-get install -y python3-urwid"
    cmdArray[(2, 17)] = "UbuSingleLineSimple"
    cmdArray[(3, 17)] = " "

    cmdArray[(0, 18)] = "apt-get-ncurses"
    cmdArray[(1, 18)] = "sudo -S apt-get install -y libncurses5-dev libncursesw5-dev ncurses-doc"
    cmdArray[(2, 18)] = "UbuSingleLineSimple"
    cmdArray[(3, 18)] = " "

    cmdArray[(0, 19)] = "apt-get-telegram"
    cmdArray[(1, 19)] = "sudo -S apt-get install -y telegram"
    cmdArray[(2, 19)] = "UbuComplex"
    cmdArray[(3, 19)] = " "

    cmdArray[(0, 20)] = "apt-get-bpython3"
    cmdArray[(1, 20)] = "sudo -S apt-get install -y bpython3"
    cmdArray[(2, 20)] = "UbuSingleLineSimple"
    cmdArray[(3, 20)] = " "

    cmdArray[(0, 21)] = "apt-get-ipython3"
    cmdArray[(1, 21)] = "sudo -S apt-get install -y ipython3"
    cmdArray[(2, 21)] = "UbuSingleLineSimple"
    cmdArray[(3, 21)] = " "

    cmdArray[(0, 22)] = "apt-get-gimp"
    cmdArray[(1, 22)] = "sudo -S apt-get install -y gimp"
    cmdArray[(2, 22)] = "UbuSingleLineSimple"
    cmdArray[(3, 22)] = " "

    cmdArray[(0, 23)] = "apt-get-qrq"
    cmdArray[(1, 23)] = "sudo -S apt-get install -y qrq"
    cmdArray[(2, 23)] = "UbuSingleLineSimple"
    cmdArray[(3, 23)] = " "

    cmdArray[(0, 24)] = "apt-get-spyder3"
    cmdArray[(1, 24)] = "sudo -S apt-get install -y spyder3"
    cmdArray[(2, 24)] = "UbuSingleLineSimple"
    cmdArray[(3, 24)] = " "

    cmdArray[(0, 25)] = "apt-get-gperiodic"
    cmdArray[(1, 25)] = "sudo -S apt-get install -y gperiodic"
    cmdArray[(2, 25)] = "UbuSingleLineSimple"
    cmdArray[(3, 25)] = " "

    cmdArray[(0, 26)] = "apt-get-inkscape"
    cmdArray[(1, 26)] = "sudo -S apt-get install -y inkscape"
    cmdArray[(2, 26)] = "UbuSingleLineSimple"
    cmdArray[(3, 26)] = " "

    cmdArray[(0, 27)] = "apt-get-blender"
    cmdArray[(1, 27)] = "sudo -S apt-get install -y blender"
    cmdArray[(2, 27)] = "UbuSingleLineSimple"
    cmdArray[(3, 27)] = " "

    cmdArray[(0, 28)] = " "
    cmdArray[(1, 28)] = " "
    cmdArray[(2, 28)] = "UbuSingleLineSimple"
    cmdArray[(3, 28)] = " "

    cmdArray[(0, 29)] = "apt-get-slack"
    cmdArray[(1, 29)] = "sudo -S apt-get install -y slack"
    cmdArray[(2, 29)] = "UbuComplex"
    cmdArray[(3, 29)] = " "

    cmdArray[(0, 30)] = "apt-get-esl-erlang"
#   cmdArray[(1, 30)] = "sudo -S apt-get install -y esl-erlang"
    cmdArray[(1, 30)] = "sudo -S apt-get install -y erlang"
    cmdArray[(2, 30)] = '("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")'
    cmdArray[(3, 30)] = "wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb"

    cmdArray[(0, 31)] = "apt-get-elixir"
    cmdArray[(1, 31)] = "sudo -S apt-get install -y elixir"
    cmdArray[(2, 31)] = '("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")'
    cmdArray[(3, 31)] = "wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb"

    cmdArray[(0, 32)] = "apt-get-gparted"
    cmdArray[(1, 32)] = "sudo -S apt-get install -y gparted"
    cmdArray[(2, 32)] = "UbuSingleLineSimple"
    cmdArray[(3, 32)] = " "

    cmdArray[(0, 33)] = "apt-get-zim"
    cmdArray[(1, 33)] = "sudo -S apt-get install -y zim"
    cmdArray[(2, 33)] = "UbuSingleLineSimple"
    cmdArray[(3, 33)] = " "

    cmdArray[(0, 34)] = "apt-get-gfortran"
    cmdArray[(1, 34)] = "sudo -S apt-get install -y gfortran"
    cmdArray[(2, 34)] = "UbuSingleLineSimple"
    cmdArray[(3, 34)] = " "

    cmdArray[(0, 35)] = "apt-get-gfortran-5"
    cmdArray[(1, 35)] = "sudo -S apt-get install -y gfortran-5"
    cmdArray[(2, 35)] = "UbuSingleLineSimple"
    cmdArray[(3, 35)] = "sudo apt-add-repository ppa:ubuntu-toolchain-r/test"

    cmdArray[(0, 36)] = "apt-get-gfortran-6"
    cmdArray[(1, 36)] = "sudo -S apt-get install -y gfortran-6"
    cmdArray[(2, 36)] = "UbuSingleLineSimple"
    cmdArray[(3, 36)] = "sudo apt-add-repository ppa:ubuntu-toolchain-r/test"

    cmdArray[(0, 37)] = "apt-get-postgresqlStuff XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    cmdArray[(1, 37)] = "sudo -S apt-get install -y postgresql libpq-dev postgresql-client postgresql-client-common"
    cmdArray[(2, 37)] = "UbuSingleLineSimple"
    cmdArray[(3, 37)] = " "

    cmdArray[(0, 38)] = "apt-get-pythonStuff"
    cmdArray[(1, 38)] = "sudo -S apt-get install -y virtualenv python-pip python3-dev"
    cmdArray[(2, 38)] = "UbuSingleLineSimple"
    cmdArray[(3, 38)] = " "

    cmdArray[(0, 39)] = "apt-get-natron"
    cmdArray[(1, 39)] = "sudo -S apt-get install -y virtualenv python-pip natron"
    cmdArray[(2, 39)] = '("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")'
    cmdArray[(3, 39)] = " "

    cmdArray[(0, 40)] = "apt-get-lightworks"
    cmdArray[(1, 40)] = "sudo -S apt-get install -y virtualenv python-pip lightworks"
    cmdArray[(2, 40)] = '("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")'
    cmdArray[(3, 40)] = " "

    cmdArray[(0, 41)] = "apt-get-xbase"
    cmdArray[(1, 41)] = "sudo -S apt-get install -y virtualenv python-pip xbase"
    cmdArray[(2, 41)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 41)] = " "

    cmdArray[(0, 42)] = "apt-get-clementine"
    cmdArray[(1, 42)] = "sudo -S apt-get install -y virtualenv python-pip clementine"
    cmdArray[(2, 42)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 42)] = " "

    cmdArray[(0, 43)] = "apt-get-rawtherapee"
    cmdArray[(1, 43)] = "sudo -S apt-get install -y virtualenv python-pip rawtherapee"
    cmdArray[(2, 43)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 43)] = " "

    cmdArray[(0, 44)] = "apt-get-bluefish"
    cmdArray[(1, 44)] = "sudo -S apt-get install -y virtualenv python-pip bluefish"
    cmdArray[(2, 44)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 44)] = " "

    cmdArray[(0, 45)] = "apt-get-openscad"
    cmdArray[(1, 45)] = "sudo -S apt-get install -y virtualenv python-pip openscad"
    cmdArray[(2, 45)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 45)] = " "

    cmdArray[(0, 46)] = "apt-get-openshot"
    cmdArray[(1, 46)] = "sudo -S apt-get install -y virtualenv python-pip openshot"
    cmdArray[(2, 46)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 46)] = " "

    cmdArray[(0, 47)] = "apt-get-openshot"
    cmdArray[(1, 47)] = "sudo -S apt-get install -y virtualenv python-pip josm"
    cmdArray[(2, 47)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 47)] = " "

    cmdArray[(0, 48)] = "apt-get-logism"
    cmdArray[(1, 48)] = "sudo -S apt-get install -y logism"
    cmdArray[(2, 48)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 48)] = " "

    cmdArray[(0, 49)] = "apt-get-spyder3"
    cmdArray[(1, 49)] = "sudo -S apt-get install -y spyder3"
    cmdArray[(2, 49)] = '("UbuSingleLineSimple",)'
    cmdArray[(3, 49)] = " "

#########################################################################

    cmdArrLineNum = 50 ## cmdArrLineNum + 1  ## 50
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-dosbox"
    cmdArray[( 1, cmdArrLineNum )] = ""   # "dosbox"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 51
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-virtualbox"
    cmdArray[( 1, cmdArrLineNum )] = ""   # "virtualbox"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 52
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-maxima"
    cmdArray[( 1, cmdArrLineNum )] = ""   # "maxima"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 53
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-pymapper"
    cmdArray[( 1, cmdArrLineNum )] = ""   # "pymapper"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 54
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-winetricks"
    cmdArray[( 1, cmdArrLineNum )] = ""   # "winetricks"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 55
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-herculesstudio"
    cmdArray[( 1, cmdArrLineNum )] = ""   # "herculesstudio"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 56
    cmdArray[ 0, cmdArrLineNum ] = "apt-get-veracrypt"
    cmdArray[ 1, cmdArrLineNum ] = " " 
    cmdArray[ 2, cmdArrLineNum ] = " "
    cmdArray[ 3, cmdArrLineNum ] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 57
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-emacs25"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install emacs25"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo apt-add-repository -y ppa:adrozdoff/emacs"

    cmdArrLineNum = cmdArrLineNum + 1  ## 58
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-zimdesktop"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 59
    cmdArray[( 0, cmdArrLineNum )] = " "
    cmdArray[( 1, cmdArrLineNum )] = ""   # "lightworks"
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 60
    cmdArray[( 0, cmdArrLineNum )] = " "
    cmdArray[( 1, cmdArrLineNum )] = ""   # "natron"
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 61
    cmdArray[( 0, cmdArrLineNum )] = " "
    cmdArray[( 1, cmdArrLineNum )] = ""   # "rcmdr r rstudio"
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 62
    cmdArray[( 0, cmdArrLineNum )] = " "
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 63
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-android-studio"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 64
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-gnome-commander"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 65
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-putty-ssh-client"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 66
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-telegram"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 67
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-slack"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 68
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-atom"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 69
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-oracle-virtualbox"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1   ##  70
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-clementine"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 71
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-JOSM"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  72
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-gnucash"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  73
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-scribus"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  74
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-zoom"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  75
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-xbase"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  76
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-rawtherapee"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  77
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-openscad"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  78
    cmdArray[( 0, cmdArrLineNum )] = "app-get-postgresforms  XXXXXXXXXXXXXXXXXXXXXXXXXX"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  79
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-undetbootin"
    cmdArray[( 1, cmdArrLineNum )] = " "
    cmdArray[( 2, cmdArrLineNum )] = " "
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  80
    cmdArray[( 0, cmdArrLineNum )] = "apt-get-umake"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install -y ubuntu-make && sudo apt-get update && sudo apt-get dist-upgrade -y"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo add-apt-repository -y ppa:ubuntu-desktop/ubuntu-make"

    cmdArrLineNum = cmdArrLineNum + 1  ##  81
    cmdArray[( 0, cmdArrLineNum )] = "umake-ide-idea"
    cmdArray[( 1, cmdArrLineNum )] = "umake ide idea"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "



    ##########################################################
    # beginning of R install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  82
    cmdArray[( 0, cmdArrLineNum )] = "R-repo-add"
    cmdArray[( 1, cmdArrLineNum )] = "sudo echo 'deb http://cran.rstudio.com/bin/linux/ubuntu xenial/' | sudo tee -a /etc/apt/sources.list"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  83
    cmdArray[( 0, cmdArrLineNum )] = "R-keyring-add-pt1"
    cmdArray[( 1, cmdArrLineNum )] = "gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  84
    cmdArray[( 0, cmdArrLineNum )] = "R-keyring-add-pt2"
    cmdArray[( 1, cmdArrLineNum )] = "gpg -a --export E084DAB9 | sudo apt-key add -"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  85
    cmdArray[( 0, cmdArrLineNum )] = "R-apt-get-rbase"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install r-base r-base-dev"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo apt-get update"

    cmdArrLineNum = cmdArrLineNum + 1  ##  86
    cmdArray[( 0, cmdArrLineNum )] = "R-apt-get-rstudio"
    cmdArray[( 1, cmdArrLineNum )] = ""
    cmdArray[( 2, cmdArrLineNum )] = '("Hand download and Ubu install")'
    cmdArray[( 3, cmdArrLineNum )] = ""

    # end of R install mess
    ##########################################################


    ##########################################################
    # beginning of Docker install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  87
    cmdArray[( 0, cmdArrLineNum )] = "Docker-add-utils-for-apt-over-https"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install apt-transport-https ca-certificates curl software-properties-common"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  88
    cmdArray[( 0, cmdArrLineNum )] = "Docker-add-gpg-key"
    cmdArray[( 1, cmdArrLineNum )] = "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  89
    cmdArray[( 0, cmdArrLineNum )] = "Docker-choose-stable-repo"
    cmdArray[( 1, cmdArrLineNum )] = "sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' "   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  90
    cmdArray[( 0, cmdArrLineNum )] = "Docker-apt-get-install"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install docker-ce"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo apt-get update"

    cmdArrLineNum = cmdArrLineNum + 1  ##  91
    cmdArray[( 0, cmdArrLineNum )] = "Docker-test-start"
    cmdArray[( 1, cmdArrLineNum )] = "docker run -it ubuntu bash"
    cmdArray[( 2, cmdArrLineNum )] = '("")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo docker run hello-world"

    # end of Docker install mess
    ##########################################################


    ##########################################################
    # beginning of Filezilla install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  92
    cmdArray[( 0, cmdArrLineNum )] = "Filezilla-choose-stable-repo"
    # cmdArray[(cmdArrLineNum, 1)] = 'sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu xenial-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'"   
    cmdArray[( 1, cmdArrLineNum )] =   'sudo sh -c ' + 'echo "deb http://archive.getdeb.net/ubuntu xenial-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'   
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  93
    cmdArray[( 0, cmdArrLineNum )] = "Filezilla-add-gpg-key"
    cmdArray[( 1, cmdArrLineNum )] = "wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -"   #
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  94
    cmdArray[( 0, cmdArrLineNum )] = "Filezilla-apt-get-install"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install filezilla"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo apt-get update"

    # end of Filezilla install mess
    ##########################################################


    ##########################################################
    # beginning of sublimetext install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  95
    cmdArray[( 0, cmdArrLineNum )] = "sublimetext-choose-stable-repo"
    # cmdArray[(cmdArrLineNum, 1)] = "sudo sh -c 'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list'" 
                                   # echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    cmdArray[( 1, cmdArrLineNum )] = 'sudo sh -c ' + 'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list' 
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  96
    cmdArray[( 0, cmdArrLineNum )] = "sublimetext-add-gpg-key"
    cmdArray[( 1, cmdArrLineNum )] = "wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -"   
                              #     wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  97
    cmdArray[( 0, cmdArrLineNum )] = "sublimetext-apt-get-install"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install sublime-text"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo apt-get update"

    # end of sublimetext install mess
    ##########################################################

    ##########################################################
    # beginning of postgresql install mess    https://tecadmin.net/install-postgresql-server-on-ubuntu/#
    # https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
    cmdArrLineNum = cmdArrLineNum + 1  ##  98
    cmdArray[( 0, cmdArrLineNum )] = "postgresql-choose-stable-repo"
    # cmdArray[(cmdArrLineNum, 1)] = "sudo sh -c 'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list'" 
                                   # echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    # vvv  value has syntax error  vvv 
    cmdArray[( 1, cmdArrLineNum )] = " " # sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'" 
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  99
    cmdArray[( 0, cmdArrLineNum )] = "postgresql-add-gpg-key"
    cmdArray[( 1, cmdArrLineNum )] = "wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -"   
                              #     wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    cmdArray[( 2, cmdArrLineNum )] = '("UbuSingleLineSimple",)'
    cmdArray[( 3, cmdArrLineNum )] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 100
    cmdArray[( 0, cmdArrLineNum )] = "postgresql-apt-get-install"
    cmdArray[( 1, cmdArrLineNum )] = "sudo apt-get install postgresql postgresql-contrib"
    cmdArray[( 2, cmdArrLineNum )] = '("UbuComplex", "NeedsPpa", "NoKey")'
    cmdArray[( 3, cmdArrLineNum )] = "sudo apt-get update"

    # end of postgresql install mess
    ##########################################################

    
    return cmdArray

# sudo apt-get install libncurses5-dev libncursesw5-dev ncurses-doc

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj     the end of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the start of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# runs in bash a command line, here usually apt-get
def aptGetShellBash(cmdLine):
    import subprocess
    # cmdLine = "echo " + userPassWd + " | " + cmdArray[(0, 1)]
    # print(cmdLine)
    print("# jcj-jcj-jcj- Function aptGetShellBash starting process of a single command.")
    out_bytes = subprocess.Popen(cmdLine, shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    # out_bytes = subprocess.Popen(cmdLine , shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # echo "yourpassword" | sudo -S apt-get autoremove
    # proc = subprocess.Popen('apt-get install -y filetoinstall', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    out_bytes.wait()
    print(("# jcj-jcj-jcj- Function aptGetShellBash ending process of a single command," + " returned: ", out_bytes))
    # print(" ")

    # print("Function aptGetShellBash: ", out_bytes)
    return out_bytes

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr    jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# repeats the aptGetShellBash() function for the size of the array cmdLine
def repeatAptGetShellBash(userPassWd, cmdArray):
    print(" ")
    print("# jcj-jcj-jcj- begining process repeatAptGetShellBash - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    print(" ")
    numCols = len(cmdArray)
    print(("numCols is: ", numCols))
    numRows = list(map(len, cmdArray))
    # numRows = int(numRows)
    print(("numRows is: ", numRows))
    # for n_n in range ( 1, numRows):
    n_n = 1
    for row in cmdArray:
        print(("n_n is: ", n_n))
        print(("# jcj-jcj-jcj- Function repeatAptGetShellBash running this single command: " + cmdArray[(n_n, 1)]))
        cmdLine = "echo " + userPassWd + " | " + cmdArray[(n_n, 1)]

        if "UbuSingleLineSimple" in cmdArray[(n_n, 2)] :    ##// cmdArray[(n_n, 2)] == "UbuSingleLineSimple":
            out_bytes = aptGetShellBash(cmdLine)
        else:
            print("# jcj-jcj-jcj- not an UbuSingleLineSimple")

        out_bytes.wait()
        print(("# jcj-jcj-jcj- Function repeatAptGetShellBash ending process of single command: " + cmdArray[(n_n, 1)] + " , returned: ", out_bytes))
        print(" ")
        n_n = n_n + 1
        if cmdArray[(n_n, 1)] == " ":
            break
        elif cmdArray[(n_n, 1)] == "":
            break

    print(" ")
    print("# jcj-jcj-jcj- ending process repeatAptGetShellBash - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    print(" ")
    return out_bytes
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# start of createNewPostgresDbTable
def createNewPostgresDbTable(cmdArray):

    ## cmdArray = genCmdArraySample( 5, 30 )
    ## print("Function genCmdArraySample: ", cmdArray)

   print()
   # return  ## cmdArray 
# end of createNewPostgresDbTable
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# start of writeRecordToPostgresDbTable
def writeRecordToPostgresDbTable( db_connect_str, sql_table_name_str, dict_of_records_to_write ):

    db_connect_str = "dbname='reappanemptyubu' user='jcj52436999' host='localhost' password='STL2lmnm'"
    
    sql_table_name_str = "ubu_install_commands_2"  # 
    # sql_table_name_str = "tutorials"
    sql_table_create_columns_str = " (dbXcoord char(40), dbYcoord char(40), dbCellContent char(40))"


    # sql_table_create_str = """CREATE TABLE IF NOT EXISTS tutorials (first_name char(40), last_name char(40))"""
    sql_table_create_str = "CREATE TABLE IF NOT EXISTS "
    sql_table_create_str += sql_table_name_str
    sql_table_create_str += sql_table_create_columns_str

    dict_of_records_to_write = (
        {"dbXcoord":"Joshua", "dbYcoord":"Drake", "dbCellContent":"Drakiie"},
        {"dbXcoord":"Steven", "dbYcoord":"Foo", "dbCellContent":"Drake"},
        {"dbXcoord":"David", "dbYcoord":"Bar", "dbCellContent":"Drakie"})

    sql_insert_columns_str = " ( dbXcoord, dbYcoord, dbCellContent )" 
    sql_insert_values = "%"+"(dbXcoord)s, "+"%"+"(dbYcoord)s, "+"%"+"(dbCellContent)s" 

    sql_insert_execute_many_str = "INSERT INTO " 
    sql_insert_execute_many_str += sql_table_name_str 
    sql_insert_execute_many_str += sql_insert_columns_str 
    sql_insert_execute_many_str += " VALUES ( " + sql_insert_values + " ) "
    # sql_insert_execute_many_str += dict_of_records_to_write
    # namedict 

    # try to connect
    try:
    # use our connection values to establish a connection
        conn = psycopg2.connect(db_connect_str)
        print((">>>*** Connection made as " + db_connect_str))
    except Exception as e:
        print(">>>*** ReAppAnEmptyUbu is UNABLE TO CONNECT TO THE DATABASE. Invalid dbname, user or password?")
        print(e)
        return e  

    # try to write records
    try:
        # create a psycopg2 cursor that can execute queries
        cursr = conn.cursor()
        # create a new table IF NOT EXISTS  
        cursr.execute( sql_table_create_str )
        # executemany to write dict of records into table
        cursr.executemany(sql_insert_execute_many_str, dict_of_records_to_write)  #namedict
        # cursr.executemany("""INSERT INTO tutorials (first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)

        # run a SELECT statement to print out result  
        cursr.execute( "SELECT * from " + sql_table_name_str )  # ("""SELECT * from tutorials""")
        rows = cursr.fetchall()
        print(rows) 
        conn.commit()
        cursr.close()
        conn.close()
    except Exception as e:
        print(">>>*** Uh oh, can't write. Invalid dbname, user or password?")
        print(e)
        return e 
  
    return " "
# end of writeRecordToPostgresDbTable
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# start of readRecordFromPostgresDbTable
def readRecordFromPostgresDbTable():

# try to connect
    connect_str = "dbname='reappanemptyubu' user='jcj52436999' host='localhost' " + "password='STL2lmnm'"
    try:
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        print((">>>*** Connection made as " + connect_str))

    except Exception as e:
        print(">>>*** ReAppAnEmptyUbu is UNABLE TO CONNECT TO THE DATABASE. Invalid dbname, user or password?")
        print(e)
    try:
        # create a psycopg2 cursor that can execute queries
        cursr = conn.cursor()
        # create a new table with a single column called "name"
        # cursor.execute("""CREATE TABLE tutorials (name char(40));""")
        # run a SELECT statement - no data in there, but we can try it
        cursr.execute("""SELECT * FROM tutorials""")
        rows = cursr.fetchall()
        print(rows)
    except Exception as e:
        print(">>>*** Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    return " "
# end of readRecordFromPostgresDbTable
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# start of writeSmplRecordToPostgresDbTable
def writeSmplRecordToPostgresDbTable():

# try to connect
    connect_str = "dbname='reappanemptyubu' user='jcj52436999' host='localhost' " + "password='STL2lmnm'"

    try:
    # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        print((">>>*** Connection made as " + connect_str))        

    except Exception as e:
        print(">>>*** ReAppAnEmptyUbu is UNABLE TO CONNECT TO THE DATABASE. Invalid dbname, user or password?")
        print(e)

    namedict = ({"first_name":"Joshua", "last_name":"Drake"},
            {"first_name":"Steven", "last_name":"Foo"},
            {"first_name":"David", "last_name":"Bar"})

    try:
        # create a psycopg2 cursor that can execute queries
        cursr = conn.cursor()
        # create a new table with a column called "name" IF NOT EXISTS  
        cursr.execute("""CREATE TABLE IF NOT EXISTS tutorials (first_name char(40), last_name char(40))""")
        cursr.executemany("""INSERT INTO tutorials (first_name,last_name) VALUES (%(first_name)s, %(last_name)s)""", namedict)
        # run a SELECT statement   
        cursr.execute("""SELECT * from tutorials""")
        rows = cursr.fetchall()
        print(rows) 
        conn.commit()
        cursr.close()
        conn.close()
        print((">>>*** Table record made as " + connect_str))

    except Exception as e:
        print(">>>*** Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

    return " "
# end of writeSmplRecordToPostgresDbTable
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# start of readSmplRecordFromPostgresDbTable
def readSmplRecordFromPostgresDbTable():

# try to connect
    connect_str = "dbname='reappanemptyubu' user='jcj52436999' host='localhost' " + "password='STL2lmnm'"
    try:
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        print((">>>*** Connection made as " + connect_str))
        
    except Exception as e:
        print(">>>*** ReAppAnEmptyUbu is UNABLE TO CONNECT TO THE DATABASE. Invalid dbname, user or password?")
        print(e)
    try:
        # create a psycopg2 cursor that can execute queries
        cursr = conn.cursor()
        # create a new table with a single column called "name"
        # cursor.execute("""CREATE TABLE tutorials (name char(40));""")
        # run a SELECT statement - no data in there, but we can try it
        cursr.execute("""SELECT * FROM tutorials""")
        rows = cursr.fetchall()
        print(rows)
    except Exception as e:
        print(">>>*** Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
    return " "
# end of readSmplRecordFromPostgresDbTable
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the end of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj    the start of sr  jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of sysExiter()   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def sysExiter():
    sys.exit()
  
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of sysExiter()   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
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

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of menuInit   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def menuInit(cmdArray):

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
        ''' 
        def inputIntegerOnly( promptString ): 
            while True:
                inputted = input( promptString )
                if inputted == "stop":
                print( "Stop chosen. ") 
                break
            elif not inputted.isdigit():
                print( "Must be a number! ")
            else: 
                inputted = int(inputted)
                return inputted
        ''' 
 
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
    if argv is None:
        argv = sys.argv

    print(" ")
    print("# jcj-jcj-jcj- START OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    thisProgramIs = "reAppAnEmptyUbu.py"
    print(("Start of program " + thisProgramIs))
    print(" ")

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

    '''
    Trying to install a favorite set of Ubu software.
    '''
    
    w = 5
    h = 99
    cmdArrayWidth = w
    cmdArrayHeight = h 
    cmdArray = {( w, h): " " for w in range(cmdArrayWidth) for h in range(cmdArrayHeight)}

    menuInit( cmdArray )

    # out_bytes.wait() 
    out_bytes = " " 
    print(("# jcj-jcj-jcj- Function Main is ending with sys.exit(): ", out_bytes))

    print(" ")
    print("# jcj-jcj-jcj- END OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    print(" ")
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of main   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
if __name__ == "__main__":
    sys.exit(main())

