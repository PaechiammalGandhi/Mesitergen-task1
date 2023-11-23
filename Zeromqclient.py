import zmq

def zmq_client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    try:
        socket.connect("tcp://localhost:5000")  # Use the correct server address with the "tcp" protocol

        message = "Hello, ZeroMQ Server!"
        print(f"Sending message: {message}")

        socket.send_string(message)

        response = socket.recv_string()
        print(f"Received response: {response}")

    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    zmq_client()

