import socket, time

IP = '172.19.3.40'
PORT = 12347
RECEIVING_SIZE = 4096
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((IP, PORT))
for i in range(11):
    msg = 'A'
    socket.send(msg)
    socket.send(msg)
    time.sleep(2)
data = socket.recv(RECEIVING_SIZE)
print "Server sent: ", data
socket.close()


