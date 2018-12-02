from socket import socket, AF_INET, SOCK_DGRAM
import time

s = socket(AF_INET, SOCK_DGRAM)
dest_ip = '0.0.0.0'
dest_port = 8080

for i in range(11):
    msg = 'A'
    s.sendto(msg, (dest_ip, dest_port))
    s.sendto(msg, (dest_ip, dest_port))
    time.sleep(2)
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
s.close()
