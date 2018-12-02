from socket import socket, AF_INET, SOCK_DGRAM


server_socket = socket(AF_INET, SOCK_DGRAM)
source_ip = '0.0.0.0'
source_port = 8080
server_socket.bind((source_ip, source_port))

data = "hi"
a_counter  = 0
sender_info = 0
while data!='':
    data, sender_info = server_socket.recvfrom(1024)
    if data == 'A':
        a_counter += 1
    elif data == 'AA':
        a_counter += 2
    print 'Received:', data
    if a_counter == 22:
        break
server_socket.sendto('B', sender_info)
print 'Client disconnected'
server_socket.close()
