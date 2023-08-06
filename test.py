import socket


def send_file(file_path, ip_address):
    with open(file_path, 'rb') as f:
        data = f.read()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, 1234))
    s.sendall(data)
    s.close()

send_file("test.txt", "192.168.16.1")