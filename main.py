'''
    itWorks - A little script that notifies you when your
              internet is up.
'''

import subprocess
import time


cmd = "ping www.google.com -c 4"
title = "Notification"
message = "Your Internet is now working."


print "Working"

def ping():
    p = subprocess.call(cmd, shell=True, stdout=subprocess.PIPE)
    # to supress output, i've used PIPE for stdout
    return p
try:
    while True:
        result = ping()
        if result == 0:
            subprocess.call("notify-send '{}' '{}'".format(title, message), shell=True)
            break
        elif result == 2: 
        # return value of 2 means that process got ctrl-c'd
            print "\nExiting"
            break
        else:
            time.sleep(4)
except KeyboardInterrupt:
    print "\b\bExiting"

