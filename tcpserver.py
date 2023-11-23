import socket

IP = "127.0.0.1"
PORT = 5006

def simple_tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((IP, PORT))
    tcp_socket.listen(1) 

    print(f"TCP Server listening on {IP}:{ PORT}")

    while True:
        conn, addr = tcp_socket.accept()
        print(f"TCP Connection address: {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"TCP Received message: {data.decode()} from {addr}")
            conn.send("TCP Server: Message received".encode())

        print(f"Connection from {addr} closed.")
        conn.close()

if __name__ == "__main__":
    simple_tcp_server()
