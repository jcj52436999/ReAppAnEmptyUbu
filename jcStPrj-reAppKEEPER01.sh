#!bin/bash
# -*- coding: utf-8 -*-
# jcStPrj-reApp.sh

RRES_X=0
RRES_Y=0

read RRES_X RRES_Y <<<$(xdpyinfo | awk -F'[ x]+' '/dimensions:/{print $3, $4}') 
echo $RRES_X, $RRES_Y 


function splashUp {
    local RES_X
    local RES_Y
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
    
    RES_X=$RRES_X
    RES_Y=$RRES_Y
    windSzXFRAC=$wwindSzXFRAC
    windSzYFRAC=$wwindSzYFRAC
    windPosXFRAC=$wwindPosXFRAC
    windPosYFRAC=$wwindPosYFRAC
    appToSplash=$aappToSplash 
    
    # konsole --workdir ~ --p TerminalRows=100 --p TerminalColumns=100 --geometry 50x60&
    
    let FRM_WDTH=$RES_X*$windSzXFRAC/100
    let FRM_HGTH=$RES_Y*$windSzYFRAC/100
    let FRM_X=$RES_X*$windPosXFRAC/100
    let FRM_Y=$RES_Y*$windPosYFRAC/100
    echo $FRM_WDTH $FRM_HGTH $FRM_X "${FRM_Y}" 
    # nohup konsole --geometry $FRM_HGTH x $FRM_WDTH + $FRM_X - $FRM_Y & 
    # nohup konsole --geometry $FRM_HGTH x $FRM_WDTH + $FRM_X - $FRM_Y & 
    # echo nohup gnome-terminal --geometry $FRM_WDTH+$FRM_HGTH+$FRM_X+$FRM_Y & 
    # nohup gnome-terminal --geometry $FRM_WDTH+$FRM_HGTH+$FRM_X+$FRM_Y & 
    
    # TOEXEC="nohup gnome-terminal --geometry $FRM_WDTH+$FRM_HGTH+$FRM_X+$FRM_Y & "
    #TOEXEC="nohup konsole --p TerminalRows=20 --p TerminalColumns=80 --geometry $FRM_WDTH + $FRM_HGTH & " 
    # appToSplash
    # TOEXEC="nohup konsole --workdir ~ --geometry $FRM_WDTH x $FRM_HGTH + $FRM_X - $FRM_Y & "
    TOEXEC="nohup $appToSplash --workdir ~ --geometry $FRM_WDTH x $FRM_HGTH + $FRM_X - $FRM_Y & "
    cd ~/
    echo $TOEXEC
    echo "#!/usr/bin/env bash" > ~/my_Script.sh
    echo "# -*- coding: utf-8 -*-" > ~/my_Script.sh 
    echo "# " > ~/my_Script.sh 
    
    echo $TOEXEC >> ~/my_Script.sh
    
    sleep 5s
    # chmod a+x /home/jcjk52436999/my_Script.sh
    chmod +x ~/my_Script.sh
    
    sleep 5s
    # bash nohup ~/my_Script.sh &
    bash ~/my_Script.sh &
    
    
    return
} 

# Making first function call to make a window.  
#RRES_X
#RRES_Y
wwindSzXFRAC=80
wwindSzYFRAC=40
wwindPosXFRAC=50
wwindPosYFRAC=50
aappToSplash="konsole" 
splashUp
sleep 5s
echo "Just ran the first exoScript."

exit

# konsole --workdir ~ --p TerminalRows=100 --p TerminalColumns=100 --geometry 50x60&
nohup firefox --geometry 700x1200+600-800 &
sleep 5s
nohup krusader --geometry 1500x600+10-900 &
sleep 5s
nohup kate --geometry 500x700+700-900 &
sleep 5s
nohup kdevelop --geometry 500x700+500-900 &
sleep 5s
nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --command "source jc-env/bin/activate" --geometry 1500x400 &
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



