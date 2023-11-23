import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((UDP_IP, UDP_PORT))

print(f"UDP Server listening on {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f"UDP Received message: {data.decode()} from {addr}")
    udp_socket.sendto("UDP Server: Message received".encode(), addr)
