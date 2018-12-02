import socket, time

"""
This client is designed only for the second part of the question.
The client sends 11 times two messages, both containing the letter 'A'.
Each iteration is separated by a two seconds waiting time.
We will(possibly) see how TCP merges the two messages merge into one, in the final answers document.
"""

# Connection related constants
IP = '127.0.0.1'
PORT = 12347
RECEIVING_SIZE = 4096
# Create the socket and connect to the server
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))
# Sending the messages as instructed.
for i in range(11):
    msg = 'A'
    # As instructed, we send the message twice using separate yet consecutive "send" calls.
    socket.send(msg)
    socket.send(msg)
    time.sleep(2)
# Print the response from the server and close the connection.
data = socket.recv(RECEIVING_SIZE)
print "Server sent: ", data
socket.close()


