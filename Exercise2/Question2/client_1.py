import socket

IP = '127.0.0.1'
PORT = 12345
RECEIVING_SIZE = 4096
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))
msg = ''.join('A' for x in range(15000))
socket.send(msg)
data = socket.recv(RECEIVING_SIZE)
print "Server sent: ", data
socket.close()


