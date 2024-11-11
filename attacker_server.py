import socket

def start_server(host="127.0.0.1", port=5005):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Listening on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            
            with client_socket:
                log_data = client_socket.recv(1024).decode('utf-8')
                if log_data:
                    print("Received log data:", log_data)
                    
                    with open("received_logs.txt", "a") as log_file:
                        log_file.write(log_data + "\n")
                else:
                    print("No data received")

# Run the server
if __name__ == "__main__":
    start_server()