import socket

"""
This client is designed only for the first part of the question.
The client sends a sequence of 15,000 'A's in one message, and print the output message from the server.
"""
# Connection related constants.
IP = '127.0.0.1'
PORT = 12345
RECEIVING_SIZE = 4096
# Open a socket and connect to the server.
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))
# Creating our message using list comprehension.
msg = ''.join('A' for x in range(15000))
# Send the message, and print the received response from the server.
socket.send(msg)
data = socket.recv(RECEIVING_SIZE)
print "Server sent: ", data
# At last, close the connection.
socket.close()


