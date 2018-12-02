import socket

IP = '127.0.0.1'
PORT = 12345
RECEIVING_SIZE = 4096
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))

msg = raw_input("Message to send: ")
while not msg == 'quit':
    socket.send(msg)
    data = socket.recv(RECEIVING_SIZE)
    print "Server sent: ", data
    msg = raw_input("Message to send: ")
socket.close()

