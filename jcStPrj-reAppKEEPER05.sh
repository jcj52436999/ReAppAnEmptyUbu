#!bin/bash
# -*- coding: utf-8 -*-
# jcStPrj-reApp.sh

RRES_X=0
RRES_Y=0
RRESCHAR_X=0
RRESCHAR_Y=0

read RRES_X RRES_Y <<<$(xdpyinfo | awk -F'[ x]+' '/dimensions:/{print $3, $4}') 
echo $RRES_X, $RRES_Y 
# echo $RRES_X, $RRES_Y 
# let RRES_X=$RRES_X 
# let RRES_Y=$RRES_Y 
let RRESCHAR_X=$RRES_X/10
let RRESCHAR_Y=$RRES_Y/7
echo $RRES_X, $RRES_Y 

function splashUp {
    local RES_X
    local RES_Y
    local RESCHAR_X
    local RESCHAR_Y
    local FRM_WDTH
    local FRM_HGTH
    local FRM_X
    local FRM_Y
    local TOEXEC
    local windSzXFRAC
    local windSzYFRAC
    local windPosXFRAC
    local windPosYFRAC
    local appToSplash # ="konsole" 
    local workDir 
    local screenDimUnits # = "pixels"
    local frameDimUnits
    
    RES_X=$RRES_X
    RES_Y=$RRES_Y
    RESCHAR_X=$RRESCHAR_X
    RESCHAR_Y=$RRESCHAR_Y
    windSzXFRAC=$1  # $wwindSzXFRAC
    windSzYFRAC=$2  # $wwindSzYFRAC
    windPosXFRAC=$3  # $wwindPosXFRAC
    windPosYFRAC=$4  # $wwindPosYFRAC
    appToSplash=$5  # $aappToSplash 
    workDir=$wworkDir 
    screenDimUnits=$sscreenDimUnits   #$7
    frameDimUnits=$fframeDimUnits    #"chars"
    # frameDimUnits=$8
    
    echo "Variable workDir = " $workDir 
    echo ", variable frameDimUnits = " $frameDimUnits " " 
    echo " " 
    
    if [[ -z $workDir ]]; then  
        workDir=""
    else    
        workDir="--workdir $workDir"         #wworkDir 
    fi 


    if [[ "$frameDimUnits" == "pixels" ]]; then  
        RESframe_X=$RRES_X
        RESframe_Y=$RRES_Y     #wworkDir 
    else 
        RESframe_X=$RRESCHAR_X    # workDir="--workdir $workDir" 
        RESframe_Y=$RRESCHAR_Y 
    fi 
    

    if [[ "$screenDimUnits" == "pixels" ]]; then  
        RESposition_X=$RRES_X
        RESposition_Y=$RRES_Y     #wworkDir 
    else 
        RESposition_X=$RRESCHAR_X    # workDir="--workdir $workDir" 
        RESposition_Y=$RRESCHAR_Y 
    fi 
     
    # konsole --workdir ~ --p TerminalRows=100 --p TerminalColumns=100 --geometry 50x60&
    
    let FRM_WDTH=$RESframe_X*$windSzXFRAC/100
    let FRM_HGTH=$RESframe_Y*$windSzYFRAC/100
    let FRM_X=$RESposition_X*$windPosXFRAC/100
    let FRM_Y=$RESposition_Y*$windPosYFRAC/100
    echo $FRM_WDTH $FRM_HGTH $FRM_X $FRM_Y 
    # nohup konsole --geometry $FRM_HGTH x $FRM_WDTH + $FRM_X - $FRM_Y & 
    # nohup konsole --geometry $FRM_HGTH x $FRM_WDTH + $FRM_X - $FRM_Y & 
    # echo nohup gnome-terminal --geometry $FRM_WDTH+$FRM_HGTH+$FRM_X+$FRM_Y & 
    # nohup gnome-terminal --geometry $FRM_WDTH+$FRM_HGTH+$FRM_X+$FRM_Y & 
    
    # TOEXEC="nohup gnome-terminal --geometry $FRM_WDTH+$FRM_HGTH+$FRM_X+$FRM_Y & "
    #TOEXEC="nohup konsole --p TerminalRows=20 --p TerminalColumns=80 --geometry $FRM_WDTH + $FRM_HGTH & " 
    # appToSplash
    # TOEXEC="nohup konsole --workdir ~ --geometry $FRM_WDTH x $FRM_HGTH + $FRM_X - $FRM_Y & "
    # TOEXEC="nohup $appToSplash --workdir $workDir --geometry ${FRM_WDTH}x$FRM_HGTH+$FRM_X-$FRM_Y & "
    TOEXEC="nohup $appToSplash $workDir --geometry ${FRM_WDTH}x$FRM_HGTH+$FRM_X-$FRM_Y & "
    cd ~/
    echo $TOEXEC
    echo "#!/usr/bin/env bash" > ~/my_Script.sh
    echo "# -*- coding: utf-8 -*-" >> ~/my_Script.sh 
    echo "# " >> ~/my_Script.sh 
    
    echo $TOEXEC >> ~/my_Script.sh
    
    sleep 5s
    # chmod a+x /home/jcjk52436999/my_Script.sh
    chmod +x ~/my_Script.sh
    
    sleep 5s
    # bash nohup ~/my_Script.sh &
    bash ~/my_Script.sh    #&
    
    
    
    return
} 

# Making first function call to make a window.  
#RRES_X
#RRES_Y
# wworkDir="~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu" 


fframeDimUnits="chars"
sscreenDimUnits="chars"
wworkDir="" 
wwindSzXFRAC=20
wwindSzYFRAC=10
wwindPosXFRAC=30
wwindPosYFRAC=10
# aappToSplash="konsole" 
aappToSplash="firefox" 
# nohup firefox --geometry 700x1200+600-800 &
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
sleep 5s
echo "Just ran the firefox exoScript."


# nohup krusader --geometry 1500x600+10-900 &
fframeDimUnits="chars"
sscreenDimUnits="pixels"
wworkDir="" 
wwindSzXFRAC=20
wwindSzYFRAC=15
wwindPosXFRAC=10
wwindPosYFRAC=80
# aappToSplash="konsole" 
aappToSplash="krusader" 
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
sleep 5s
echo "Just ran the Krusader exoScript."


#nohup kate --geometry 500x700+700-900 &
fframeDimUnits="chars"
sscreenDimUnits="pixels"
wworkDir="" 
wwindSzXFRAC=20
wwindSzYFRAC=15
wwindPosXFRAC=10
wwindPosYFRAC=80
# aappToSplash="konsole" 
aappToSplash="kate" 
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
sleep 5s
echo "Just ran the Kate exoScript."


# nohup kdevelop --geometry 500x700+500-900 &
fframeDimUnits="pixels"
sscreenDimUnits="pixels"
wworkDir="" 
wwindSzXFRAC=50
wwindSzYFRAC=50
wwindPosXFRAC=25
wwindPosYFRAC=25
# aappToSplash="konsole" 
aappToSplash="kdevelop" 
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
sleep 5s
echo "Just ran the Kdevelop exoScript."


# nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
#nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
fframeDimUnits="pixels"
sscreenDimUnits="pixels"
wworkDir="~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu" 
wwindSzXFRAC=65
wwindSzYFRAC=2
wwindPosXFRAC=18
wwindPosYFRAC=40
# aappToSplash="konsole" 
aappToSplash="konsole" 
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
sleep 5s
echo "Just ran a Konsole exoScript."


# nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
#nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
fframeDimUnits="pixels"
sscreenDimUnits="pixels"
wworkDir="~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu" 
wwindSzXFRAC=70
wwindSzYFRAC=5
wwindPosXFRAC=20
wwindPosYFRAC=40
# aappToSplash="konsole" 
aappToSplash="konsole" 
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
sleep 5s
echo "Just ran a Konsole exoScript."


# nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
#nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
fframeDimUnits="pixels"
sscreenDimUnits="pixels"
wworkDir="~" 
wwindSzXFRAC=70
wwindSzYFRAC=75
wwindPosXFRAC=10
wwindPosYFRAC=10
# aappToSplash="konsole" 
aappToSplash="konsole" 
splashUp $wwindSzXFRAC $wwindPosYFRAC $wwindPosXFRAC $wwindPosYFRAC $aappToSplash $wworkDir $fframeDimUnits 
# $sscreenDimUnits
# sleep 5s
echo "Just ran a Konsole exoScript."





exit

# konsole --workdir ~ --p TerminalRows=100 --p TerminalColumns=100 --geometry 50x60&
# konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --geometry 1500x400 "source jc-env/bin/activate" &
nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --geometry 1100x200+800-600 &
# konsole --workdir ~ --geometry 800x200+1100-50 -e ls &
# nohup source jc-env/bin/activate &
# konsole --workdir ~ --geometry 800x200+1100-50 --noclose -e ls
nohup konsole --workdir ~ --geometry 800x200+1100-50 &
# konsole --workdir ~ --geometry 800x200+400-50 --noclose --hold -e ls &
# nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --geometry 800x200+400-50 --noclose -e konsole ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu/jc-env/bin/activate &
#konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --geometry 800x200+400-50 --e="bash -c '~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu/jc-env/bin/activate; $SHELL'" &
konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --geometry 800x200+400-50 --e="bash -c '~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu/jc-env/bin/activate'" &


echo "Done with it."

ls



