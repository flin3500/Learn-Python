import socket
import threading

def receiver(udp_socket):
        #  receive data
        while True:
                recv_data = udp_socket.recvfrom(1024)
                print(recv_data)

def sender(udp_socket):
        # 4. send data
        while True:
                send_data = input("Input the data want to send")
                udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 9300))

def main():

        # 1. make a udp socket
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 2. bind information
        udp_socket.bind(("", 7788))

        t1 = threading.Thread(target=receiver, args=(udp_socket,))
        t2 = threading.Thread(target=sender, args=(udp_socket,))

        t1.start()
        t2.start()

if __name__ == "__main__":
        main()