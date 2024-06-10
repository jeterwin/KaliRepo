import socket
import tqdm

#host = "0.0.0.0"
host = "ip"
port = 20

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, addr = server.accept()

# First send the size, create the size yourself and continue the rest
file_name = client.recv(9).decode() # 9 bites for "gotit.txt"
print(file_name)

bites_file_size = 0

file = open(file_name, "wb")
file_bytes = b""

while True:
    x = str(client.recv(1).decode())
    if x.isdigit():
        bites_file_size = bites_file_size * 10 + int(x)
    else:
        file_bytes += x.encode()
        break

done = False

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=bites_file_size)

while not done:
    data = client.recv(1)
    
    if file_bytes[-4:] == b"<ME>":
        done = True
    else:
        file_bytes += data
    progress.update(1)

file.write(file_bytes)
file.close()
client.close()
server.close()
