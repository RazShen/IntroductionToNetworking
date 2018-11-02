from socket import socket, AF_INET, SOCK_DGRAM
import sys

print(len(sys.argv))
if len(sys.argv) < 5:
    print("Not enough arguments, quitting...")
my_port = sys.argv[1]
parent_ip = sys.argv[2]
parent_port = sys.argv[3]
ips_file_name = sys.argv[4]
domain_to_ip = {}
try:
    with open(ips_file_name) as ips_file:
        for line in ips_file:
            if line.index(",") < 0:
                continue
            name, ip = line.split(",")
            ip = ip.strip()
            domain_to_ip[name] = ip

except:
    print("error in loading ips file, quitting...")
    exit()

my_socket = socket(AF_INET, SOCK_DGRAM)
my_ip = '127.0.0.1'
my_socket.bind((my_ip, my_port))


def request_from_parent(domain):
    temporary_socket = socket(AF_INET, SOCK_DGRAM)
    temporary_socket.sendto(domain, (parent_ip, parent_port))
    result, sender = temporary_socket.recvfrom(2048)
    temporary_socket.close()
    return result

def flush():
    with open(ips_file_name, 'w+') as ips:
        for key,value in domain_to_ip.items():
            ips.write(key+"," + value + "\n")
        

while True:
    domain, sender_info = my_socket.recvfrom(2048)
    if domain in domain_to_ip:
        address = domain_to_ip[domain]
    else:
        address = request_from_parent(domain)
        domain_to_ip[domain] = address
        flush()
    my_socket.sendto(address, sender_info)

