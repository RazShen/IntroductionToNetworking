import socket, threading, time

# Server related constants
IP = '0.0.0.0'
PORT = 12347
RECEIVING_BYTES = 1024
NUM_CLIENTS = 5
# Create the server socket, bind it to the right port, and listen for a client.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(NUM_CLIENTS)
# Accept a new client and handle it.
client_socket, client_address = server.accept()
print 'Connection from: ', client_address
data = "hi"  # Dummy initial value
a_counter = 0  # This counter remembers how many 'A's were sent so far.
while data != '':  # The client will send '' if it closes.
    data = client_socket.recv(RECEIVING_BYTES)
    client_socket.send('B')
    if data == 'A':  # Message is one A
        a_counter += 1
    elif data == 'AA':  # Message is two 'A's
        a_counter += 2
    print 'Received:', data
    # If we received 22 'A's, which is the amount expected, we can stop the loop.
    if a_counter == 22:
        break
# Answer B and close both sockets
print 'Client disconnected'
client_socket.close()
server.close()
