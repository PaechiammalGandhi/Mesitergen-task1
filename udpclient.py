import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    message = "Hello, UDP Server!"
    udp_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))

    data, addr = udp_socket.recvfrom(1024)
    print(f"UDP Received response: {data.decode()} from {addr}")

finally:
    udp_socket.close()

