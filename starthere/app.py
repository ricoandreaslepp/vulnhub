import socket

def main():
    # Define the host and port to listen on
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 31337  # Port to listen on

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the host and port
        server_socket.bind((host, port))

        # Listen for incoming connections
        server_socket.listen()

        print(f"Server listening on port {port}...")

        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()

            # Send a response to the client
            client_socket.sendall(b"ctf{susp4ci0us_0pen_p0rt5}")

            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    main()
