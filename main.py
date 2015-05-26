'''
	itWorks - A little script that notifies you when your
	          internet is up.
'''

import os
import time

#TODO: find a way to supress ping output and a way to exit the script
#FIXME: keyboard interrupt doesn't work every time because of sleep().
#       find a solution.

cmd = "ping www.google.com -c 4"
title = "Notification"
message = "Your Internet is now working."
try:
	while True:
		result = os.system(cmd)
		if result == 0:
			os.system("notify-send '{}' '{}'".format(title, message))
			break
		else:
			time.sleep(4)
except KeyboardInterrupt, e:
	print "Exiting"

