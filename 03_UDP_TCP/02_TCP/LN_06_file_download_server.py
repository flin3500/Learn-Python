import socket

def send_file(client_socket):

    # 1. receive the file name
    file_name = client_socket.recv(1024).decode("utf-8")
    print("The download file name is %s " % (file_name))

    # 2. open the file and read data
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("Can not open %s" % file_name)

    # 3. send the data
    if file_content:
        client_socket.send(file_content)

def main():
    # 1. create a tcp socket 
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. bind local information
    tcp_server_socket.bind(("",7788))

    # 3. listening
    tcp_server_socket.listen(128)

    while True:

        # 4. wait for the data and create the client socket
        client_socket, client_addr = tcp_server_socket.accept()

        # 5. call the send file func
        send_file(client_socket)
    
        # 6. close server and client
        client_socket.close()
        
    tcp_server_socket.close()
    

if __name__ == '__main__':
    main()
