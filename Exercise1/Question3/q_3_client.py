from socket import socket, AF_INET, SOCK_DGRAM
import sys

if (len(sys.argv)) < 3:
    print("not enough arguments, quitting...")
serverIP = sys.argv[1]
serverPort = sys.argv[2]

s = socket(AF_INET, SOCK_DGRAM)
dest_ip = '127.0.0.1'
dest_port = 8080
msg = raw_input("")

while not msg == 'quit':
    s.sendto(msg, (dest_ip, dest_port))
    data, sender_info = s.recvfrom(2048)
    print "Server sent: ", data
    msg = raw_input("Message to send: ")
s.close()
