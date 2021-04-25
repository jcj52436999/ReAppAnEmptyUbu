#!bin/bash
# konsole --workdir ~ --p TerminalRows=100 --p TerminalColumns=100 --geometry 50x60&
nohup firefox --geometry 700x1200+600-800 &
sleep 5s
nohup krusader --geometry 1500x600+10-900 &
sleep 5s
nohup kate --geometry 500x700+700-900 &
sleep 5s
nohup kdevelop --geometry 500x700+500-900 &
sleep 5s
nohup konsole --workdir ~/Dropbox/WkspcPythonSTANDALONES/ReAppAnEmptyUbu --geometry 1500x400 &
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



