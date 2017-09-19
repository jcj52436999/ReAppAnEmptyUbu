#  reAppAnEmptyUbu-201606272311.py

import sys

def genCmdArraySample():
    w = 3
    h = 21
    width = w
    height = h
    cmdArray = {(w, h): 0 for w in range(width) for h in range(height)}

    cmdArray[(0, 1)] = "sudo -S apt-get update"
    print(cmdArray[(0, 0)])

    cmdArray[(0, 2)] = "sudo -S apt-get upgrade -y"

    cmdArray[(0, 3)] = "sudo -S apt-get autoremove -y"

    cmdArray[(0, 4)] = "sudo -S apt-get autoclean -y"

    cmdArray[(0, 5)] = "sudo -S apt-get install -y git"

    cmdArray[(0, 6)] = "sudo -S apt-get install -y oracle-java7-installer"
    cmdArray[(1, 6)] = "sudo add-apt-repository ppa:webupd8team/java"  # follow with apt-get update
    cmdArray[(2, 6)] = "wget -O - http://deb.opera.com/archive.key | sudo apt-key add -"

    cmdArray[(0, 7)] = "sudo -S apt-get install -y oracle-java8-installer"
    cmdArray[(1, 7)] = "sudo add-apt-repository ppa:webupd8team/java"  # follow with apt-get update
    cmdArray[(2, 7)] = "wget -O - http://deb.opera.com/archive.key | sudo apt-key add -"

    cmdArray[(0, 8)] = "sudo -S apt-get install -y python3-urwid"

    return cmdArray


def aptGetShellBash(cmdLine):
    import subprocess
      # cmdLine = "echo " + userPassWd + " | " + cmdArray[(0, 1)]
      # print(cmdLine)
    out_bytes = subprocess.Popen(cmdLine, shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    # out_bytes = subprocess.Popen(cmdLine , shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # echo "yourpassword" | sudo -S apt-get autoremove
    # proc = subprocess.Popen('apt-get install -y filetoinstall', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    out_bytes.wait()
    # print(out_bytes)
    return out_bytes

def main(argv=None):
    if argv is None:
        argv = sys.argv


    print("Start of program reAppEmptyUbu-201606261038.py")

    import curses
    import getpass
    import os
    import shutil
    import subprocess
    from subprocess import Popen, PIPE, STDOUT

    import urwid

    '''
    print("We are in a comment.")
    print("We are still in the same comment.")
    '''

    print("We are No Longer in that comment.")

    user = getpass.getuser()
    userPassWd = getpass.getpass()

    print(user)
    print(userPassWd)

    out_bytes = subprocess.check_output(['ls'])
    print(out_bytes)


###
    cmdArray = genCmdArraySample()
    print(cmdArray)

    # out_bytes = subprocess.check_output(['apt-get ', 'update', shell=True])
    # cmdLine = ['echo ' + userPassWd + ' | sudo -S apt-get update']
    # cmdLine = "sudo apt-get update"
    cmdLine = "echo " + userPassWd + " | " + cmdArray[(0, 1)]
    print(cmdLine)
      # out_bytes = subprocess.Popen(cmdLine, shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    # out_bytes = subprocess.Popen(cmdLine , shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # echo "yourpassword" | sudo -S apt-get autoremove
      # proc = subprocess.Popen('apt-get install -y filetoinstall', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    out_bytes = aptGetShellBash(cmdLine)

      # out_bytes.wait()
    print(out_bytes)

### the end of main ##################################################################################################
if __name__ == "__main__":
    sys.exit(main())
#  reAppAnEmptyUbu-201606272311.py

import sys

def genCmdArraySample():
    w = 3
    h = 21
    width = w
    height = h
    cmdArray = {(w, h): 0 for w in range(width) for h in range(height)}

    cmdArray[(0, 1)] = "sudo -S apt-get update"
    print(cmdArray[(0, 0)])

    cmdArray[(0, 2)] = "sudo -S apt-get upgrade -y"

    cmdArray[(0, 3)] = "sudo -S apt-get autoremove -y"

    cmdArray[(0, 4)] = "sudo -S apt-get autoclean -y"

    cmdArray[(0, 5)] = "sudo -S apt-get install -y git"

    cmdArray[(0, 6)] = "sudo -S apt-get install -y oracle-java7-installer"
    cmdArray[(1, 6)] = "sudo add-apt-repository ppa:webupd8team/java"  # follow with apt-get update
    cmdArray[(2, 6)] = "wget -O - http://deb.opera.com/archive.key | sudo apt-key add -"

    cmdArray[(0, 7)] = "sudo -S apt-get install -y oracle-java8-installer"
    cmdArray[(1, 7)] = "sudo add-apt-repository ppa:webupd8team/java"  # follow with apt-get update
    cmdArray[(2, 7)] = "wget -O - http://deb.opera.com/archive.key | sudo apt-key add -"

    cmdArray[(0, 8)] = "sudo -S apt-get install -y python3-urwid"

    return cmdArray


def aptGetShellBash(cmdLine):
    import subprocess
      # cmdLine = "echo " + userPassWd + " | " + cmdArray[(0, 1)]
      # print(cmdLine)
    out_bytes = subprocess.Popen(cmdLine, shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    # out_bytes = subprocess.Popen(cmdLine , shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # echo "yourpassword" | sudo -S apt-get autoremove
    # proc = subprocess.Popen('apt-get install -y filetoinstall', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    out_bytes.wait()
    # print(out_bytes)
    return out_bytes

def main(argv=None):
    if argv is None:
        argv = sys.argv


    print("Start of program reAppEmptyUbu-201606261038.py")

    import curses
    import getpass
    import os
    import shutil
    import subprocess
    from subprocess import Popen, PIPE, STDOUT

    import urwid

    '''
    print("We are in a comment.")
    print("We are still in the same comment.")
    '''

    print("We are No Longer in that comment.")

    user = getpass.getuser()
    userPassWd = getpass.getpass()

    print(user)
    print(userPassWd)

    out_bytes = subprocess.check_output(['ls'])
    print(out_bytes)


###
    cmdArray = genCmdArraySample()
    print(cmdArray)

    # out_bytes = subprocess.check_output(['apt-get ', 'update', shell=True])
    # cmdLine = ['echo ' + userPassWd + ' | sudo -S apt-get update']
    # cmdLine = "sudo apt-get update"
    cmdLine = "echo " + userPassWd + " | " + cmdArray[(0, 1)]
    print(cmdLine)
      # out_bytes = subprocess.Popen(cmdLine, shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    # out_bytes = subprocess.Popen(cmdLine , shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    # echo "yourpassword" | sudo -S apt-get autoremove
      # proc = subprocess.Popen('apt-get install -y filetoinstall', shell=True, stdin=None, stdout=open("/dev/null", "w"), stderr=None, executable="/bin/bash")
    out_bytes = aptGetShellBash(cmdLine)

      # out_bytes.wait()
    print(out_bytes)

### the end of main ##################################################################################################
if __name__ == "__main__":
    sys.exit(main())
