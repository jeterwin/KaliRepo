import sys
import os
from threading import Thread
import subprocess

def createSocket(ip):
    try:
        result = str(subprocess.check_output("ping -a -n 1 " + ip))
        if "Destination" not in result:
            print("Found device with IP:", ip)
			#print("Device found at IP: {}".format(ip))
    except:
        sys.exit()

# Not finished yet
for i in range(0, 255):
    ip = "192.168.0." + str(i)
	# First check for speed with
	#createSocket(index), threading is slower if you are running the code
	# with your own IP as a test
    thread = Thread(target=createSocket, args=(ip, ))
    thread.start()