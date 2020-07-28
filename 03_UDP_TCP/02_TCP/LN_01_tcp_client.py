import socket

def main():
    # 1. make a tcp socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. connect to the server
    server_ip = input("Input server IP: ")
    server_port = int(input("Input server Port: "))
    server_addr = (server_ip, server_port)
    tcp_client_socket.connect(server_addr) 

    # 3. input data
    send_data = input("Input data to send: ")
    tcp_client_socket.send(send_data.encode("utf-8"))

    # 4. close tcp socket
    tcp_client_socket.close()

if __name__ == "__main__":
    main()