import socket
import time

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(("", 9300))
listen_socket.listen(128)
listen_socket.setblocking(False)

serve_socket_list = list()

while True:

    time.sleep(0.5)

    try:
        new_socket, new_addr = listen_socket.accept()
    except Exception as ret:
        print("---No new client---")
    else:
        print("---New client come----")
        new_socket.setblocking(False)
        serve_socket_list.append(new_socket)
        
    for serve_socket in serve_socket_list:
        try:
            recv_data = serve_socket.recv(1024)
        except Exception as ret:
            print("----No data from this client----")
        else:
            print("-----No Exception-----")
            print(recv_data)
            if recv_data:
                print("----client send data-----")
            else:
                serve_socket.close()
                serve_socket_list.remove(serve_socket)
                print("----serve socket close---")