#!/usr/bin/python2
import socket
# Change to your target host example: target_host = "www.google.com"
target_host = "www.example.com"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data, change 'Host:' to the target host, example: Host: google.com
client.send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

# receive some data 
response = client.recv(4096)

print(response)
