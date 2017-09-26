#  reAppAnEmptyUbu.py
'''

.
.


'''

import sys
import pickle
import json
import sqlite3
import psycopg2
import django

def genaFile_cmdArrValsDotCsv():

    cmdArray = genCmdArraySample()
    print("Function genCmdArraySample: ", cmdArray)

    cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 55, 1):

        for column in range(0, 4, 1):
            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            strOut = "    cmdArray[(" + str(row) + ", " + str(column) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print("    To" + strOut)
            cmdArrValDotTxt.write(strOut + '\n')

        print()
        cmdArrValDotTxt.write('\n')


    cmdArrValDotTxt.close()
    print()
    return


def genaFile_cmdArrHeadersAndValsIntoListOfDicts():

    cmdArray = genCmdArraySample()
    print("Function genCmdArraySample: ", cmdArray)

    cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 55, 1):

        for column in range(0, 4, 1):
            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            strOut = "    cmdArray[(" + str(row) + ", " + str(column) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print("    To" + strOut)
            cmdArrValDotTxt.write(strOut + '\n')

        print()
        cmdArrValDotTxt.write('\n')


    cmdArrValDotTxt.close()
    print()
    return


def genaFile_cmdArrValsDotTxt():  # Gens txt file with some reversals

    cmdArray = genCmdArraySample()
    print("Function genCmdArraySample: ", cmdArray)

    cmdArrValDotTxt = open('cmdArrVals.txt', 'w')
    print()
    for  row in range(0, 55, 1):

        for column in range(0, 4, 1):
            strOut = "cmdArray[(" + str(column) + ", " + str(row) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print( strOut )
            strOut = "    cmdArray[(" + str(row) + ", " + str(column) + ")] = " + '"' + cmdArray[(column, row)] + '"'
            print("    To" + strOut)
            cmdArrValDotTxt.write(strOut + '\n')

        print()
        cmdArrValDotTxt.write('\n')


    cmdArrValDotTxt.close()
    print()
    return


# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the start of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# Generates as a dev default an array of apt-get command lines
def genCmdArraySample():
    w = 5
    h = 60
    width = w
    height = h
    cmdArray = {(w, h): " " for w in range(width) for h in range(height)}
    cmdArrLineNum = 0

    # y is record number
    # x is item in record
    # x is 0 for a unique name for the desired command line
    # x is 1 for the command line itself
    # x is 2 for a list of strings as properties of the command
    # x is 3 for archive ppa if needed
    # x is 4 for archive key if needed

    # array db headers
    cmdArray[(0, 0)] = "unique-name"
    cmdArray[(0, 1)] = "command"
    cmdArray[(0, 2)] = "cmd-properties"
    cmdArray[(0, 3)] = "ppa"

    cmdArray[(1, 0)] = "apt-get-update"
    cmdArray[(1, 1)] = "sudo -S apt-get update"
    cmdArray[(1, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(1, 3)] = " "

    cmdArray[(2, 0)] = "apt-get-upgrade"
    cmdArray[(2, 1)] = "sudo -S apt-get upgrade -y"
    cmdArray[(2, 2)] = ("UbuSingleLineSimple",)  # ("UbuComplex", "GeneratesRebootReq")
    cmdArray[(2, 3)] = " "

    cmdArray[(3, 0)] = "apt-get-autoremove"
    cmdArray[(3, 1)] = "sudo -S apt-get autoremove -y"
    cmdArray[(3, 2)] = "UbuSingleLineSimple"
    cmdArray[(3, 3)] = " "

    cmdArray[(4, 0)] = "apt-get-autoclean"
    cmdArray[(4, 1)] = "sudo -S apt-get autoclean -y"
    cmdArray[(4, 2)] = "UbuSingleLineSimple"
    cmdArray[(4, 3)] = " "

    cmdArray[(5, 0)] = "apt-get-install-git"
    cmdArray[(5, 1)] = "sudo -S apt-get install -y git"
    cmdArray[(5, 2)] = "UbuSingleLineSimple"
    cmdArray[(5, 3)] = " "

    cmdArray[(6, 0)] = "apt-get-install-ojava7-installer"
    cmdArray[(6, 1)] = "sudo -S apt-get install -y oracle-java7-installer"
    cmdArray[(6, 2)] = ("UbuComplex", "InstOfInstaller", "NeedsPpa", "NoKey")
    cmdArray[(6, 3)] = "sudo add-apt-repository ppa:webupd8team/java"

    cmdArray[(7, 0)] = "apt-get-install-ojava8-installer"
    cmdArray[(7, 1)] = "sudo -S apt-get install -y oracle-java8-installer"
    cmdArray[(7, 2)] = ("UbuComplex", "InstOfInstaller", "NeedsPpa", "NoKey")
    cmdArray[(7, 3)] = "sudo add-apt-repository ppa:webupd8team/java"

    cmdArray[(8, 0)] = "apt-get-opera-stable"
    cmdArray[(8, 1)] = "sudo -S apt-get install -y opera-stable"
    cmdArray[(8, 2)] = ("UbuComplex", "InstOfInstaller", "NeedsPpa", "NeedsKey")
    cmdArray[(8, 3)] = "notSure"
    cmdArray[(8, 4)] = " "

    cmdArray[(9, 0)] = "apt-get-firefox"
    cmdArray[(9, 1)] = "sudo -S apt-get install -y firefox"
    cmdArray[(9, 2)] = "UbuSingleLineSimple"
    cmdArray[(9, 3)] = " "

    cmdArray[(10, 0)] = "apt-get-chrome"
    cmdArray[(10, 1)] = "sudo -S apt-get install -y google-chrome-stable"
    cmdArray[(10, 2)] = ("UbuComplex", "InstOfInstaller", "NeedsPpa", "NeedsKey")
    # cmdArray[(10, 3)] = "sudo sh -c 'echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list'"  
    cmdArray[(10, 3)] = "sudo sh -c 'echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list'"
    cmdArray[(10, 4)] = "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -"

    cmdArray[(11, 0)] = "apt-get-canary"
    cmdArray[(11, 1)] = "sudo -S apt-get install -y google-chrome-canary"
    cmdArray[(11, 2)] =  ("UbuComplex", "InstOfInstaller", "NeedsPpa", "NeedsKey")
    # cmdArray[(11, 3)] = "sudo sh -c 'echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list'"
    cmdArray[(11, 3)] = "sudo sh -c 'echo 'deb http://dl.google.com/linux/chrome/deb/ canary main' >> /etc/apt/sources.list.d/google.list'"
    cmdArray[(11, 4)] = "wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -"

    cmdArray[(12, 0)] = "apt-get-shutter"
    cmdArray[(12, 1)] = "sudo -S apt-get install -y shutter"
    cmdArray[(12, 2)] = "UbuSingleLineSimple"
    cmdArray[(12, 3)] = " "

    cmdArray[(13, 0)] = "apt-get-stellarium"
    cmdArray[(13, 1)] = "sudo -S apt-get install -y stellarium"
    cmdArray[(13, 2)] = "UbuSingleLineSimple"
    cmdArray[(13, 3)] = " "

    cmdArray[(14, 0)] = "apt-get-atom"
    cmdArray[(14, 1)] = "sudo -S apt-get install -y atom"
    cmdArray[(14, 2)] = "UbuComplex"
    cmdArray[(14, 3)] = " "

    cmdArray[(15, 0)] = "apt-get-idle3"
    cmdArray[(15, 1)] = "sudo -S apt-get install -y idle3"
    cmdArray[(15, 2)] = "UbuSingleLineSimple"
    cmdArray[(15, 3)] = " "

    cmdArray[(16, 0)] = "apt-get-gcommander"
    cmdArray[(16, 1)] = "sudo -S apt-get install -y gnome-commander"
    cmdArray[(16, 2)] = "UbuSingleLineSimple"
    cmdArray[(16, 3)] = " "

    cmdArray[(17, 0)] = "apt-get-python3-urwid"
    cmdArray[(17, 1)] = "sudo -S apt-get install -y python3-urwid"
    cmdArray[(17, 2)] = "UbuSingleLineSimple"
    cmdArray[(17, 3)] = " "

    cmdArray[(18, 0)] = "apt-get-ncurses"
    cmdArray[(18, 1)] = "sudo -S apt-get install -y libncurses5-dev libncursesw5-dev ncurses-doc"
    cmdArray[(18, 2)] = "UbuSingleLineSimple"
    cmdArray[(18, 3)] = " "

    cmdArray[(19, 0)] = "apt-get-telegram"
    cmdArray[(19, 1)] = "sudo -S apt-get install -y telegram"
    cmdArray[(19, 2)] = "UbuComplex"
    cmdArray[(19, 3)] = " "

    cmdArray[(20, 0)] = "apt-get-bpython3"
    cmdArray[(20, 1)] = "sudo -S apt-get install -y bpython3"
    cmdArray[(20, 2)] = "UbuSingleLineSimple"
    cmdArray[(20, 3)] = " "

    cmdArray[(21, 0)] = "apt-get-ipython3"
    cmdArray[(21, 1)] = "sudo -S apt-get install -y ipython3"
    cmdArray[(21, 2)] = "UbuSingleLineSimple"
    cmdArray[(21, 3)] = " "

    cmdArray[(22, 0)] = "apt-get-gimp"
    cmdArray[(22, 1)] = "sudo -S apt-get install -y gimp"
    cmdArray[(22, 2)] = "UbuSingleLineSimple"
    cmdArray[(22, 3)] = " "

    cmdArray[(23, 0)] = "apt-get-qrq"
    cmdArray[(23, 1)] = "sudo -S apt-get install -y qrq"
    cmdArray[(23, 2)] = "UbuSingleLineSimple"
    cmdArray[(23, 3)] = " "

    cmdArray[(24, 0)] = "apt-get-spyder3"
    cmdArray[(24, 1)] = "sudo -S apt-get install -y spyder3"
    cmdArray[(24, 2)] = "UbuSingleLineSimple"
    cmdArray[(24, 3)] = " "

    cmdArray[(25, 0)] = "apt-get-gperiodic"
    cmdArray[(25, 1)] = "sudo -S apt-get install -y gperiodic"
    cmdArray[(25, 2)] = "UbuSingleLineSimple"
    cmdArray[(25, 3)] = " "

    cmdArray[(26, 0)] = "apt-get-inkscape"
    cmdArray[(26, 1)] = "sudo -S apt-get install -y inkscape"
    cmdArray[(26, 2)] = "UbuSingleLineSimple"
    cmdArray[(26, 3)] = " "

    cmdArray[(27, 0)] = "apt-get-blender"
    cmdArray[(27, 1)] = "sudo -S apt-get install -y blender"
    cmdArray[(27, 2)] = "UbuSingleLineSimple"
    cmdArray[(27, 3)] = " "

    cmdArray[(28, 0)] = " "
    cmdArray[(28, 1)] = " "
    cmdArray[(28, 2)] = "UbuSingleLineSimple"
    cmdArray[(28, 3)] = " "

    cmdArray[(29, 0)] = "apt-get-slack"
    cmdArray[(29, 1)] = "sudo -S apt-get install -y slack"
    cmdArray[(29, 2)] = "UbuComplex"
    cmdArray[(29, 3)] = " "

    cmdArray[(30, 0)] = "apt-get-esl-erlang"
    cmdArray[(30, 1)] = "sudo -S apt-get install -y esl-erlang"
    cmdArray[(30, 2)] = ("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")
    cmdArray[(30, 3)] = "wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb"

    cmdArray[(31, 0)] = "apt-get-elixir"
    cmdArray[(31, 1)] = "sudo -S apt-get install -y elixir"
    cmdArray[(31, 2)] = ("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")
    cmdArray[(31, 3)] = "wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && sudo dpkg -i erlang-solutions_1.0_all.deb"

    cmdArray[(32, 0)] = "apt-get-gparted"
    cmdArray[(32, 1)] = "sudo -S apt-get install -y gparted"
    cmdArray[(32, 2)] = "UbuSingleLineSimple"
    cmdArray[(32, 3)] = " "

    cmdArray[(33, 0)] = "apt-get-zim"
    cmdArray[(33, 1)] = "sudo -S apt-get install -y zim"
    cmdArray[(33, 2)] = "UbuSingleLineSimple"
    cmdArray[(33, 3)] = " "

    cmdArray[(34, 0)] = "apt-get-gfortran"
    cmdArray[(34, 1)] = "sudo -S apt-get install -y gfortran"
    cmdArray[(34, 2)] = "UbuSingleLineSimple"
    cmdArray[(34, 3)] = " "

    cmdArray[(35, 0)] = "apt-get-gfortran-5"
    cmdArray[(35, 1)] = "sudo -S apt-get install -y gfortran-5"
    cmdArray[(35, 2)] = "UbuSingleLineSimple"
    cmdArray[(35, 3)] = "sudo apt-add-repository ppa:ubuntu-toolchain-r/test"

    cmdArray[(36, 0)] = "apt-get-gfortran-6"
    cmdArray[(36, 1)] = "sudo -S apt-get install -y gfortran-6"
    cmdArray[(36, 2)] = "UbuSingleLineSimple"
    cmdArray[(36, 3)] = "sudo apt-add-repository ppa:ubuntu-toolchain-r/test"

    cmdArray[(37, 0)] = "apt-get-postgresqlStuff"
    cmdArray[(37, 1)] = "sudo -S apt-get install -y postgresql libpq-dev postgresql-client postgresql-client-common"
    cmdArray[(37, 2)] = "UbuSingleLineSimple"
    cmdArray[(37, 3)] = " "

    cmdArray[(38, 0)] = "apt-get-pythonStuff"
    cmdArray[(38, 1)] = "sudo -S apt-get install -y virtualenv python-pip python3-dev"
    cmdArray[(38, 2)] = "UbuSingleLineSimple"
    cmdArray[(38, 3)] = " "

    cmdArray[(39, 0)] = "apt-get-natron"
    cmdArray[(39, 1)] = "sudo -S apt-get install -y virtualenv python-pip natron"
    cmdArray[(39, 2)] = ("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")
    cmdArray[(39, 3)] = " "

    cmdArray[(40, 0)] = "apt-get-lightworks"
    cmdArray[(40, 1)] = "sudo -S apt-get install -y virtualenv python-pip lightworks"
    cmdArray[(40, 2)] = ("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")
    cmdArray[(40, 3)] = " "

    cmdArray[(41, 0)] = "apt-get-xbase"
    cmdArray[(41, 1)] = "sudo -S apt-get install -y virtualenv python-pip xbase"
    cmdArray[(41, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(41, 3)] = " "

    cmdArray[(42, 0)] = "apt-get-clementine"
    cmdArray[(42, 1)] = "sudo -S apt-get install -y virtualenv python-pip clementine"
    cmdArray[(42, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(42, 3)] = " "

    cmdArray[(43, 0)] = "apt-get-rawtherapee"
    cmdArray[(43, 1)] = "sudo -S apt-get install -y virtualenv python-pip rawtherapee"
    cmdArray[(43, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(43, 3)] = " "

    cmdArray[(44, 0)] = "apt-get-bluefish"
    cmdArray[(44, 1)] = "sudo -S apt-get install -y virtualenv python-pip bluefish"
    cmdArray[(44, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(44, 3)] = " "

    cmdArray[(45, 0)] = "apt-get-openscad"
    cmdArray[(45, 1)] = "sudo -S apt-get install -y virtualenv python-pip openscad"
    cmdArray[(45, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(45, 3)] = " "

    cmdArray[(46, 0)] = "apt-get-openshot"
    cmdArray[(46, 1)] = "sudo -S apt-get install -y virtualenv python-pip openshot"
    cmdArray[(46, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(46, 3)] = " "

    cmdArray[(47, 0)] = "apt-get-openshot"
    cmdArray[(47, 1)] = "sudo -S apt-get install -y virtualenv python-pip josm"
    cmdArray[(47, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(47, 3)] = " "

    cmdArray[(48, 0)] = "apt-get-logism"
    cmdArray[(48, 1)] = "sudo -S apt-get install -y logism"
    cmdArray[(48, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(48, 3)] = " "

    cmdArray[(49, 0)] = "apt-get-spyder3"
    cmdArray[(49, 1)] = "sudo -S apt-get install -y spyder3"
    cmdArray[(49, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(49, 3)] = " "

#########################################################################

    cmdArray[(50, 0)] = "apt-get-dosbox"
    cmdArray[(50, 1)] = ""   # "dosbox"
    cmdArray[(50, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(50, 3)] = " "

    cmdArray[(51, 0)] = "apt-get-virtualbox"
    cmdArray[(51, 1)] = ""   # "virtualbox"
    cmdArray[(51, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(51, 3)] = " "

    cmdArray[(52, 0)] = "apt-get-maxima"
    cmdArray[(52, 1)] = ""   # "maxima"
    cmdArray[(52, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(52, 3)] = " "

    cmdArray[(53, 0)] = "apt-get-pymapper"
    cmdArray[(53, 1)] = ""   # "pymapper"
    cmdArray[(53, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(53, 3)] = " "

    cmdArray[(54, 0)] = "apt-get-winetricks"
    cmdArray[(54, 1)] = ""   # "winetricks"
    cmdArray[(54, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(54, 3)] = " "

    cmdArray[(55, 0)] = "apt-get-herculesstudio"
    cmdArray[(55, 1)] = ""   # "herculesstudio"
    cmdArray[(55, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(55, 3)] = " "

    cmdArray[(56, 0)] = "apt-get-veracrypt"
    cmdArray[(56, 1)] = " " 
    cmdArray[(56, 2)] = " "
    cmdArray[(56, 3)] = " "

    cmdArray[(57, 0)] = "apt-get-emacs25"
    cmdArray[(57, 1)] = "sudo apt-get install emacs25"
    cmdArray[(57, 2)] = ("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")
    cmdArray[(57, 3)] = "sudo apt-add-repository -y ppa:adrozdoff/emacs"

    cmdArray[(58, 0)] = "apt-get-zimdesktop"
    cmdArray[(58, 1)] = " "
    cmdArray[(58, 2)] = " "
    cmdArray[(58, 3)] = " "

    cmdArray[(59, 0)] = " "
    cmdArray[(59, 1)] = ""   # "lightworks"
    cmdArray[(59, 2)] = " "
    cmdArray[(59, 3)] = " "

    cmdArray[(60, 0)] = " "
    cmdArray[(60, 1)] = ""   # "natron"
    cmdArray[(60, 2)] = " "
    cmdArray[(60, 3)] = " "

    cmdArray[(61, 0)] = " "
    cmdArray[(61, 1)] = ""   # "rcmdr r rstudio"
    cmdArray[(61, 2)] = " "
    cmdArray[(61, 3)] = " "

    cmdArray[(62, 0)] = " "
    cmdArray[(62, 1)] = " "
    cmdArray[(62, 2)] = " "
    cmdArray[(62, 3)] = " "

    cmdArray[(63, 0)] = "apt-get-android-studio"
    cmdArray[(63, 1)] = " "
    cmdArray[(63, 2)] = " "
    cmdArray[(63, 3)] = " "

    cmdArray[(64, 0)] = "apt-get-gnome-commander"
    cmdArray[(64, 1)] = " "
    cmdArray[(64, 2)] = " "
    cmdArray[(64, 3)] = " "

    cmdArray[(65, 0)] = "apt-get-putty-ssh-client"
    cmdArray[(65, 1)] = " "
    cmdArray[(65, 2)] = " "
    cmdArray[(65, 3)] = " "

    cmdArray[(66, 0)] = "apt-get-telegram"
    cmdArray[(66, 1)] = " "
    cmdArray[(66, 2)] = " "
    cmdArray[(66, 3)] = " "

    cmdArray[(67, 0)] = "apt-get-slack"
    cmdArray[(67, 1)] = " "
    cmdArray[(67, 2)] = " "
    cmdArray[(67, 3)] = " "

    cmdArray[(68, 0)] = "apt-get-atom"
    cmdArray[(68, 1)] = " "
    cmdArray[(68, 2)] = " "
    cmdArray[(68, 3)] = " "

    cmdArray[(69, 0)] = "apt-get-oracle-virtualbox"
    cmdArray[(69, 1)] = " "
    cmdArray[(69, 2)] = " "
    cmdArray[(69, 3)] = " "

    cmdArrLineNum = 70   ##  70
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-clementine"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ## 71
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-JOSM"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  72
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-gnucash"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  73
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-scribus"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  74
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-zoom"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  75
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-xbase"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  76
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-rawtherapee"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  77
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-openscad"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  78
    cmdArray[(cmdArrLineNum, 0)] = "app-get-postgresforms"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  79
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-undetbootin"
    cmdArray[(cmdArrLineNum, 1)] = " "
    cmdArray[(cmdArrLineNum, 2)] = " "
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  80
    cmdArray[(cmdArrLineNum, 0)] = "apt-get-umake"
    cmdArray[(cmdArrLineNum, 1)] = "sudo apt-get install -y ubuntu-make && sudo apt-get update && sudo apt-get dist-upgrade -y"
    cmdArray[(cmdArrLineNum, 2)] = ("UbuComplex", "NotAnInstaller", "NeedsPpa", "NoKey")
    cmdArray[(cmdArrLineNum, 3)] = "sudo add-apt-repository -y ppa:ubuntu-desktop/ubuntu-make"

    cmdArrLineNum = cmdArrLineNum + 1  ##  81
    cmdArray[(cmdArrLineNum, 0)] = "umake-ide-idea"
    cmdArray[(cmdArrLineNum, 1)] = "umake ide idea"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "



    ##########################################################
    # beginning of R install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  82
    cmdArray[(cmdArrLineNum, 0)] = "R-repo-add"
    cmdArray[(cmdArrLineNum, 1)] = "sudo echo 'deb http://cran.rstudio.com/bin/linux/ubuntu xenial/' | sudo tee -a /etc/apt/sources.list"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  83
    cmdArray[(cmdArrLineNum, 0)] = "R-keyring-add-pt1"
    cmdArray[(cmdArrLineNum, 1)] = "gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  84
    cmdArray[(cmdArrLineNum, 0)] = "R-keyring-add-pt2"
    cmdArray[(cmdArrLineNum, 1)] = "gpg -a --export E084DAB9 | sudo apt-key add -"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  85
    cmdArray[(cmdArrLineNum, 0)] = "R-apt-get-rbase"
    cmdArray[(cmdArrLineNum, 1)] = "sudo apt-get install r-base r-base-dev"
    cmdArray[(cmdArrLineNum, 2)] = ("UbuComplex", "NeedsPpa", "NoKey")
    cmdArray[(cmdArrLineNum, 3)] = "sudo apt-get update"

    cmdArrLineNum = cmdArrLineNum + 1  ##  86
    cmdArray[(cmdArrLineNum, 0)] = "R-apt-get-rstudio"
    cmdArray[(cmdArrLineNum, 1)] = ""
    cmdArray[(cmdArrLineNum, 2)] = ("Hand download and Ubu install")
    cmdArray[(cmdArrLineNum, 3)] = ""

    # end of R install mess
    ##########################################################


    ##########################################################
    # beginning of Docker install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  87
    cmdArray[(cmdArrLineNum, 0)] = "Docker-add-utils-for-apt-over-https"
    cmdArray[(cmdArrLineNum, 1)] = "sudo apt-get install apt-transport-https ca-certificates curl software-properties-common"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  88
    cmdArray[(cmdArrLineNum, 0)] = "Docker-add-gpg-key"
    cmdArray[(cmdArrLineNum, 1)] = "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  89
    cmdArray[(cmdArrLineNum, 0)] = "Docker-choose-stable-repo"
    cmdArray[(cmdArrLineNum, 1)] = "sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' "   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  90
    cmdArray[(cmdArrLineNum, 0)] = "Docker-apt-get-install"
    cmdArray[(cmdArrLineNum, 1)] = "sudo apt-get install docker-ce"
    cmdArray[(cmdArrLineNum, 2)] = ("UbuComplex", "NeedsPpa", "NoKey")
    cmdArray[(cmdArrLineNum, 3)] = "sudo apt-get update"

    cmdArrLineNum = cmdArrLineNum + 1  ##  91
    cmdArray[(cmdArrLineNum, 0)] = "Docker-test-start"
    cmdArray[(cmdArrLineNum, 1)] = "docker run -it ubuntu bash"
    cmdArray[(cmdArrLineNum, 2)] = ("")
    cmdArray[(cmdArrLineNum, 3)] = "sudo docker run hello-world"

    # end of Docker install mess
    ##########################################################


    ##########################################################
    # beginning of Filezilla install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  92
    cmdArray[(cmdArrLineNum, 0)] = "Filezilla-choose-stable-repo"
    # cmdArray[(cmdArrLineNum, 1)] = 'sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu xenial-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'"   
    cmdArray[(cmdArrLineNum, 1)] =   'sudo sh -c ' + 'echo "deb http://archive.getdeb.net/ubuntu xenial-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'   
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  93
    cmdArray[(cmdArrLineNum, 0)] = "Filezilla-add-gpg-key"
    cmdArray[(cmdArrLineNum, 1)] = "wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -"   #
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  94
    cmdArray[(cmdArrLineNum, 0)] = "Filezilla-apt-get-install"
    cmdArray[(cmdArrLineNum, 1)] = "sudo apt-get install filezilla"
    cmdArray[(cmdArrLineNum, 2)] = ("UbuComplex", "NeedsPpa", "NoKey")
    cmdArray[(cmdArrLineNum, 3)] = "sudo apt-get update"

    # end of Filezilla install mess
    ##########################################################


    ##########################################################
    # beginning of sublimetext install mess

    cmdArrLineNum = cmdArrLineNum + 1  ##  95
    cmdArray[(cmdArrLineNum, 0)] = "sublimetext-choose-stable-repo"
    # cmdArray[(cmdArrLineNum, 1)] = "sudo sh -c 'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list'" 
                                   # echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    cmdArray[(cmdArrLineNum, 1)] = 'sudo sh -c ' + 'echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list' 
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  96
    cmdArray[(cmdArrLineNum, 0)] = "sublimetext-add-gpg-key"
    cmdArray[(cmdArrLineNum, 1)] = "wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -"   
                              #     wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    cmdArray[(cmdArrLineNum, 2)] = ("UbuSingleLineSimple",)
    cmdArray[(cmdArrLineNum, 3)] = " "

    cmdArrLineNum = cmdArrLineNum + 1  ##  97
    cmdArray[(cmdArrLineNum, 0)] = "sublimetext-apt-get-install"
    cmdArray[(cmdArrLineNum, 1)] = "sudo apt-get install sublime-text"
    cmdArray[(cmdArrLineNum, 2)] = ("UbuComplex", "NeedsPpa", "NoKey")
    cmdArray[(cmdArrLineNum, 3)] = "sudo apt-get update"

    # end of sublimetext install mess
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
    print("# jcj-jcj-jcj- Function aptGetShellBash ending process of a single command," + " returned: ", out_bytes)
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
    print("numCols is: ", numCols)
    numRows = map(len, cmdArray)
    # numRows = int(numRows)
    print("numRows is: ", numRows)
    # for n_n in range ( 1, numRows):
    n_n = 1
    for row in cmdArray:
        print("n_n is: ", n_n)
        print("# jcj-jcj-jcj- Function repeatAptGetShellBash running this single command: " + cmdArray[(n_n, 1)])
        cmdLine = "echo " + userPassWd + " | " + cmdArray[(n_n, 1)]

        if "UbuSingleLineSimple" in cmdArray[(n_n, 2)] :    ##// cmdArray[(n_n, 2)] == "UbuSingleLineSimple":
            out_bytes = aptGetShellBash(cmdLine)
        else:
            print("# jcj-jcj-jcj- not an UbuSingleLineSimple")

        out_bytes.wait()
        print("# jcj-jcj-jcj- Function repeatAptGetShellBash ending process of single command: " + cmdArray[(n_n, 1)] + " , returned: ", out_bytes)
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

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the start of sr   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
# provides a serial line by line terminal interface
def line_by_line_term_interface():

    import getpass
    import subprocess

    out_bytes = subprocess.check_output(['ls'])
    print(out_bytes)

    line_choice = 1
    print("")
    print("1. Choose 1 for use of upgrade commands from original default array.")
    print("2. Choose 2 for .")
    print("3. Choose 3 for .")
    print("4. Choose 4 for outputting default cmdArray list to csv file.")
    print("5. Choose 5 for gen a file cmdArrVals.txt.")
    line_choice = input("Which number do you want? ")
    line_choice = int(line_choice)

    if line_choice <= 1:
        cmdArray = genCmdArraySample()
        print("Function genCmdArraySample: ", cmdArray)
    elif line_choice <= 2:
        cmdArray = genCmdArraySample()
        print("Function genCmdArraySample: ", cmdArray)
    elif line_choice <= 3:
        cmdArray = genCmdArraySample()
        print("Function genCmdArraySample: ", cmdArray)
    elif line_choice <= 4:
        out_bytes = genaFile_cmdArrValsDotTxt()
        print( out_bytes )
        sys.exit(main())
    elif line_choice <= 5:
        out_bytes = genaFile_cmdArrValsDotTxt()
        print( out_bytes )
        sys.exit(main())
    else:
        cmdArray = genCmdArraySample()
        print("Function genCmdArraySample: ", cmdArray)


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

# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the Start of main   jcj-jcjjcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
def main(argv=None):
    if argv is None:
        argv = sys.argv

    print(" ")
    print("# jcj-jcj-jcj- START OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    thisProgramIs = "reAppAnEmptyUbu.py"
    print("Start of program " + thisProgramIs)
    print(" ")
    import curses
    import getpass
    import os
    import shutil
    import subprocess
    import pprint
    #  import pformat  
    from subprocess import Popen, PIPE, STDOUT

    # import urwid
    import numpy

    '''
    Trying to install a favorite set of Ubu software.
    '''

    line_choice = 3
    print("")
    print("1. Choose 1 for Cursed terminal interface.")
    print("2. Choose 2 for hand built terminal interface.")
    print("3. Choose 3 for line by line terminal interface.")
    print("4. Choose 4 for outputting default cmdArray list to csv file.")
    print("5. Choose 5 for gen a file cmdArrVals.txt.")
    print("6. Choose 6 to EXIT program.")
    line_choice = input("Which number do you want? ")
    line_choice = int(line_choice)

    if line_choice <= 1:
        out_bytes = line_by_line_term_interface()
    elif line_choice <= 2:
        out_bytes = line_by_line_term_interface()
    elif line_choice <= 3:
        out_bytes = line_by_line_term_interface()
    elif line_choice <= 4:
        out_bytes = genaFile_cmdArrValsDotTxt()
        print( out_bytes )
        sys.exit(main())
    elif line_choice <= 5:
        out_bytes = genaFile_cmdArrValsDotTxt()
        print( out_bytes )
        sys.exit(main())
    elif line_choice <= 6:
        out_bytes = "Exit program is chosen. sys.exit() "
        print(); print( out_bytes )
        sys.exit()
    else:
        out_bytes = "Entry is out of range." # line_by_line_term_interface()
        print(); print( out_bytes )
        sys.exit(main())

    # out_bytes.wait()
    print("# jcj-jcj-jcj- Function Main is ending with sys.exit(): ", out_bytes)

    print(" ")
    print("# jcj-jcj-jcj- END OF PROGRAM - jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj")
    print(" ")
# jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj   the End of main   jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj-jcj
if __name__ == "__main__":
    sys.exit(main())
