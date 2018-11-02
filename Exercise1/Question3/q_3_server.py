from socket import socket, AF_INET, SOCK_DGRAM
import sys

if len(sys.argv) < 5:
    print("Not enough arguments, quitting...")
port = sys.argv[1]
parentIP = sys.argv[2]
parentPort = sys.argv[3]
ipsFileName = sys.argv[4]
ips_name_ip_dict = {}
try:
    with open(ipsFileName) as ips_file:
        for line in ips_file:
            name, ip = line.split(",")
            ips_name_ip_dict[name] = ip
            
except:
    print("error in loading ips file, quitting...")
    exit()
s = socket(AF_INET, SOCK_DGRAM)
source_ip = '127.0.0.1'
source_port = 8080
s.bind((source_ip, source_port))

while True:
	data, sender_info = s.recvfrom(2048)
	print "Message: ", data, " from: ", sender_info
	s.sendto(data.upper(), sender_info)