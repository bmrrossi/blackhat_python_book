import socket

server_ip = "127.0.0.1"
server_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((server_ip, server_port))

client.send("teste".encode())

response = client.recv(4096)

print(response)