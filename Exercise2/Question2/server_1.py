import socket

# Server related constants
IP = '0.0.0.0'
PORT = 12345
RECEIVING_BYTES = 20000
NUM_CLIENTS = 5
# Creating the socket, binding to the server's port, and listening for clients.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(NUM_CLIENTS)

# Server's main loop, which accepts clients and handles the data received by them.
while True:
    # Accept a new client
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    # Read the data from the client(Expecting to see 15000 'A's)
    data = client_socket.recv(RECEIVING_BYTES)
    print 'Received:', data
    # Answer "B" and close the connection(The conversation is over now).
    client_socket.send('B')
    print 'Client disconnected'
    client_socket.close()
