from socket import socket, AF_INET, SOCK_DGRAM
import time

"""
This client is designed only for the tthird part of the question.
This is a UDP client that sends 11 times two messages, both containing the letter 'A'.
Each iteration is separated by a two seconds waiting time.
"""
# Connection related constants
IP = '127.0.0.1'
PORT = 8080
RECEIVING_BYTES = 2048
# Create a UDP socket.
s = socket(AF_INET, SOCK_DGRAM)
# Send as instructed the messages using UDP sendTo call.
for i in range(11):
    msg = 'A'
    s.sendto(msg, (IP, PORT))
    s.sendto(msg, (IP, PORT))
    time.sleep(2)
    data, sender_info = s.recvfrom(RECEIVING_BYTES)
    print(data)
# Print the response from the server and close the socket.
data, sender_info = s.recvfrom(RECEIVING_BYTES)
print "Server sent: ", data
s.close()
