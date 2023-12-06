import socket
import threading

def listen_server(client_socket):
    while True:
        response = client_socket.recv(1024)
        print(f"Server: {response.decode()}")


def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set up the server information
    server_host = '127.0.0.1'  # Change this to the server's host
    server_port = 7839  # Change this to the server's port

    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")


        thread1 = threading.Thread(target=listen_server, args=(client_socket,))
        thread1.start()

        while True:
            # Send a message to the server
            message = input("Enter your message ('quit' to exit): ")
            if message.lower() == 'quit':
                break

            client_socket.sendall(message.encode())

    except ConnectionRefusedError:
        print("Connection refused. The server is not running or unavailable.")
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()
