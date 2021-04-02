#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# mthdGenCmdArraySample.py as part of reAppAnEmptyUbu.py
# Created originally in 2018 as a simplistic exercise in broad-spectrum py use
# @author Joe Jackson 




def genCmdArraySample( cmdArrayWidth, cmdArrayHeight ):
    if (cmdArrayWidth < 1):
      w = 5; cmdArrayWidth = w

    if (cmdArrayHeight < 1):
      h = 99; cmdArrayHeight = h
    #'''  
    #w = 5
    #h = 99
    #cmdArrayWidth = w
    #cmdArrayHeight = h 
    #'''
    cmdArray = {( w, h): " " for w in range(cmdArrayWidth) for h in range(cmdArrayHeight)}
    cmdArrLineNum = 0

    #'''
    #w = 5
    #h = 60
    #width = w
    #height = h
    #cmdArray = {(w, h): " " for w in range(width) for h in range(height)}
    #'''

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

