import sys
from threading import Thread
import socket

TARGET = socket.gethostbyname(sys.argv[1])

def createSocket(index):
	try:
		socket.setdefaulttimeout(1)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = s.connect_ex((TARGET, index))
		
		if result == 0:
			print("Port open at: {}".format(index))
			
		s.close()
	except:
		sys.exit()

for i in range(0, 65535):
	# First check for speed with
	#createSocket(i)#, threading is slower if you are running the code
	# with your own IP as a test
	thread = Thread(target=createSocket, args=(i, ))
	thread.start()