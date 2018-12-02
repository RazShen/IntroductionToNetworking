from socket import socket, AF_INET, SOCK_DGRAM
import sys

<<<<<<< HEAD:Exercise1/Question3/q_3_server.py
=======
# Checking valid input
>>>>>>> d8738bdfac6814a46adee0ad3897a8599d137ef8:Exercise1/Question3/server.py
if len(sys.argv) < 5:
    print("Not enough arguments, quitting...")

# Parsing the input
my_port = int(sys.argv[1])
parent_ip = sys.argv[2]
parent_port = int(sys.argv[3])
ips_file_name = sys.argv[4]

domain_to_ip = {}

# Initializing the dictionary using the ips file
#  (dictionary is key: domain_name, value: ip_address)
try:
    with open(ips_file_name) as ips_file:
        for line in ips_file:
            if line.index(",") < 0:
                continue
            name, ip = line.split(",")
            ip = ip.strip()
            domain_to_ip[name] = ip
<<<<<<< HEAD:Exercise1/Question3/q_3_server.py

=======
>>>>>>> d8738bdfac6814a46adee0ad3897a8599d137ef8:Exercise1/Question3/server.py
except Exception:
    print("error in loading ips file, quitting...")
    exit()

# Creating a socket and binding to it using our ip
my_socket = socket(AF_INET, SOCK_DGRAM)
my_ip = '127.0.0.1'
my_socket.bind((my_ip, my_port))

# Asking the parent for a specific domain
def request_from_parent(domain):
    temporary_socket = socket(AF_INET, SOCK_DGRAM)
    temporary_socket.sendto(domain, (parent_ip, parent_port))
    result, sender = temporary_socket.recvfrom(2048)
    temporary_socket.close()
    return result

<<<<<<< HEAD:Exercise1/Question3/q_3_server.py

def flush():
    with open(ips_file_name, 'w+') as ips:
        for key, value in domain_to_ip.items():
            ips.write(key + "," + value + "\n")


=======
# After receiving from the parent the new domain ip address, write it to the ips file
def flush():
    with open(ips_file_name, 'w+') as ips:
        for key,value in domain_to_ip.items():
            ips.write(key+"," + value + "\n")
        
# Server always running receving queries from clients.
>>>>>>> d8738bdfac6814a46adee0ad3897a8599d137ef8:Exercise1/Question3/server.py
while True:
    domain, sender_info = my_socket.recvfrom(2048)

    if domain in domain_to_ip:
        address = domain_to_ip[domain]
    else:
        address = request_from_parent(domain)
        domain_to_ip[domain] = address
        flush()
    my_socket.sendto(address, sender_info)
