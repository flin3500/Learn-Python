import socket

def main():
    # 1. create a tcp socket 
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. bind local information
    tcp_server_socket.bind(("",7788))

    # 3. listening
    tcp_server_socket.listen(128)

    # 4. wait for the data and create the client socket
    client_socket, client_addr = tcp_server_socket.accept()

    # 5. receive the data
    recv_data = client_socket.recv(1024)

    print(recv_data)

    # 6. send the data
    client_socket.send("Hi from server".encode("utf-8"))
    
    # 7. close server and client
    client_socket.close()
    tcp_server_socket.close()
    

if __name__ == '__main__':
    main()
