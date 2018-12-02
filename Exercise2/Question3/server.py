
import socket
import threading
import os

IP = '0.0.0.0'
PORT = 16670
MAX_CLIENTS = 5

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(MAX_CLIENTS)

files_directory = "files"

HTTP_OK = "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n{content}"
HTTP_NOT_FOUND = "HTTP/1.1 404 Not Found\r\nConnection: close"
HTTP_REMOVED_PERM = "HTTP/1.1 301 Moved Permanently\r\nConnection: close\r\nLocation: /result.html\r\n\r\n"
def fetch_file(file_identifer):
    path = files_directory + "/" + file_identifer
    try:
        if file_identifer.endswith(".jpg"):
            file = open(path, "rb")
        else:
            file = open(path, "r")
        ans = file.read()
        file.close()
        return ans
    except:
        return ""


def handle_client(client_socket):
    message = client_socket.recv(1024)
    print(message)
    # CHECK FOR BUGS IN THE SPLIT FUNCTIONS!!!
    splitted_message = message.split("\r\n")
    request_line = splitted_message[0].split(" ")
    ans = HTTP_NOT_FOUND
    if request_line[0] == "GET":
        resource_identifier = request_line[1]
        if resource_identifier == "/redirect":
            ans = HTTP_REMOVED_PERM
        else:
            if resource_identifier == "/":
                resource_identifier = "index.html"
            file_content = fetch_file(resource_identifier)
            if file_content:
                ans = HTTP_OK.format(content=file_content)
    client_socket.send(ans)
    client_socket.close()


while True:
    client_socket, client_address = server_socket.accept()
    print 'New Connection: ', client_address
    threading.Thread(target=handle_client, args=[client_socket]).start()
