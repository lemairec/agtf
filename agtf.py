#!/usr/bin/env python

import sys, optparse, subprocess, urllib2, os, os.path, errno, zipfile, string, json, platform, shutil, tarfile, urlparse, tempfile, multiprocessing
from subprocess import Popen, PIPE
import argparse
import sys

from Tkinter import *
PATH = os.getcwd();

def callWithoutPrint(cmdline):
    ret = subprocess.call(cmdline, shell=True)
    if ret != 0:
        print >> sys.stderr, 'Running: ' + cmdline + ' failed with exit code ' + str(ret) + '!'
    return ret

def call(cmdline):
    print 'Running: ' + cmdline
    callWithoutPrint(cmdline)


def clickedGPS():
    call("~/agrigpspi/agrigpspi.py run")

def installGPS():
    print(PATH + "/agrigpspi")
    if os.path.exists(PATH + "/agrigpspi"):
        call("cd ~/agrigpspi; git reset --hard; git pull")
    else:
        call("git clone https://github.com/lemairec/agrigpspi.git ~/agrigpspi; ~/agrigpspi/agrigpspi.py install")

def nettoyageGPS():
    call("rm -rf ~/agrigpspi/build; mkdir ~/agrigpspi/build")

def update_setup():
   call("cd ~/agtf; git pull;")
   exit();

def clickedBineuse():
    call("~/bineuse/bineuse.py run")

def installBineuse():
    print(PATH + "/bineuse")
    if os.path.exists(PATH + "/bineuse"):
        call("cd ~/bineuse; git reset --hard; git pull")
    else:
        call("git clone git@github.com:lemairec/bineuse.git ~/bineuse; ~/bineuse/bineuse.py install")

def nettoyageBineuse():
    call("rm -rf ~/bineuse/build; mkdir ~/bineuse/build")

def clickedBineuseNew():
    call("~/bineuse_new/bineuse.py run")

def installBineuseNew():
    print(PATH + "/bineuse_new")
    if os.path.exists(PATH + "/bineuse_new"):
        call("cd ~/bineuse_new; git reset --hard; git pull; git checkout new_gui")
    else:
        call("git clone git@github.com:lemairec/bineuse.git ~/bineuse_new; cd ~/bineuse_new; git checkout new_gui; ~/bineuse_new/bineuse.py install")

def nettoyageBineuseNew():
    call("rm -rf ~/bineuse_new/build; mkdir ~/bineuse_new/build")

window = Tk()
window.title("AGTF app")
window.geometry('800x600')


btn = Button(window, text="GPS", command=clickedGPS, height = 5, width = 20)
btn.grid(column=0, row=0)

btn = Button(window, text="update GPS", command=installGPS, height = 5, width = 20)
btn.grid(column=0, row=1)

btn = Button(window, text="clean GPS", command=nettoyageGPS, height = 5, width = 20)
btn.grid(column=0, row=2)


btn = Button(window, text="Bineuse", command=clickedBineuse, height = 5, width = 20)
btn.grid(column=1, row=0)

btn = Button(window, text="update Bineuse", command=installBineuse, height = 5, width = 20)
btn.grid(column=1, row=1)

btn = Button(window, text="clean Bineuse", command=nettoyageBineuse, height = 5, width = 20)
btn.grid(column=1, row=2)

btn = Button(window, text="Bineuse new", command=clickedBineuseNew, height = 5, width = 20)
btn.grid(column=2, row=0)

btn = Button(window, text="update Bineuse", command=installBineuseNew, height = 5, width = 20)
btn.grid(column=2, row=1)

btn = Button(window, text="clean Bineuse", command=nettoyageBineuseNew, height = 5, width = 20)
btn.grid(column=2, row=2)




btn = Button(window, text="update AGTF", command=update_setup)
btn.grid(column=3, row=5)


window.mainloop()
