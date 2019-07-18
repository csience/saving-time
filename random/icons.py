#!/usr/bin/env python

'''
(*) Replaces "showicons" and "hideicons" bash scripts in /bin/ directory for macOS. Works on 10.12.4.
(*) Usage: "icons -b ([true,false])
(*) mkanger@me.com
(*) 04-15-2017
'''

import subprocess
import getopt
import sys

if sys.argv:
    o,a = getopt.getopt(sys.argv[1:], 'b:')
    opt = o[0][1]
else:
    opt = "false"

# defaults write com.apple.finger CreateDesktop [true/false]
try:
    subprocess.check_output(["defaults","write","com.apple.finder","CreateDesktop",opt])
    # restart Finder PID
    subprocess.call(["killall","Finder"])
except:
    print("error")