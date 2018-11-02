from socket import socket, AF_INET, SOCK_DGRAM, timeout
import sys

if (len(sys.argv)) < 3:
    print("not enough arguments, quitting...")
# Parsing the input
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
# Creating socket that uses udp and ipv4
my_socket = socket(AF_INET, SOCK_DGRAM)
# Getting input from the user
domain = raw_input("")
# Client always running asking queries (untill stop)
while True:
    my_socket.sendto(domain, (server_ip, server_port))
    ip, sender_info = my_socket.recvfrom(2048)
    print ip
    domain = raw_input("")

# Closing the socket after finishing sending
my_socket.close()
