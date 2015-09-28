#Simple TCP client

import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create a socket object with the 2 socket parameters
#AF_INET: means standard IPv4 or hostname
#SOCK_STREAM: indicates this will be a TCP client

#Connect to Client
client.connect((target_host, target_port))

#Send some data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#Recieve some data
response = client.recv(4096)

print(response)