import socket

# Server related constants
IP = '0.0.0.0'
PORT = 12345
NUM_CLIENTS = 5
RECEIVING_BYTES = 1024
# Create the socket, bind it to the port, and listen for clients.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(NUM_CLIENTS)

# The server's main loop, accepts clients and handles the client until it decides to close the connection.
# For now, this is not a great server, since it can only server one client at a time.
while True:
    # wait for a connection from a new client
    client_socket, client_address = server.accept()
    print 'Connection from: ', client_address
    # Handle the client: wait for input and then send the output in upper case letters.
    data = client_socket.recv(RECEIVING_BYTES)
    while not data == '':  # When the client disconnects TCP automatically sends '' and we know to stop the loop.
        print 'Received:', data
        client_socket.send(data.upper())
        data = client_socket.recv(RECEIVING_BYTES)
    # Close the client and accept a new one in the next iteration.
    print 'Client disconnected'
    client_socket.close()
