import socket
import threading
import os

# Server related constants
IP = '0.0.0.0'
PORT = 16670
MAX_CLIENTS = 5

# Constant HTTP message formats.

HTTP_OK = "HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n{content}"
HTTP_NOT_FOUND = "HTTP/1.1 404 Not Found\r\nConnection: close"
HTTP_REMOVED_PERM = "HTTP/1.1 301 Moved Permanently\r\nConnection: close\r\nLocation: /result.html\r\n\r\n"

# The directory in which the server's resources are saved.
files_directory = "files"


# Returns a file's content according to it's relative location. If it doesn't exist- returns ""
def fetch_file(file_identifier):
    path = files_directory + "/" + file_identifier
    try:
        if file_identifier.endswith(".jpg"):
            my_file = open(path, "rb")
        else:
            my_file = open(path, "r")
        # Could find the file,
        ans = my_file.read()
        my_file.close()
        return ans
    except:  # Could not open or find the rile, return none.
        return ""


# The function that handles a connected client
def handle_client(client_socket):
    message = client_socket.recv(1024)
    print(message)
    # Split the request by lines.
    splitted_message = message.split("\r\n")
    # The only line we care about is the first one, and if it is "GET .... HTTP/1.1"
    request_line = splitted_message[0].split(" ")
    ans = HTTP_NOT_FOUND  # Starting with not found and if we can find it we send a different answer
    if request_line[0] == "GET":  # Ignore requests other than GET
        resource_identifier = request_line[1]  # The URI we are looking for
        if resource_identifier == "/redirect":  # Handling the /redirect case.
            ans = HTTP_REMOVED_PERM
        else:
            if resource_identifier == "/":  # Handling the index.html case.
                resource_identifier = "index.html"
            # try to fetch the file contents
            file_content = fetch_file(resource_identifier)
            if file_content:  # If we found contents, we will return HTTP OK with the content. o/w ans stays 404 Not found.
                ans = HTTP_OK.format(content=file_content)
    print ans
    # Send the final answer to the client and close the connection with it.
    client_socket.send(ans)
    client_socket.close()


# Create the socket, bind it to the requested port, and listen for clients.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(MAX_CLIENTS)

# The server mains loop that accepts clients and servers them.
while True:
    # Wait for a new client.
    client_socket, client_address = server_socket.accept()
    print 'New Connection: ', client_address
    # Handle the client, in a different thread so our server can handle multiple clients at a time.
    threading.Thread(target=handle_client, args=[client_socket]).start()
