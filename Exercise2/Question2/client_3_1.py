from socket import socket, AF_INET, SOCK_DGRAM

"""
This client is designed only for the third part of the question.
This is a UDP client that sends a sequence of 15,000 'A's in one message, and prints the output message from the server.
Our goal is to show in the final answers document, that fragmentation in the network layer would occur in this scenario.
"""
# Connection related constants
IP = '0.0.0.0'
PORT = 8080
RECEIVING_BYTES = 2048
# Create a UDP socket.
s = socket(AF_INET, SOCK_DGRAM)
# Create the message using list comprehension.
msg = ''.join('A' for x in range(15000))
# Send the message using UDP sendTo call.
s.sendto(msg, (IP, PORT))
# receive data(from the server) and print it.
data, sender_info = s.recvfrom(RECEIVING_BYTES)
print "Server sent: ", data
# Close the socket
s.close()
