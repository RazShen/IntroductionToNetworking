from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
dest_ip = '0.0.0.0'
dest_port = 8080
msg = ''.join('A' for x in range(15000))
s.sendto(msg, (dest_ip, dest_port))
data, sender_info = s.recvfrom(2048)
print "Server sent: ", data
s.close()
