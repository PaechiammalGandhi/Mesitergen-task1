import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5006

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((TCP_IP, TCP_PORT))

message = "Hello, TCP Server!"
tcp_socket.send(message.encode())

data = tcp_socket.recv(1024)
print(f"TCP Received response: {data.decode()}")

tcp_socket.close()
