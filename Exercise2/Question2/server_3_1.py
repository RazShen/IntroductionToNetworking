from socket import socket, AF_INET, SOCK_DGRAM

# This is a UDP server for the 15,000 'A's UDP client.

# Server related constants
IP = '0.0.0.0'
PORT = 12345
RECEIVING_BYTES = 20000
# Create a UDP socket.
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((IP, PORT))

# Receive from the client a message, and print it(Expecting 15000 'A's).
data, sender_info = server_socket.recvfrom(RECEIVING_BYTES)
print 'Connection from: ', sender_info
print 'Received:', data
# Respond a B, and close.
server_socket.sendto('B', sender_info)
server_socket.close()
