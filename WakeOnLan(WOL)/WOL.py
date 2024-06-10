import sys
import socket

macAddress = sys.argv[1]
magicPacket = "\xFF" * 6 + macAddress * 16
deviceIP = sys.argv[2]
port = 9
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(magicPacket.encode(), (deviceIP, port))