import socket

# Defining the connection-related constants
IP = '127.0.0.1'
PORT = 12345
RECEIVING_SIZE = 4096
# Creating the socket and connecting to the server.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))

# The loop that sends the user's message to the server and outputs the response, and so on.
msg = raw_input("Message to send: ")
while not msg == 'quit':
    socket.send(msg)
    data = socket.recv(RECEIVING_SIZE)
    print "Server sent: ", data
    msg = raw_input("Message to send: ")
# Close the socket once finished.
socket.close()
