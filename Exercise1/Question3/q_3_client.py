from socket import socket, AF_INET, SOCK_DGRAM
import sys

if (len(sys.argv)) < 3:
    print("not enough arguments, quitting...")
server_ip = sys.argv[1]
server_port = sys.argv[2]

my_socket = socket(AF_INET, SOCK_DGRAM)
domain = raw_input("")
while True:
    my_socket.sendto(domain, (server_ip, server_port))
    ip, sender_info = s.recvfrom(2048)
    print ip
    domain = raw_input("")
s.close()
