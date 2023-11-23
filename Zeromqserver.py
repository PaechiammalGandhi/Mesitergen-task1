import zmq

def zmq_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5000")  # Use the desired port (5000 in this example) with the "tcp" protocol

    print("ZeroMQ Server listening on tcp://*:5000")

    try:
        while True:
            message = socket.recv_string()
            print(f"ZeroMQ Received message: {message}")

            # Process the received message here (acknowledge, reply, etc.)
            response = f"ZeroMQ Server: Acknowledgment for {message}"

            socket.send_string(response)

    finally:
        socket.close()
        context.term()

if __name__ == "__main__":
    zmq_server()


