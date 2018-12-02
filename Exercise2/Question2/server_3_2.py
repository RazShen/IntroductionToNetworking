from socket import socket, AF_INET, SOCK_DGRAM

# Server related constants
IP = '0.0.0.0'
PORT = 12345
RECEIVING_BYTES = 1024
# Create the socket and bind to our port.
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((IP, PORT))

data = "hi"  # Dummy initialized the data variable.
a_counter = 0
while data != '':
    # Receive data from the user.
    data, sender_info = server_socket.recvfrom(RECEIVING_BYTES)
    if data == 'A':
        a_counter += 1
    elif data == 'AA':
        a_counter += 2
    print 'Received:', data
    # Once 22 'A's are received(which is the amount expected), we can stop waiting for more messages.
    if a_counter == 22:
        server_socket.sendto('B', sender_info)
# Send back 'B' and close the connection.
server_socket.close()
